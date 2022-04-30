"""
    Histogram equalization is a basic image processing technique
    that adjusts the global contrast of an image by updating
    the image histogram’s pixel intensity distribution.

    Essentially, histogram equalization works by:

        1. Computing a histogram of image pixel intensities
        2. Evenly spreading out and distributing the most frequent pixel values (i.e., the ones with the largest counts in the histogram)
        3. Giving a linear trend to the cumulative distribution function (CDF)

    Notice how our histogram has numerous peaks,
    indicating there are a good number of pixels binned to those respective buckets.
    With histogram equalization,
    our goal is to spread these pixels to buckets that don’t have as many pixels binned to them.
"""

import argparse
import cv2 
import matplotlib.pyplot as plt 


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input" , required=True , help="Image path")
args = vars(ap.parse_args())

# load the input image from disk and convert it to grayscale
print("[INFO] loading input image...")
image = cv2.imread(args["input"])
gray = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

# Draw histogram plot
histogram = cv2.calcHist([gray] , [0] , None , [256] , [0,255] )
plt.plot(histogram , color = 'k')
plt.show()

# apply histogram equalization
print("[INFO] performing histogram equalization...")
equalized = cv2.equalizeHist(gray)

# Show equalized image
cv2.imshow("Input" , gray)
cv2.imshow(" Histogram Equalization ", equalized)
cv2.waitKey(0)

# Equaliziation Histogram diagram
histogram_equalization = cv2.calcHist([equalized] , [0] ,None ,[256] , [0,255] )
plt.plot(histogram_equalization , color = 'k')
plt.show()

# show bot histograms in one 
plt.plot(histogram)
plt.plot(histogram_equalization)
plt.legend("Original_hist" , "Equalized_Hist")
plt.show()