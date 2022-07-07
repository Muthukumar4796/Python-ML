import cv2
image=cv2.imread('love.jpg')
cv2.imshow('lov',image)
cv2.waitKey(0)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale image',gray)

edged=cv2.Canny(gray,200,300)
cv2.waitKey(0)

contours,hierarchy=cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring',edged)
cv2.waitKey(0)

print('Number of contour found='+ str(len(contours)))
cv2.drawContours(image,contours,-1,(0,255,0),1)

cv2.imshow('Contours',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
