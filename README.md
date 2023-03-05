# Face_recognition_attendance-manhatton-


This is a Python program that uses facial recognition to take attendance of people. The program uses the OpenCV and face_recognition libraries to detect faces in a video stream and match them with known faces to take attendance.

# Requirements
The program requires the following Python libraries:

OpenCV
face_recognition
numpy
csv
These libraries can be installed using pip.

# Usage
The program can be used by running the attendance.py file. Before running the program, make sure to place images of known faces in the images directory. The images should be in .jpg format and should be named after the person's name. For example, if the person's name is John, the image should be named john.jpg.

When the program is run, it captures a video stream from the default camera (0) and detects faces in the stream. The program then matches the detected faces with the known faces and takes attendance of the people present.

The attendance is stored in a CSV file with the name of the current date. The file is created in the same directory as the program.

To exit the program, press the 'q' key.

# License
This program is licensed under the MIT License.