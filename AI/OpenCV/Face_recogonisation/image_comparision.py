import pandas as pd
from skimage.metrics import structural_similarity as compare_ssim
import imutils
import cv2


imageA = cv2.imread('road.jpg')
imageB = cv2.imread('road - Copy.jpg')
cv2.waitKey(0)

# Grayscale
grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

# compute the Structural Similarity Index (SSIM) between the two
# images, ensuring that the difference image is returned
(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff * 255).astype("uint8")

print("SSIM: {}".format(score))
if score==1:
    cv2.putText(grayB, text='Pass', org=(150, 200), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(255, 255, 0),
                thickness=3)
    cv2.imshow('Lable', grayB)
else:
    cv2.putText(grayB, text='Fail', org=(150, 200), fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=3, color=(255, 255, 0),
                thickness=3)
    cv2.imshow('Lable',grayB)
# threshold the difference image, followed by finding contours to
# obtain the regions of the two input images that differ
# thresh = cv2.threshold(diff, 0, 255,
# 	cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
# 	cv2.CHAIN_APPROX_SIMPLE)
# cnts = imutils.grab_contours(cnts)


# show the output images
cv2.imshow("Original", imageA)
cv2.imshow("Modified", imageB)
# cv2.imshow("Diff", diff)
# cv2.imshow("Thresh", thresh)
cv2.waitKey(0)


