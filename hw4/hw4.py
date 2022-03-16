# Homework : Computer Vision
# Authors  : Sam, Beck, Matthew, Chase
# Abstract :
#   Practices using the OpenCV2 library for detecting chess piece images 
#   through four different filters- Canny, Prewitt, Sobel, and Laplacian.
# Help     :
#   Run `$ pip install opencv-python` to get the OpenCV2 library.

import numpy as np
import os, glob

# 1.	Install OpenCV2 for either Python or C++. (pip install opencv-python) 
#       (2 Pts)
import cv2 as cv


# 2.	Download the dataset from 
#       https://www.kaggle.com/anshulmehtakaggl/chess-pieces-detection-images-dataset. 
#       (2 Pts)
PATH = './hw4/data'


# 3.	Write a program (either C++ or Python) to open and display each image 
#       from the Queen directory using OpenCV. Note: The imread and imshow 
#       functions will probably be helpful. (10 Pts Undergrad, 5 Pts Grad)
def problem3():
    '''This function will iterate through the entire queen's image directory,
    presenting the next image in a new window upon a key press.'''
    for f in glob.glob(PATH+'/Queen-Resized/*.jpg'):
        img = cv.imread(cv.samples.findFile(f))
        cv.imshow(f, img)
        cv.waitKey(0)
        cv.destroyAllWindows() 
    print('problem3: complete')
    pass


# 4.	Use a Hough Transform to identify lines on the first image of the queen 
#       dataset with a threshold of 50, rho of 1, theta of pi/180, max line gap 
#       of 250, and a minimal line length of 10. (10 Pts)
def problem4():
    img = cv.imread(cv.samples.findFile(PATH+'/Queen-Resized/00000000_resized.jpg'))
    # convert to grayscale
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    # indentify edges
    edges = cv.Canny(gray, 50, 150, apertureSize=3)
    lines = cv.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=10, maxLineGap=250)
    # connect endpoints to draw lines over original image
    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv.line(img,(x1,y1),(x2,y2),(0,255,0),2)
    # cv.imwrite('hough_transform_p4.jpg',img)
    cv.imshow('problem4: hough', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    print('problem 4: complete')
    pass


# 5.	Modify the program to display and save the result of running each image 
#       through a Canny filter 
#       (https://docs.opencv.org/3.4/da/d22/tutorial_py_canny.html). (20 Pts 
#       Undergrad, 10 Pts Grad)
def problem5():
    files = glob.glob(PATH+'/**/*.jpg')
    output = PATH+'/canny_filter'
    # create output folders
    folders = ['pawn_resized', 'knight-resize', 'Queen-Resized', 'Rook-resize', 'bishop_resized']
    for f in folders:
        os.makedirs(output+'/'+f, exist_ok=True)
    # run canny filter on each image of dataset and store it in output path
    for f in files:
        filepath = f.replace(PATH, '')
        img = cv.imread(cv.samples.findFile(f))
        # convert to grayscale
        gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
        # filter using canny
        cv.Laplacian
        edges = cv.Canny(img, 50, 150, apertureSize=3)
        # save result to output path
        cv.imwrite(output+filepath, edges)
    print('problem5: canny filtered output found at:', output)
    pass

# 6.	Repeat Step 4 with Prewitt, Sobel, and Laplacian filters. (10 Pts 
#       Undergrad, 5 Pts Grad)
def problem6():
    img = cv.imread(cv.samples.findFile(PATH+'/Queen-Resized/00000000_resized.jpg'))
    # convert to grayscale
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    ddepth = cv.CV_16S
    scale = 1
    delta = 0

    # [!] --- apply Prewitt filter ---
    prewitt_mask_x = np.array([[1,  1,  1],
                              [ 0,  0,  0],
                              [-1, -1, -1]])
    prewitt_mask_y = np.array([[-1, 0, 1],
                              [ -1, 0, 1],
                              [ -1, 0, 1]])
    prewitt_x = cv.filter2D(gray, ddepth, kernel=prewitt_mask_x, delta=delta)
    prewitt_y = cv.filter2D(gray, ddepth, kernel=prewitt_mask_y)

    abs_prewitt_x = cv.convertScaleAbs(prewitt_x)
    abs_prewitt_y = cv.convertScaleAbs(prewitt_y)

    prewitt = cv.addWeighted(abs_prewitt_x, 0.5, abs_prewitt_y, 0.5, 0)
    # cv.imwrite('prewitt_filter_p6.jpg', prewitt)
    cv.imshow('problem6: prewitt', prewitt)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # [!] --- perform Sobel edge detection ---
    grad_x = cv.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=3, scale=scale, delta=delta)
    grad_y = cv.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=3, scale=scale, delta=delta)

    abs_grad_x = cv.convertScaleAbs(grad_x)
    abs_grad_y = cv.convertScaleAbs(grad_y)

    sobel = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    # cv.imwrite('sobel_filter_p6.jpg', sobel)
    cv.imshow('problem6: sobel', sobel)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # [!] --- perform Laplacian edge detection ---
    laplace = cv.Laplacian(gray, ddepth=ddepth, ksize=3, scale=scale, delta=delta)
    laplace = cv.convertScaleAbs(laplace)
    # cv.imwrite('laplace_filter_p6.jpg',laplace)
    cv.imshow('problem6: laplace', laplace)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print('problem 6: complete')
    pass


def main():
    print('homework 4')
    # problem3()
    # problem4()
    # problem5()
    # problem6()
    pass

# 7.	For Grad Students Only: Quantify the differences between methods by 
#       calculating the average Mean Square Error between the outputs of each 
#       other method to Canny’s output. (20 Pts)

# --- SKIPPED FOR SAM, BECK, AND CHASE (undergrad section) ---

# program entry-point
if __name__ == "__main__":
    main()