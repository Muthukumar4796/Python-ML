import cv2
import numpy as np


# load image as grayscale
img = cv2.imread('love.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# threshold input image using otsu thresholding as mask and refine with morphology
threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
analysis= cv2.connectedComponentsWithStats(threshold,4,cv2.CV_32F)
kernel = np.ones((9,9), np.uint8)
mask = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
mask = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)

# put mask into alpha channel of result
result = img.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask

# save resulting masked image
cv2.imwrite('Love_cropped.png', result)