import cv2

har=cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')


video=cv2.VideoCapture('demo.mp4')

while True:
    ret,frame=video.read()

    if ret:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        plate=har.detectMultiScale(frame,1.1,10)

        for x,y,w,h in plate:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            cv2.putText(frame,"No Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.imshow("Output",frame)

        if cv2.waitKey(1) & 0xff==ord('q'):
           break
    else:
        break
cv2.destroyAllWindows()
video.release()


