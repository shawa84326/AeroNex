import streamlit as st
import cv2
import numpy as np
import os

# Set Streamlit theme
st.set_page_config(
    page_title="AeroNex Image Classifier",
    page_icon="🚀",
    # layout="wide",
)

# Set Streamlit style
st.markdown(
    '''
    <style>
        body {
            color: #FFFFFF;
            background-color: #000000;
            font-family: 'Helvetica', sans-serif;
        }
        .stTextInput {
            color: #000000 !important;
            background-color: #FFFFFF !important;
        }
        .st-bb {
            border-bottom: 2px solid #FFFFFF;
        }
        .st-ec {
            color: #00FFFF;
        }
    </style>
    '''
    ,
    unsafe_allow_html=True,
)


# Load YOLO model and configuration
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Function to perform YOLO object detection
def classify_image(image):
    height, width, _ = image.shape
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)
    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []

    for output in layer_outputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    return indexes, boxes, class_ids

# Streamlit app
def main():
    st.title("AeroNex Image Classifier")

    image_folder = "imaging"
    image_files = [os.path.join(image_folder, file) for file in os.listdir(image_folder) if file.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        st.warning(f"No images found in the '{image_folder}' folder.")
        return

    if st.button("Classify Images in Folder"):
        st.write("Classifying images in folder...")

        for image_file in image_files:
            image = cv2.imread(image_file)
            indexes, boxes, class_ids = classify_image(image)

            # Create three columns
            col1, col2, col3 = st.columns(3)

            # Display the original image without boxes in the first column
            col1.image(image, caption="Original Image", use_column_width=True)

            # Display the image with classified boxes in the second column
            image_with_boxes = image.copy()
            for i in range(len(boxes)):
                x, y, w, h = boxes[i]
                cv2.rectangle(image_with_boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
                label = classes[class_ids[i]]
                cv2.putText(image_with_boxes, f"{label}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            col2.image(image_with_boxes, caption="Image with Classified Boxes", use_column_width=True)

            # Display object counts in the third column
            object_counts = {}
            col3.write("Object Counts:")
            for i in range(len(boxes)):
                label = classes[class_ids[i]]
                if label not in object_counts:
                    object_counts[label] = 1
                else:
                    object_counts[label] += 1
            for label, count in object_counts.items():
                col3.write(f"{label}: {count}")

if __name__ == "__main__":
    main()
