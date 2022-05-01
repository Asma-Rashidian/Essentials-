import argparse
from ast import arg
import cv2 
import matplotlib.pyplot as plt 


ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--input" , type= str ,required=True , help="Image path")
"""
    You’ll typically want to leave this value in the range of 2-5.
    If you set the value too large, then effectively, what you’re
    doing is maximizing local contrast, which will, in turn, maximize
    noise (which is the opposite of what you want).
    Instead, try to keep this value as low as possible.
"""
ap.add_argument("-c" , "--clip" , type=float , default=2.0 , help= "Theashold for contrast limiting")
"""
    The tile grid size for CLAHE. Conceptually, what we are doing
    here is dividing our input image into tile x tile cells and
    then applying histogram equalization to each cell (with the
    additional bells and whistles that CLAHE provides).
"""
ap.add_argument("-t" , "--tile" , type= int  , default= 8 , help="Tile grid size -- divides image into tile x times cells ")
args = vars(ap.parse_args())

# Load image
image = cv2.imread(args["input"])
# turn image to grya scale 
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)
cv2.imshow(" Gray Scale " , gray)
cv2.waitKey(0)


# apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
print("[INFO] applying CLAHE ...")
clahe = cv2.createCLAHE(clipLimit=args["clip"] , tileGridSize=(args["tile"] , args["tile"]))
equalized = clahe.apply(gray)
cv2.imshow(" Equalized " , equalized)
cv2.waitKey(0)

# Histogram plot of grayscale image 
histogram_original = cv2.calcHist([gray] , [0] , None , [256], [0 , 255])
histogram_equalized = cv2.calcHist([equalized]  ,[0] , None , [256] ,[0,255])
plt.plot(histogram_original)
plt.plot(histogram_equalized)
plt.show()




