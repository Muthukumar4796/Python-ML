import cv2
import numpy as np
import time

# loading_classifier
human_classifier=cv2.CascadeClassifier('haarcascades/haarcascade_fullbody.xml')

# video_capture_from_file
cap=cv2.VideoCapture('data/walking.avi')

while cap.isOpened():

    # reading_from_file
    ret,frame=cap.read()
    if ret is True:
        # slowing_down_video
        # time.sleep(0.02)

        # grayscaling_frame
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        # detecting_humans
        humans=human_classifier.detectMultiScale(gray,1.5,4)

        # drawing_rectangles_on_cars
        for (x,y,w,h) in humans:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.imshow('pedestrians_detected',frame)
        
        # closing_window_on_ENTER_pressed
        if cv2.waitKey(1)==13:
            break
    

cap.release()
cv2.destroyAllWindows()