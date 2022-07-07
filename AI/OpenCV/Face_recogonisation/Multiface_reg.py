import cv2
import face_recognition as fc

image=fc.load_image_file('multi_face.jpg')
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

face_locations = fc.face_locations(image)
print(face_locations)

for i in range(len(face_locations)):
    image=cv2.rectangle(image,(face_locations[i][3],face_locations[i][0]),(face_locations[i][1],face_locations[i][2]),(0,255,0),2)


cv2.imshow('multi_face',image)
cv2.waitKey(0)