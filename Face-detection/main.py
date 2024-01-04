import cv2
import numpy as np
video=cv2.VideoCapture(0)
har=cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
while True:
    success, frame=video.read()
    if success:
        '''Convert the BGR (Blue, Green, Red) image to grayscale. Haar Cascade works on grayscale images.'''
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        '''Use the detectMultiScale method to find faces in the grayscale frame. Adjust parameters like 
        scaleFactor=1.1 and minNeighbors=4 for better detection.'''
        faces=har.detectMultiScale(gray,1.1,4)
        '''For each detected face, draw a blue rectangle around it on the original colored frame.'''
        for x,y,w,h in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)

        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()
