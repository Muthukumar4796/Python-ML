import cv2
import numpy as np

image = cv2.imread('love.jpg', 1)
Tesla = cv2.imread('Tesla.jpg', 1)

image2 = image.copy()
image3 = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
#cv2.imshow('thresh', thresh)

_, cnts, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in cnts:

    #---- making sure to avoid small unwanted contours ---
    if cv2.contourArea(c) > 150:

        #--- selecting contours having 5 sides ---
        if len(cv2.approxPolyDP(c, 0.04 * cv2.arcLength(c, True), True)) == 5:


            cv2.drawContours(image2, [c], -1, (0, 255, 0), 2)

            #--- finding bounding box dimensions of the contour ---
            x, y, w, h = cv2.boundingRect(c)
            print(x, y, w, h)

            #--- overlaying the monkey in place of pentagons using the bounding box dimensions---
            image3[y:y+h, x:x+w] = cv2.resize(Tesla, (np.abs(x - (x+w)), np.abs(y - (y+h))))


cv2.imshow('image2', image2)
cv2.imshow('image3', image3)

cv2.waitKey(0)
cv2.destroyAllWindows()