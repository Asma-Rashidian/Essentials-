import argparse
import cv2
import imutils 
import numpy as np 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input" , required= True , help= "Imaage path")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])


def rotate_bound (image , angle):

    # grab the dimensions of the image and then determine the
    # center
    (h, w )= image.shape[:2]
    (cX , cY) = (w//2 , h//2)

    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    # The matrix is in the folder 

    M = cv2.getRotationMatrix2D((cX , cY) , -angle , 1.0)
    cos = np.abs(M[0,0])
    sin = np.abs(M[0,1])

    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))

    # adjust the rotation matrix to take into account translation
    M[0,2] += (nW / 2) - cX
    M[1,2] += (nH / 2) - cY

    # perform the actual rotation and return the image
    return cv2.warpAffine(image , M ,(nW , nH))



# # loop over the rotation angles
# for angle in np.arange(0, 360, 15):
# 	rotated = imutils.rotate(image, angle)
# 	cv2.imshow("Rotated (Problematic)", rotated)
# 	cv2.waitKey(0)

# # loop over the rotation angles again, this time ensuring
# # no part of the image is cut off
# for angle in np.arange(0, 360, 15):
# 	rotated = rotate_bound(image, angle)
# 	cv2.imshow("Rotated (Correct)", rotated)
# 	cv2.waitKey(0)


gray = cv2.cvtColor(image  , cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray , (3,3), 0)
edge = cv2.Canny(blurred ,20 , 100)
cv2.imshow("edges" , edge)
cv2.waitKey(0)

cnts = cv2.findContours(edge.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# ensure at least one contour was found
if len(cnts) > 0:
	# grab the largest contour, then draw a mask for the pill
	c = max(cnts, key=cv2.contourArea)
	mask = np.zeros(gray.shape, dtype="uint8")
	cv2.drawContours(mask, [c], -1, 255, -1)
	# compute its bounding box of pill, then extract the ROI,
	# and apply the mask
	(x, y, w, h) = cv2.boundingRect(c)
	imageROI = image[y:y + h, x:x + w ]
	maskROI = mask[y:y + h, x:x + w]
	imageROI = cv2.bitwise_and(imageROI, imageROI,
		mask=maskROI)

cv2.imshow("Image ROI" , imageROI)
cv2.waitKey(0)