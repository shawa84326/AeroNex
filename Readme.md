# AeroNex Application Suite Readme

## Techin513 AeroNex – Ankit Shaw, Xinyi Zhou, Ravinder Gulla

This repository contains the code for the AeroNex application suite, consisting of a React web application, image feature extraction with filters, image classification, and an autonomous drone system. Below are the instructions on how to run each component.

### AeroNex Web Application

#### Overview
The AeroNex web application is a React-based interactive interface showcasing the capabilities of AeroNex drones, with a focus on aerial intelligence for precision operations.

#### How to Run
1. Ensure you have Node.js and npm installed on your machine.
2. Install project dependencies:
    ```bash
    npm install
    ```
3. Start the React development server:
    ```bash
    npm start
    ```
4. Open the application in your default web browser by visiting the provided URL.

#### Explore AeroNex App
- Navigate through different sections using the provided links and buttons.
- Buttons like "Initiate Drone Capture," "Apply Filters," and "Detection & Classification" link to specific functionalities.
- The technical diagram and research & development team sections provide insights into the project's architecture and the team behind it.

#### Important Notes
- React and Node.js with npm are prerequisites for development.
- Ensure required images and logos are in specified paths.
- Customize the application according to your needs by exploring React components and styling.

##### Code Structure
- **App.js, App.css**
- **Image folder: images/**

### AeroNex Feature Extraction with Image Filters - Python Code

#### Overview
This Streamlit app, titled "Feature Extraction with Image Filters," allows users to apply various image filters to analyze and extract features from images.

#### How to Run
1. Ensure you have Python installed on your machine.
2. Run the Streamlit app:
    ```bash
    streamlit run filter.py
    ```
3. Open the provided URL in your web browser.
4. Upload an image and select a filter from the dropdown menu to observe the effects.

#### Important Notes
- Adjustments and customizations can be made to image filter options.
- Required Python packages: streamlit, scipy, scikit-image, matplotlib.
- Place test images in the "images" folder or specify the image_path variable.

##### Code Structure
- **filter.py**
- **Images folder: imaging/**

### AeroNex Image Classifier - Python Code

#### Overview
This Streamlit app, named "AeroNex Image Classifier," utilizes the YOLO (You Only Look Once) object detection model to classify objects in images.

#### How to Run
1. Ensure you have Python installed on your machine.
2. Download YOLO files (yolov3.weights, yolov3.cfg, coco.names) from the official YOLO website.
3. Place YOLO files in the script's directory.
4. Run the Streamlit app:
    ```bash
    streamlit run image_classification.py
    ```
5. Open the provided URL in your web browser.
6. Click the "Classify Images in Folder" button to initiate image classification.

#### Important Notes
- Ensure necessary YOLO files are in the script's directory.
- Images for classification should be in the "imaging" folder.

##### Code Structure
- **image_classification.py**
- **Images folder: imaging/**

### AeroNex Autonomous Drone - Python Code

#### Overview
This Python app, "AeroNex Autonomous Drone," enables users to fly the drone autonomously in a rectangular room, capturing videos of objects in a fixed path.

#### How to Run
1. Ensure you have Python installed on your machine.
2. Power on the drone, wait for the WiFi to start.
3. Connect the laptop to the drone's WiFi and pair.
4. Run the drone script:
    ```bash
    python3 fly_drone.py
    ```
5. The drone will take off, complete the surveillance task, record videos, and return.

#### Important Notes
- Be cautious of obstacles in the drone's path.
- Inaccuracies in sensors may affect obstacle detection.

##### Code Structure
- **fly_drone.py**

Feel free to explore, customize, and contribute to the AeroNex application suite!
