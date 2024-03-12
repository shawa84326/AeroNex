import streamlit as st
from scipy.ndimage import sobel, gaussian_laplace
from skimage import color, filters, morphology
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Set Streamlit theme
st.set_page_config(
    page_title="Feature Extraction with Image Filters",
    page_icon="🚀",
    # layout="wide",
)

def apply_filter(input_image, filter_type):
    # Convert PIL Image to NumPy array
    input_array = np.array(input_image)

    if input_array.shape[-1] == 4:
        # If the image has an alpha channel, remove it
        input_array = input_array[:, :, :3]

    grayscale_image = color.rgb2gray(input_array)

    # Rest of the code remains unchanged...
    
    if filter_type == 'Sobel':
        filtered_image = sobel(grayscale_image)
    elif filter_type == 'Laplacian':
        filtered_image = gaussian_laplace(grayscale_image, sigma=1.0)
    elif filter_type == 'Black&White':
        filtered_image = filters.gaussian(grayscale_image, sigma=0.3)
    elif filter_type == 'Morphological':
        # Apply binary erosion and dilation as separate images
        binary_image = grayscale_image > filters.threshold_otsu(grayscale_image)
        erosion_result = morphology.binary_erosion(binary_image, morphology.disk(5))
        dilation_result = morphology.binary_dilation(binary_image, morphology.disk(5))

        # Convert boolean images to numeric type before normalization
        erosion_result = erosion_result.astype(np.float64)
        dilation_result = dilation_result.astype(np.float64)

        # Normalize the image data to [0.0, 1.0]
        erosion_result = (erosion_result - np.min(erosion_result)) / (np.max(erosion_result) - np.min(erosion_result))
        dilation_result = (dilation_result - np.min(dilation_result)) / (np.max(dilation_result) - np.min(dilation_result))

        return erosion_result, dilation_result
    elif filter_type == 'Colorize':
        # Use a predefined colormap (e.g., viridis) to colorize the grayscale image
        colorized_image = plt.cm.viridis(grayscale_image)

        # Normalize the image data to [0.0, 1.0] in each color channel
        colorized_image = (colorized_image - np.min(colorized_image)) / (np.max(colorized_image) - np.min(colorized_image))

        return colorized_image
    else:
        # Default to Sobel filter if no valid option is selected
        filtered_image = sobel(grayscale_image)

    # Normalize the image data to [0.0, 1.0]
    filtered_image = (filtered_image - np.min(filtered_image)) / (np.max(filtered_image) - np.min(filtered_image))

    return filtered_image


# Streamlit app
def main():
    st.title("Feature Extraction with Image Filters")

    # Path to your image file
    image_path = "images/filter_matrix.jpg"

    # Display the image
    st.image(image_path, caption="Your Image Caption", use_column_width=True)


    # Upload image through Streamlit
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    # Dropdown for selecting filter
    filter_type = st.selectbox("Select filter:", ['Sobel', 'Laplacian', 'Black&White', 'Morphological', 'Colorize'])

    if uploaded_image is not None:
        # Convert to PIL image
        input_image = Image.open(uploaded_image)

        # Apply selected filter
        filtered_image = apply_filter(input_image, filter_type)

        # Display images side by side using columns
        col1, col2 = st.columns(2)

        # Display original image in the first column
        with col1:
            st.image(input_image, caption='Original Image', use_column_width=True)

        # Display filtered image in the second column
        with col2:
            if filter_type == 'Morphological':
                # Display erosion and dilation results separately
                st.image(filtered_image[0], caption='Erosion Result', use_column_width=True)
                st.image(filtered_image[1], caption='Dilation Result', use_column_width=True)
            else:
                # Display other filter results
                st.image(filtered_image, caption=f'{filter_type} Filtered Image', use_column_width=True)

if __name__ == "__main__":
    main()
