"""
    ArUco detection in images or live video stream 
        Step 1: Load image 
        Step 2: Load appropraite dictionary 
        Step 3: Define Aruco parameters 
        Step 4: Perform aruco maker detection on input image 
"""
"""
    The cv2.aruco.detectMaker function accepts three argumens 
    image : input image 
    arucoDict : the aruci=o dictionary we are using 
    parameters : The ArUco parameters used for detection (unless you have a good reason to modify the parameters, the default parameters returned by cv2.aruco.DetectorParameters_create are typically sufficient

    After applying Aruco detection the cv2.aruco.detectMaker returns :
    corners : a list that contain (x,y) -coordinates of our detected aruco makers 
    ids: aruco idsof the detected markers 
    rejected : A list of potential markers that were found but ultimately rejected due to the inner code of the marker being unable to be parsed (visualizing the rejected markers is often useful for debugging purposes)

"""
import argparse 
import cv2
import sys 
import imutils


ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--input" , required=True , type=str , help=" input image path")
ap.add_argument("-t", "--type" , type=str , default="DICT_ARUCO_ORIGINAL" , help=" type of Aruco tag to detect ")
args = vars(ap.parse_args())

# The key to this dictionary is a human-readable string (i.e., the name of the ArUco tag type). The key then maps to the value, which is OpenCV’s unique identifier for the ArUco tag type.
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

# load the input image from disk and resize it
print("[INFO] loading image...")
image = cv2.imread(args["input"])
# image = imutils.resize(image  , width=600)

# verify that the supplied ArUCo tag exists and is supported by
# OpenCV
if ARUCO_DICT.get(args["type"], None) is None:
	print("[INFO] ArUCo tag of '{}' is not supported".format(args["type"]))
	sys.exit(0)

# load the ArUCo dictionary, grab the ArUCo parameters, and detect
# the markers
print("[INFO] detecting '{}' tags...".format(args["type"]))
arucoDict = cv2.aruco.Dictionary_get(ARUCO_DICT[args["type"]])
arucoParams = cv2.aruco.DetectorParameters_create()
(corners, ids, rejected) = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

print(arucoParams)
print(corners)
print(ids)
print(rejected)

# verify *at least* one ArUco marker was detected
if len(corners) > 0:
	# flatten the ArUco IDs list
	ids = ids.flatten()

	# loop over the detected ArUCo corners
	for (makerCorner , markerID) in zip(corners , ids):
		# extract the marker corners (which are always returned in
		# top-left, top-right, bottom-right, and bottom-left order)
		corners = makerCorner.reshape((4,2))
		(topLeft , topRight , bottomRight ,bottomLeft ) = corners 
		
		# convert each of the (x, y)-coordinate pairs to integers
		topRight = (int(topRight[0]), int(topRight[1]))
		bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
		bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))
		topLeft = (int(topLeft[0]), int(topLeft[1]))

		# draw the bounding box of the ArUCo detection
		cv2.line(image, topLeft, topRight, (255,69,0), 2)
		cv2.line(image, topRight, bottomRight,(255,69,0), 2)
		cv2.line(image, bottomRight, bottomLeft,(255,69,0), 2)
		cv2.line(image, bottomLeft, topLeft, (255,69,0), 2)

		# draw the ArUco marker ID on the image
		cv2.putText(image, str(markerID),
			(topLeft[0], topLeft[1] - 15), cv2.FONT_HERSHEY_SIMPLEX,
			0.5, (255,69,0), 2)
		print("[INFO] ArUco marker ID: {}".format(markerID))
		# show the output image
		cv2.imshow("Image", image)
		cv2.waitKey(0)

