
## AeroNex Web Application ##
This React web application, titled "AeroNex," provides an interactive interface showcasing the capabilities of AeroNex drones, specifically focusing on aerial intelligence for precision operations. The application features information about the AeroNex project, its processes, technical diagrams, and the research and development team.

How to Run
Clone the Repository:

bash
Copy code
git clone [<https://github.com/rgulla16/AeroNex>]
cd <https://github.com/rgulla16/AeroNex>
Install Dependencies:
Ensure you have Node.js and npm installed on your machine. Then, install the project dependencies:

bash
Copy code
npm install
Run the React App:
Start the React development server:

bash
Copy code
npm start
This will open the application in your default web browser.

Explore the AeroNex App:

Navigate through different sections using the provided links and buttons.
The "Initiate Drone Capture," "Apply Filters," and "Detection & Classification" buttons link to specific functionalities of the AeroNex project.
The technical diagram and research & development team sections provide insights into the project's architecture and the team behind it.
Code Explanation
Images and Styling:

The application imports various images for logos, team members, technical diagrams, etc.
The styling is handled through CSS, ensuring a visually appealing and consistent design.
Main Application Component:

The App component is the main component rendering different sections of the AeroNex web application.
Sections include an overview of the AeroNex project, the capture, enhance, and detect processes, a technical diagram, and information about the research & development team.
Buttons and Links:

Buttons such as "Initiate Drone Capture," "Apply Filters," and "Detection & Classification" are linked to specific functionalities.
The application uses anchor tags (<a>) to navigate to external URLs or routes within the React app.
Team Information:

The research & development team section displays images and information about team members.
Important Notes
The application uses React and requires Node.js and npm for development.
Ensure you have the necessary images and logos in the specified paths.
Explore the React components and styling to customize the application according to your needs.


Aeronex Autonomous Drone - python code

This python app,  "Aeronex Autonomous Drone," enables users Fly the drone in a rectangular room which is 30ft by 20 ft and capture video of the objects in the room in a fixed path. The drone navigates for a short distance and takes a video and shares it in a folder called /imaging/ and then moves on to the next location and takes a video from that location till it completes a full rectangle. 

How to Run
Environment Setup:

Ensure you have Python installed on your machine.

Use the Drone:

Power on the Drone. Ensure that there are no obstacles in the drone path. Though we have used code to avoid obstacles, the drone sometimes does not detect the obstacles making it difficult for complete autonomy. This can be due to the inaccuracy of the sensors.
Wait for the wifi to start on the drone. 
Connect the laptop wifi to the drone wifi and pair it 
Once it is connected, run the fly_drone.py file using 'python3 fly_drone.py'
The drone will take over and complete the surveillence task of the room, record videos at the fixed waypoints and return to the locaiton.



AeroNex Feature Extraction with Image Filters - python code

This Streamlit app, titled "Feature Extraction with Image Filters," enables users to apply various image filters to analyze and extract features from images. Users can choose from a set of filters, including Sobel, Laplacian, Black & White, Morphological, and Colorize, and observe the effects on the uploaded images.

How to Run
Environment Setup:

Ensure you have Python installed on your machine.
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Install Dependencies:

bash
Copy code
pip install streamlit scipy scikit-image matplotlib
Run the Streamlit App:

bash
Copy code
streamlit run your_script_name.py
Replace your_script_name.py with the actual name of your Python script.

Use the App:

Open the provided URL in your web browser.
Upload an image using the "Choose an image..." button.
Select a filter from the dropdown menu to apply to the uploaded image.
View the original and filtered images side by side.
Code Explanation
Streamlit Setup:

The Streamlit app is configured with a custom title and theme.
Image Filtering Function:

The apply_filter function processes the uploaded image based on the selected filter type.
Filters include Sobel, Laplacian, Black & White, Morphological (binary erosion and dilation), and Colorize.
Main Streamlit Function:

The main function of the Streamlit app:
Displays the title and an example image.
Allows users to upload an image and choose a filter type.
Applies the selected filter and displays the original and filtered images side by side.
Important Notes
Adjustments and customizations can be made to the image filter options.
Ensure you have the required Python packages installed (streamlit, scipy, scikit-image, matplotlib).
Images for testing can be placed in the "images" folder or specified by the image_path variable.


AeroNex Image Classifier - python code
This Streamlit app, named "AeroNex Image Classifier," utilizes the YOLO (You Only Look Once) object detection model to classify objects in images. Users can classify images within a specified folder, viewing the original image, an image with classified bounding boxes, and object counts.

How to Run
Environment Setup:

Ensure you have Python installed on your machine.
Clone the Repository:

bash
Copy code
git clone <repository-url>
cd <repository-folder>
Install Dependencies:

bash
Copy code
pip install streamlit opencv-python numpy
Download YOLO Files:

Download the YOLO files (yolov3.weights, yolov3.cfg, and coco.names) from the official YOLO website or your preferred source.
Place these files in the same directory as the script.
Run the Streamlit App:

bash
Copy code
streamlit run your_script_name.py
Replace your_script_name.py with the actual name of your Python script.

Use the App:

Open the provided URL in your web browser.
Click the "Classify Images in Folder" button to initiate image classification.
View the original image, the image with classified boxes, and object counts.
Code Explanation
Streamlit Setup:

The Streamlit app is configured with a custom theme and style for improved visualization.
YOLO Model Initialization:

YOLO model and configuration files (yolov3.weights, yolov3.cfg, and coco.names) are loaded.
YOLO Object Detection Function:

The classify_image function performs object detection using the YOLO model.
Main Streamlit Function:

The main function of the Streamlit app:
Displays the title and checks for available images in a specified folder.
Initiates the classification process on button click.
Displays the original image, image with classified boxes, and object counts in three columns.
Important Notes
Ensure you have the necessary YOLO files (yolov3.weights, yolov3.cfg, and coco.names) in the script's directory.
Images for classification should be placed in the "imaging" folder.