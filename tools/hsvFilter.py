import time

from libraries.vision.usbCamera import usbCamera
import cv2
import sys
import numpy as np
from libraries.vision.enums import * # for defining CAMERA_INDEX

def nothing(x):
    pass

# Create a window
cv2.namedWindow('Input')

# create Input for color change
cv2.createTrackbar('HMin','Input',0,179,nothing) # Hue is from 0-179 for Opencv
cv2.createTrackbar('SMin','Input',0,255,nothing)
cv2.createTrackbar('VMin','Input',0,255,nothing)
cv2.createTrackbar('HMax','Input',0,179,nothing)
cv2.createTrackbar('SMax','Input',0,255,nothing)
cv2.createTrackbar('VMax','Input',0,255,nothing)

# Set default value for MAX HSV Input.
cv2.setTrackbarPos('HMax', 'Input', 179)
cv2.setTrackbarPos('SMax', 'Input', 255)
cv2.setTrackbarPos('VMax', 'Input', 255)

# Initialize to check if HSV min/max value changes
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

# define a video capture object
camera = usbCamera(CAMERA_INDEX, False)
time.sleep(1)

waitTime = 33

while(1):

    # Capture the video frame
    # by frame
    img = camera.take_photo(False)
    output = img.copy()

    # Display the resulting frame
    cv2.imshow('Input', img)

    # get current positions of all Input
    hMin = cv2.getTrackbarPos('HMin','Input')
    sMin = cv2.getTrackbarPos('SMin','Input')
    vMin = cv2.getTrackbarPos('VMin','Input')

    hMax = cv2.getTrackbarPos('HMax','Input')
    sMax = cv2.getTrackbarPos('SMax','Input')
    vMax = cv2.getTrackbarPos('VMax','Input')

    # Set minimum and max HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])

    # Create HSV Input and threshold into a range.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(img,img, mask= mask)

    height, width, depth = img.shape
    highlight = img
    for i in range(0, height):
        for j in range(0, width):
            if not mask[i, j]:
                highlight[i, j] = img[i, j] * 0.4



            # Print if there is a change in HSV value
    if( (phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display output Input
    cv2.imshow('Output',output)
    cv2.imshow('Highlight',highlight)

    # Wait longer to prevent freeze for videos.
    if cv2.waitKey(waitTime) & 0xFF == ord('q'):
        break

# After the loop release the cap object
camera.end()
cv2.destroyAllWindows()