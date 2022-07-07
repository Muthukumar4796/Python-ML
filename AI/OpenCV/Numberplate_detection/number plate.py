import cv2
import imutils
import numpy as np
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img = cv2.imread('hyundai-verna-same-number-plate.jpg',cv2.IMREAD_COLOR)
cv2.imshow("Original Image",img)
img = imutils.resize(img, width=500,height=500)
cv2.imshow("Resized Image",img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert to grey scale
cv2.imshow("Grayscale Image",gray)
gray = cv2.bilateralFilter(gray, 11, 17, 17) #Blur to reduce noise
cv2.imshow("Noise Image",gray)
edged = cv2.Canny(gray, 30, 200) #Perform Edge detection
cv2.imshow("Edge Image",edged)
cnts,new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(cnts)
img1=img.copy()
cv2.drawContours(img1,cnts,-1,(0,255,0),3)
cv2.imshow("img1",img1)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:30]
print(cnts)
screenCnt = None #will store the number plate contour
img2 = img.copy()
cv2.drawContours(img2,cnts,-1,(0,255,0),3) 
cv2.imshow("img2",img2) #top 30 contours

count=0
idx=7

# loop over contours
for c in cnts:
  # approximate the contour
        peri = cv2.arcLength(c, True)
        print(peri)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)
        print(approx)
        if len(approx) == 4: #chooses contours with 4 corners
                screenCnt = approx
                x,y,w,h = cv2.boundingRect(c) #finds co-ordinates of the plate
                new_img=img[y:y+h,x:x+w]
                cv2.imwrite('./'+str(idx)+'.png',new_img) #stores the new image
                idx+=1
                break
            #draws the selected contour on original image        
cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Final image with plate detected",img)

Cropped_loc='./7.png' #the filename of cropped image
cv2.imshow("cropped",cv2.imread(Cropped_loc))
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe' #exe file for using ocr

text=pytesseract.image_to_string(Cropped_loc,lang='eng') #converts image characters to string
print("Number is:" ,text)
cv2.waitKey(0)
cv2.destroyAllWindows() 
