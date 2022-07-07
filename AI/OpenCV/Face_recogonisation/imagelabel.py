import cv2
from skimage.metrics import structural_similarity as compare_ssim
import numpy as np
import matplotlib as plt

# Let's load a simple image with 3 black squares
image1 = cv2.imread('road.jpg')
image2 = cv2.imread('road - Copy.jpg')
cv2.waitKey(0)

# Grayscale
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
edged2 = cv2.Canny(gray2, 30, 200)
cv2.waitKey(0)

# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged,
	cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours1,hierarchy1 =cv2.findContours(edged2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.imshow('Canny Edges After Contouring2',edged2)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image1, contours, -1, (0, 255, 0), 3)



cv2.imshow('Contours', image1)
cv2.waitKey(0)
a= edged
b= edged2

if a==b:
	cv2.putText(edged, text='Pass', org=(150, 200), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(255, 255, 0), thickness=3)
	cv2.imshow('Lable', edged)
else:
	cv2.putText(edged2, text='Fail', org=(150, 200), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(255, 255, 0), thickness=3)
	cv2.imshow('Lable2', edged2)

cv2.waitKey(0)
cv2.destroyAllWindows()



