#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/8/20 13:46:11

import numpy as np
import cv2

#img = cv2.imread('vim-key.png')
#cv2.imshow('image', img)
#k = cv2.waitKey(0)
#cv2.destroyAllWindows()

# when the arguement of VideoCapture is file name
# the video file can be played from
cap = cv2.VideoCapture(0)


# define the codec and create videowriter object
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#video_out = cv2.VideoWriter('test.avi', fourcc, 20.0, (640,480))




cv2.namedWindow('test1')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#this is . 
my_cascade = cv2.CascadeClassifier('my_cascade.xml')

while(True):
    # now read every frame from the camera
    ret, frame = cap.read()
    # get gray output
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    my_object = my_cascade.detectMultiScale(gray, 50, 50)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)

    for (x,y,w,h) in my_object:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2)

    # draw a blue line
    #frame = cv2.line(frame, (0,0), (511,311), (255,0,0), 5)
    # draw a rectangle
    #frame = cv2.rectangle(frame, (340,0), (400,128), (0,255,0), 3)
    # draw a circle
    #frame = cv2.circle(frame, (400,60), 60, (0,0,255), -1)
    # draw a ploygon
    #pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32)
    #pts = pts.reshape((-1,1,2))
    #frame = cv2.polylines(frame, [pts], True, (0,255,255))
    # print text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'object recognition test', (10,400), font, 1, (255,255,255), 2, cv2.LINE_AA)

    # set all pixel 's red to 0
    #frame[:, :, 2] = 0
    #video_out.write(frame)
    cv2.imshow('test1', frame)
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:
        break

cap.release()
#video_out.release()
cv2.destroyAllWindows()
