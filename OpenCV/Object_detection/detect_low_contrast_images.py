"""
    If a low contrast image is detected, you can throw the image out or alert the user to capture an image in better lighting conditions.

    >> pip3 install opencv-contrib-python
    >> pip3 install scikit-image
"""

from numpy import imag
from skimage.exposure import is_low_contrast
from imutils.paths import list_images
import argparse 
import cv2 
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--input" , required=True , help="path to input directory of images")
#Essentially, what this means is that if less than 35% of the range of brightness occupies the full range of the data type, then the image is considered low contrast.
ap.add_argument("-t" , "--tresh" , type=float , default=0.35 , help="threshold for low contrast")
args = vars(ap.parse_args())

# grab the paths to the input images
imagePaths = sorted(list(list_images(args["input"])))

# loop over images 
for (i , imagePath ) in enumerate(imagePaths):
    
    # load the input image from disk, resize it, and convert it to
	# grayscale
    print("[INFO] proccssing image {} / {} ..." .format(i+1 , len(imagePaths)))

    image = cv2.imread(imagePath)
    image = imutils.resize(image , width=450)
    gray = cv2.cvtColor(image , cv2.COLOR_RGB2GRAY)

    # blur the image slightly and perform edge detection
    blurred  = cv2.GaussianBlur(gray , (5,5) , 0)
    edge = cv2.Canny(blurred , 30 , 150)

   


    # check to see if the image is low contrast
    if is_low_contrast (gray , fraction_threshold=args["tresh"]) :
        # update the text and color 
        text = " low Contrast : Yes"
        color = (0,0,255) 
    
    # otherwise, the image is *not* low contrast, so we can continue
	# processing it
    else:
        # find contours in the edge map and find the largest one,
		# initialize the text and color to indicate that the input image
        # is *not* low contrast
        text = " Low Contrast : No" 
        color = (0,255,0)
        
        cnts = cv2.findContours(edge.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts , key=cv2.contourArea)

        # draw the largest contour on the image 
        cv2.drawContours(image , [c] , -1 , (0,255,0) , 2)

    # draw the text on the output image
    cv2.putText(image , text , (5,25) , cv2.FONT_HERSHEY_SIMPLEX , 0.8 , color , 2)


    # show the output image and edge map
    cv2.imshow("Image", image)
    cv2.imshow("Edge", edge)
    cv2.waitKey(0)