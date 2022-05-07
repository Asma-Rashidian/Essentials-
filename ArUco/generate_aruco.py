"""
    Usage of ArUco makers and AprilTags :
        1. Camera calibration
        2. Object size estimation
        3. Measuring the distance between camera and object
        4. 3D position
        5. Object orientation
        6. Robotics and autonomous navigation

    The benefits od ArUco maker over AprilTags :
        1. ArUco markers are built into the OpenCV library via the cv2.aruco submodule (i.e., we don’t need additional Python packages).
        2. The OpenCV library itself can generate ArUco markers via the cv2.aruco.drawMarker function
        3. There are online ArUco generators that we can use if we don’t feel like coding (unlike AprilTags where no such generators are easily found).
        5. There are ROS (Robot Operating System) implementations of ArUco markers.
        6. And from an implementation perspective, ArUco marker detections tend to be more accurate, even when using the default parameters.

"""

"""
    The OpenCV library has a built-in ArUco marker generator through its cv2.aruco.drawMarker function.

        The parameters to this function include:

        1. dictionary: The ArUco dictionary specifying the type of markers we’re using
        2. id: The ID of the marker we’ll be drawing (has to be a valid ID In the ArUco dictionary)
        3. sidePixels: Size in pixels of the (square) image that we’ll be drawing the ArUco marker on
        4. borderBits: Width and height (in pixels) of the border
"""
# pip install opencv-contrib-python

from ast import arg
import cv2 
import argparse 
import numpy as np 
import sys 




# N*N is the 2D bit size of ArUco maker . eg : 6*6 =36 ArUco has 36 bits 
# M : number of ArUco Ids that can be implemented with that dictionary
# These are conventions 
ARUCO_DICT = {
	"DICT_4X4_50": cv2.aruco.DICT_4X4_50,
	"DICT_4X4_100": cv2.aruco.DICT_4X4_100,
	"DICT_4X4_250": cv2.aruco.DICT_4X4_250,
	"DICT_4X4_1000": cv2.aruco.DICT_4X4_1000,
	"DICT_5X5_50": cv2.aruco.DICT_5X5_50,
	"DICT_5X5_100": cv2.aruco.DICT_5X5_100,
	"DICT_5X5_250": cv2.aruco.DICT_5X5_250,
	"DICT_5X5_1000": cv2.aruco.DICT_5X5_1000,
	"DICT_6X6_50": cv2.aruco.DICT_6X6_50,
	"DICT_6X6_100": cv2.aruco.DICT_6X6_100,
	"DICT_6X6_250": cv2.aruco.DICT_6X6_250,
	"DICT_6X6_1000": cv2.aruco.DICT_6X6_1000,
	"DICT_7X7_50": cv2.aruco.DICT_7X7_50,
	"DICT_7X7_100": cv2.aruco.DICT_7X7_100,
	"DICT_7X7_250": cv2.aruco.DICT_7X7_250,
	"DICT_7X7_1000": cv2.aruco.DICT_7X7_1000,
	"DICT_ARUCO_ORIGINAL": cv2.aruco.DICT_ARUCO_ORIGINAL,
	"DICT_APRILTAG_16h5": cv2.aruco.DICT_APRILTAG_16h5,
	"DICT_APRILTAG_25h9": cv2.aruco.DICT_APRILTAG_25h9,
	"DICT_APRILTAG_36h10": cv2.aruco.DICT_APRILTAG_36h10,
	"DICT_APRILTAG_36h11": cv2.aruco.DICT_APRILTAG_36h11
}

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True, help="path to output image containing ArUCo tag")
ap.add_argument("-i", "--id", type=int, required=True, help="ID of ArUCo tag to generate")
ap.add_argument("-t", "--type", type=str, default="DICT_ARUCO_ORIGINAL", help="type of ArUCo tag to generate")
args = vars(ap.parse_args())


# verify that the supplied ArUCo tag exists and is supported by
# OpenCV
if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(
		args["type"]))
	sys.exit(0)

    
# load the ArUCo dictionary
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])


# allocate memory for the output ArUCo tag and then draw the ArUCo
# tag on the output image
print("[INFO] generating ArUCo tag type '{}' with ID '{}'".format(
	args["type"], args["id"]))
tag = np.zeros((300, 300, 1), dtype="uint8")
cv2.aruco.drawMarker(arucoDict, args["id"], 300, tag, 1)


# write the generated ArUCo tag to disk and then display it to our
# screen
cv2.imwrite(args["output"], tag)
cv2.imshow("ArUCo Tag", tag)
cv2.waitKey(0)