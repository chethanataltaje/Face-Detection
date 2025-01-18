# Real-Time Face and Smile Detection Using OpenCV
## This project implements a real-time face and smile detection system using OpenCV's Haar Cascade Classifiers. The application processes video from your webcam and highlights detected faces and smiles with bounding boxes and labels.

### Features:
* Real-time face detection: Detects faces in the video feed and highlights them with blue bounding boxes.
* Smile detection: Identifies smiles within the detected faces and marks them with green bounding boxes.
* Live annotations: Displays labels for faces and smiles in the video.
* Easy exit
  
### Code Overview
The application uses two primary functions:

1. draw_boundary
* Purpose: Detects objects (faces or smiles) in a frame and annotates them with bounding boxes and labels.

* Parameters:
  * img: The current frame from the video feed.
  * classifier: The Haar Cascade classifier used for detection.
  * scaleFactor: Parameter specifying how much the image size is reduced at each image scale.
  * minNeighbours: Specifies how many neighbors each rectangle should have to retain it.
  * color: The color of the bounding box.
  * text: The label to display for the detected object.

2. detect
  * Purpose: Handles face detection first and then smile detection within detected face regions.
  * Parameters:
  * img: The current frame from the video feed.
  * faceCascade: Haar Cascade classifier for face detection.
  * smileCascade: Haar Cascade classifier for detecting smiles
    
### Usage:
1. Run the script
2. Webcam feed:
* The application will open your webcam and display real-time detection.
* Blue boxes: Faces detected.
* Green boxes: Smiles detected within faces.
3. Exit: press 'q' to exit the application

  Link to the demo video: https://drive.google.com/file/d/1ht7qXYCrBPqTsp06fOTykt4jnpTsbA-r/view?usp=sharing

