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
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_out = cv2.VideoWriter('test.avi', fourcc, 20.0, (640,480))

drawing = False # True if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


def nothing(x):
    pass

cv2.namedWindow('test')


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

while(True):
    # now read every frame from the camera
    ret, frame = cap.read()
    # get gray output
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey), (ex+ew,ey+eh), (0,255,0),2)


    # print text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'face recoggnition test', (10,400), font, 1, (255,255,255), 2, cv2.LINE_AA)

    video_out.write(frame)
    cv2.imshow('test', frame)
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:
        break

cap.release()
video_out.release()
cv2.destroyAllWindows()
