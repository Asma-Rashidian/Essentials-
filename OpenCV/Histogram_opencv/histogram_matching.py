"""
    Histogram matching with OpenCV, scikit-image, and Python

    we have an input image and a reference image. Our goal is to:

        1. Compute histograms for each image
        2. Take the reference image histogram
        3. Update the pixel intensity values in the input image using the reference histogram, such that they match
        
        *** Take the input image and match it to the reference image,
        thereby transferring the color/intensity distribution from the
        reference image into the source image***

        image 5, 6 are considered for this code 
"""

from typing import Tuple
from skimage import exposure 
import matplotlib.pyplot as plt 
import argparse 
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-s" ,"--source" , required=True , help="Source image path")
ap.add_argument("-r" , "--reference" , required=True , help= "Reference path")
args = vars(ap.parse_args())

# load the source and reference images
source = cv2.imread(args["source"])
reference = cv2.imread(args["reference"])

# determine if we are performing multichannel histogram matching
# and then perform histogram matching itself
print("[INFO] performing histogram matching...")
multi = True if source.shape[-1] > 1 else False
matched = exposure.match_histograms(source , reference , multichannel=multi )

# show the output images
cv2.imshow("Source", source)
cv2.imshow("Reference", reference)
cv2.imshow("Matched", matched)
cv2.waitKey(0)


# *** Plots ***
# construct a figure to display the histogram plots for each channel
# before and after histogram matching was applied
(fig, axs) =  plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
# loop over our source image, reference image, and output matched
# image
for (i, image) in enumerate((source, reference, matched)):
	# convert the image from BGR to RGB channel ordering
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	# loop over the names of the channels in RGB order
	for (j, color) in enumerate(("red", "green", "blue")):
		# compute a histogram for the current channel and plot it
		(hist, bins) = exposure.histogram(image[..., j],
			source_range="dtype")
		axs[j, i].plot(bins, hist / hist.max())
		# compute the cumulative distribution function for the
		# current channel and plot it
		(cdf, bins) = exposure.cumulative_distribution(image[..., j])
		axs[j, i].plot(bins, cdf)
		# set the y-axis label of the current plot to be the name
		# of the current color channel
		axs[j, 0].set_ylabel(color)


# set the axes titles
axs[0, 0].set_title("Source")
axs[0, 1].set_title("Reference")
axs[0, 2].set_title("Matched")
# display the output plots
plt.tight_layout()
plt.show()