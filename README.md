# Face and Eye Detection Program

This program utilizes OpenCV (Open Source Computer Vision Library) to detect faces and eyes in real-time video from a camera. It employs Haar cascades for face and eye recognition. The program draws rectangles around detected faces and eyes and displays corresponding labels.

## Prerequisites

Before running the program, ensure that the following requirements are met:

- Python (version 3.x) is installed.
- The OpenCV library (`cv2`) is installed.

## Installation

To set up the program, follow these steps:

1. Clone or download the program repository to your local machine.
2. Make sure you have the Haar cascade classifier files (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) in the `classifiers` directory.

## Running the Program

To run the program, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the program files are located.
3. Run the program using the command:

   ```
   py main.py
   ```

   The program will open the camera and start detecting faces and eyes in real-time video.

## Instructions

- The program uses the primary camera by default. If you have multiple cameras, make sure the correct one is selected as the primary camera.
- The video feed will be mirrored to mimic a mirror-like effect.
- Detected faces will be surrounded by a blue rectangle, and the label "Face" will be displayed above each face.
- Detected eyes will be surrounded by a green rectangle, and the label "Eye" will be displayed above each eye.
- Press the 'x' key to exit the program.

Note: If you encounter any issues or errors, make sure you have installed all the necessary dependencies and check that the Haar cascade classifier files are in the correct directory.

Enjoy using the face and eye detection program!