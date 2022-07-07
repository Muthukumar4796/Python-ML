import cv2
import matplotlib.pyplot as plt
img= cv2.imread('Tesla.jpg')
edges=cv2.Canny(img,200,300,10,L2gradient=True)
plt.figure()
plt.title('Tesla SUV')
plt.imshow(edges,cmap='gray')
plt.show()
