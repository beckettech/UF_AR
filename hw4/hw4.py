# Homework : Computer Vision
# Authors  : Sam, Beck, Matthew, Chase
# Abstract :
#   Practices using the OpenCV2 library for detecting chess piece images 
#   through four different filters- Canny, Prewitt, Sobel, and Laplacian.
# Help     :
#   Run `$ pip install opencv-python` to get the OpenCV2 library.

# 1.	Install OpenCV2 for either Python or C++. (pip install opencv-python) 
#       (2 Pts)
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 2.	Download the dataset from 
#       https://www.kaggle.com/anshulmehtakaggl/chess-pieces-detection-images-dataset. 
#       (2 Pts)

# 3.	Write a program (either C++ or Python) to open and display each image 
#       from the Queen directory using OpenCV. Note: The imread and imshow 
#       functions will probably be helpful. (10 Pts Undergrad, 5 Pts Grad)
def main():
    print('homework 4')
    pass

# 4.	Use a Hough Transform to identify lines on the first image of the queen 
#       dataset with a threshold of 50, rho of 1, theta of pi/180, max line gap 
#       of 250, and a minimal line length of 10. (10 Pts)

# 5.	Modify the program to display and save the result of running each image 
#       through a Canny filter 
#       (https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html). (20 Pts 
#       Undergrad, 10 Pts Grad)

# 6.	Repeat Step 4 with Prewitt, Sobel, and Laplacian filters. (10 Pts 
#       Undergrad, 5 Pts Grad)

# 7.	For Grad Students Only: Quantify the differences between methods by 
#       calculating the average Mean Square Error between the outputs of each 
#       other method to Canny’s output. (20 Pts)


# program entry-point
if __name__ == "__main__":
    main()