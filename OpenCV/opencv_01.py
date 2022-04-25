"""
    Our first script will cover basics image processing operations using images from movie .
"""

# import the necessary packages
import argparse
import imutils 
import cv2
from numpy import imag


#Command Line Arguments 
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True , help="image path")
args= vars(ap.parse_args())

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread(args["input"])
(h, w,c) = image.shape
print("Height : {} , Width : {} , Depth : {} ".format(h, w,c))

# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv2.imshow("Image" , image)
cv2.waitKey(0)
