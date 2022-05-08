"""
    Our first script will cover basics image processing operations using images from movie .
    1. Access pixels
    2. Array Slicing and Cropping 
    3. Resizing images 
    4. Rotaing an image 
    5. Smoothing an image 
    6. Drawing on image 

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

# Pixels in gray scale has  a value representing in grayscale mood (0 , 255)
# Pixels in RGB color space has value of ((0,255) , (0,255) ,(0,255))
# OpenCv standard is BGR not RGB.
print(image)
(B ,G , R) = image[0,0]
print("R :{} , G :{} , B :{}".format( R , G , B))


"""
    2. Arraying slicing and Cropping 

    Extractiong " Region of Interst" (ROIs) is an important skil for imagr processing .
    Example: you’re working on recognizing faces in a movie. First, you’d run a face detection algorithm to find the coordinates of faces in all the frames you’re working with.
    Then you’d want to extract the face ROIs and either save them or process them.
    Locating all frames containing Dr. Ian Malcolm in Jurassic Park would be a great face recognition mini-project to work on.
"""
#  image[startY : EndY , startX : EndX]
roi = image[4:41 , 117:163]
cv2.imshow("ROI" , roi)
cv2.waitKey(0)



"""
    3. Resizing an image 
"""
# Resizing images 
# resize the image to 300x300px, ignoring aspect ratio
resized = cv2.resize(image , (300 , 300))
cv2.imshow("Fixed Resizing " , resized)
cv2.waitKey(0)

"""
    Let’s calculate the aspect ratio of the original image
    and use it to resize an image so that it doesn’t appear squished and distorted:
"""
# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 /w
dim = (300, int(h *r))      # the logic behind is h*300/w 
resized1 = cv2.resize(image , dim )
cv2.imshow("Aspect Ratio Resize" , resized)
cv2.waitKey(0)

"""
    Computing the aspect ratio each time we want to rsize an image is abit tedious , 
    so you can wrap the code in afunction witjin "imutil"
"""
# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized2 = imutils.resize(image , width=300)
cv2.imshow("Imutil Resize " , resized2)
cv2.waitKey(0)



"""
    4. Rotate an image 
"""
# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w//2 , h//2)
matris = cv2.getRotationMatrix2D(center , -45 , 1.0)
rotated = cv2.warpAffine(image ,matris , (w,h))
cv2.imshow(" OPenCv Rotation" , rotated)
cv2.waitKey(0)

# Now let’s perform the same operation in just a single line of code
rotated1 = imutils.rotate(image , -45)
cv2.imshow("Imutils Rotation", rotated1)
cv2.waitKey(0)

# Notice in this rotaion the image is clipped so we can use this method 
rotated2 = imutils.rotate_bound(image , 45 )   #angle must consider posetive
cv2.imshow("Imutils Bound Rotation", rotated2)
cv2.waitKey(0)



"""
    5. Smooting an image 
    In many image processing pipelines, we must blur an image to reduce high-frequency noise,
    making it easier for our algorithms to detect and understand the actual contents of the image 
    rather than just noise that will “confuse” our algorithms. 
    Blurring an image is very easy in OpenCV and there are a number of ways to accomplish it.

    We use GaussianBlur function
"""
blurred = cv2.GaussianBlur(image , (11,11) , 0) #Gaussian Blur with an 11 x 11 kernel 
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)


"""
    6. Drawing on an image .
    In this section, we’re going to draw a rectangle, circle, and line on an input image.
    We’ll also overlay text on an image as well.
    
    **Before we move on with drawing on an image with OpenCV, take note that drawing operations on images are performed in-place.
    Therefore at the beginning of each code block, we make a copy of the original image storing the copy as output .
    We then proceed to draw on the image called output in-place so we do not destroy our original image.
"""
# draw a 2px thick red rectangle surrounding the face
output = image.copy()
# Our starting pixel coordinate which is the top-left. In our case, the top-left is (31 ,211)
# The ending pixel — bottom-right. The bottom-right pixel is located at (171 ,29)
cv2.rectangle(output , (31 , 211) , (171 , 29) , (0,0,255), 2)
cv2.imshow("Rectangle", output)
cv2.waitKey(0)

#place a solid blue circle
# draw a blue 20px (filled in) circle on the image centered at
# x=29,y=31 the circle center
output = image.copy()
cv2.circle(output , (29, 31) ,20 , (255,0,0) , -1 )   # 20 is the radius of circle
#thickness : The line thickness. Since I supplied a negative value (-1 ), the circle is solid/filled in.
cv2.imshow("Circle", output)
cv2.waitKey(0)


# Draw Red Line 
# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv2.line(output , (60,20) , (400 , 200) , (0,0,255) , 5)
cv2.imshow("Line", output)
cv2.waitKey(0)

# Draw green text on the image
output = image.copy()
# pt : The starting point for the text  and scale : Font size multiplier.
cv2.putText( output , "Asma Rashidian" , (10 ,25) , cv2.FONT_HERSHEY_SIMPLEX , 0.7 , (0,0,255) , 2 )
cv2.imshow("Text", output)
cv2.waitKey(0)

