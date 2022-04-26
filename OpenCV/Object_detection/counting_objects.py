"""
    1. Grayscale 
    2. Edge detection 
    3. Canny Algorithm 
    4. Thresholding
    5. Detect and draw Contour
"""



import cv2
import imutils 
import argparse 


ap = argparse.ArgumentParser()
ap.add_argument("-i" , "--input" , required=True , help = "Image path")
ap.add_argument("-o" , "--output" , required=True , help= " Final Image path")
args = vars(ap.parse_args())

image = cv2.imread(args["input"])
cv2.imshow(" Original Image" , image)
cv2.waitKey(0)

"""
    1. Grayscale 
    convert the image to grayscale
"""
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow(" Grayscale Image" , gray)
cv2.waitKey(0)


"""
    4. Thresholding 
    Thresholding can help us to remove lighter or darker regions and contours of images.
"""
# threshold the image by setting all pixel values less than 225
# to 255 (white; foreground) and all pixel values >= 225 to 255
# (black; background), thereby segmenting the image
#  Black <232 , 232<= White <=255
thresh = cv2.threshold(gray , 232 , 255 , cv2.THRESH_BINARY_INV)[1]
cv2.imshow(" Threshold" , thresh)
cv2.waitKey(0)


"""
    2. Edge detection
    3. Canny Algorithm 
    applying edge detection we can find the outlines of objects in images
"""
# minVal : A minimum threshold, in our case 30 .
# maxVal : The maximum threshold which is 150 in our example.
# aperture_size : The Sobel kernel size. By default this value is 3
edged = cv2.Canny(thresh , 30 , 150 , apertureSize=3 )
cv2.imshow(" Edged " , edged)
cv2.waitKey(0)

"""
    5. Detect and Draw Contours 
    find contours (i.e., outlines) of the foreground objects in the
    thresholded image
"""
cnts = cv2.findContours(thresh.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
output = image.copy()

for c in cnts :
    cv2.drawContours(output , [c] , -1 , (240,0,159) , 3)
    cv2.imshow("Contours" , output)
    cv2.waitKey(0)

text = " {} Objects are founded".format(len(cnts))
cv2.putText(output , text , (5,10) , cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,255) , 2)
cv2.imwrite(args["output"] , output)
