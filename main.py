#program here :trol:

#write a program that detects parallel lines in opencv

import cv2 as cv
import numpy as np


img = cv.imread('images/img1.jpg')

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) # convert to grayscale

edges = cv.Canny(gray,50,150,apertureSize = 3) # detect edges using canny edge detection
lines = cv.HoughLines(edges,1,np.pi/180,200) # detect lines using hough transform

for line in lines:
    rho,theta = line[0] # get rho and theta values which are the parameters of the line
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b)) 
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv.line(img,(x1,y1),(x2,y2),(0,0,255),2) # draw the line on the image

#resize image to fit screen
# dispimg = cv.resize(lines, (1920,1080))
dispimg = cv.resize(edges, (1920,1080))

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    cv.imshow('image',edges)