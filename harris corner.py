# Python programe to illustrate
# corner detection with
# Harris Corner Detection Method

# organizing imports
import cv2
import numpy as np

# path to input image specified and
# image is loaded with imread command
image = cv2.imread(r'C:\Users\Aryan\Desktop\chessboard.jpg')
image1= cv2.resize(image, (300,300))

# convert the input image into
# grayscale color space
operatedImage = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# modify the data type
# setting to 32-bit floating point
operatedImage = np.float32(operatedImage)

# apply the cv2.cornerHarris method
# to detect the corners with appropriate
# values as input parameters
dest = cv2.cornerHarris(operatedImage, 2, 5, 0.07)

# Results are marked through the dilated corners
dest = cv2.dilate(dest, None)

# Reverting back to the original image,
# with optimal threshold value
image1[dest > 0.01 * dest.max()]=[0, 0, 255]

# the window showing output image with corners
cv2.imshow('Image with Borders', image1)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
