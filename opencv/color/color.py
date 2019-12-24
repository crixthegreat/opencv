#python code env
#-*-coding:utf-8-*-
#Code by Crix @ crixthegreat@gmail.com
#https://github.com/crixthegreat/
#codetime: 2019/12/4 22:09:49

import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

lower_green = np.array([35, 143, 46])  # 绿色范围低阈值
upper_green = np.array([77, 255, 200])  # 绿色范围高阈值

lower_red = np.array([0, 150, 46])  # 红色范围低阈值
upper_red = np.array([10, 255, 250])  # 红色范围高阈值

lower_yellow = np.array([26, 33, 46]) # threshold value for yellow
upper_yellow = np.array([36,255,255])

lower_black = np.array([0, 0, 0]) # threshold value for yellow
upper_black = np.array([180,255,30])

# cap = cv2.VideoCapture('1.mp4')  # 打开视频文件
cap = cv2.VideoCapture(0)#打开USB摄像头

# define the codec and create videowriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_out = cv2.VideoWriter('test.avi', fourcc, 20.0, (640,360))

while (True):
    ret, frame = cap.read()  # 读取一帧
    frame = frame[60:420, 0:640]
   
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #mask_green = cv2.inRange(hsv_img, lower_green, upper_green)  # 根据颜色范围删选
    #mask_red = cv2.inRange(hsv_img, lower_red, upper_red)       # 根据颜色范围删选
    #mask_yellow = cv2.inRange(hsv_img, lower_yellow, upper_yellow)       # 根据颜色范围删选
    mask_black = cv2.inRange(hsv_img, lower_black, upper_black)       # 根据颜色范围删选

    #mask_green = cv2.medianBlur(mask_green, 7)  # 中值滤波
    #mask_red = cv2.medianBlur(mask_red, 7)  # 中值滤波
    #mask_yellow = cv2.medianBlur(mask_yellow, 7)  # 中值滤波
    mask_black = cv2.medianBlur(mask_black, 7)  # 中值滤波
    
    #mask = cv2.bitwise_or(mask_green, mask_red, mask_yellow)
    
    contours, hierarchy = cv2.findContours(mask_black, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #contours, hierarchy = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #contours2, hierarchy2 = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #contours3, hierarchy3 = cv2.findContours(mask_yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        if w < 40 or h < 40:
            continue
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "drive plate gasket", (x, y - 5), font, 0.7, (0, 255, 0), 2)

    '''
    for cnt2 in contours2:
        (x2, y2, w2, h2) = cv2.boundingRect(cnt2)
        if w2< 40 or h2 < 40:
            continue
        cv2.rectangle(frame, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 255), 2)
        cv2.putText(frame, "Red", (x2, y2 - 5), font, 0.7, (0, 0, 255), 2)
        
    for cnt3 in contours3:
        (x3, y3, w3, h3) = cv2.boundingRect(cnt3)
        if w3 < 40 or h3 < 40:
            continue
        cv2.rectangle(frame, (x3, y3), (x3 + w3, y3 + h3), (0, 255, 255), 2)
        cv2.putText(frame, "yellow", (x3, y3 - 5), font, 0.7, (0, 255, 255), 2)
    '''

    #video_out.write(frame)
    cv2.imshow("dection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
video_out.release()
cv2.destroyAllWindows()
