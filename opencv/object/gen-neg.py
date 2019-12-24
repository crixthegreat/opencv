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

drawing = False # True if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1


cv2.namedWindow('test1')

frame_num = 0
pic_num = 1
while(True):
    frame_num += 1
    # now read every frame from the camera
    ret, frame = cap.read()
    # get gray output
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    resized_image = cv2.resize(gray,(100,100))
    if frame_num % 10 == 0:
        cv2.imwrite(str(pic_num) + '.jpg', resized_image)
        pic_num += 1

    cv2.imshow('test1', frame)
    k = cv2.waitKey(1) & 0xFF 
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
