# OpenCV and Python Color Detection

import argparse 
import cv2
import numpy as np 


ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--input" , required=True , help= " Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])

# define the list of boundaries , alist of colors red blue yellow and gray
# Note : in opencv we have BGR instead of RGB 
# list of tuples 
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])
]

# Loop over bounderies 
for (lower, upper) in boundaries:

	# create NumPy arrays from the boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
	mask = cv2.inRange(image, lower, upper)  # the mask is 0 and 1 
	output = cv2.bitwise_and(image, image, mask = mask)

	# show the images
	cv2.imshow("images", np.hstack([image, output]))
	cv2.waitKey(0)
