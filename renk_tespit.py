#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)   # 1'e basınca y eksenine göre yansıma alır
    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 180, 80])
    upper_red = np.array([10,255,255])

    lower_green = np.array([40, 70, 80])
    upper_green = np.array([90,255,255])

    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
       
    maske = cv2.inRange(hsv_frame, lower_red, upper_red)
    maske1 = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    maske2= cv2.inRange(hsv_frame, lower_green, upper_green)

    Blur= cv2.GaussianBlur ( frame , ( 7, 7 ) , cv2.BORDER_DEFAULT )
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    frame = cv2.filter2D(frame, -1, kernel)

    maske = cv2.medianBlur(maske,7)
    maske1 = cv2.medianBlur(maske1,7)
    maske2 = cv2.medianBlur(maske2,7)

    red = cv2.bitwise_and(frame,frame, mask = maske)
    blue = cv2.bitwise_and(frame,frame, mask = maske1)
    green = cv2.bitwise_and(frame,frame, mask = maske2)
    
    _ ,contours1, _ = cv2.findContours(maske, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    _ ,contours2, _ = cv2.findContours(maske1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    _ ,contours3, _ = cv2.findContours(maske2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    cv2.drawContours(frame, contours1, -1, (255,0,0),3)    #red
    cv2.drawContours(frame, contours2, -1, (0,0,255),3)   #blue
    cv2.drawContours(frame, contours3, -1, (0,0,255),3)   #green
    cv2.drawContours(Blur, contours1, -1, (255,0,0),3) 
    cv2.drawContours(Blur, contours2, -1, (255,0,0),3) 
    cv2.drawContours(Blur, contours3, -1, (255,0,0),3) 


    for cnt in contours1:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt , 0.01 * peri, True)
        if area > 5000: 
            cv2.drawContours(frame, [cnt], -1, (255,0,0),-1)
            cv2.drawContours(Blur, [cnt], -1, (255,0,0),-1)
            if len(approx) == 15:
                sekil_adi = "Daire"
                
                #x,y = approx[0][0]  
                M = cv2.moments(cnt) 
                cx= int(M['m10']/M['m00'])  
                cy= int(M['m01']/M['m00'])
                cv2.putText(Blur,"Kirmizi"+ sekil_adi, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2)
    
    for cnt in contours2:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt , 0.01 * peri, True)
        if area > 5000: 
            cv2.drawContours(frame, [cnt], -1, (255,0,0),-1)
            cv2.drawContours(Blur, [cnt], -1, (255,0,0),-1)
            if len(approx) == 15:
                sekil_adi = "Daire"
                
                #x,y = approx[0][0]  
                M = cv2.moments(cnt) 
                cx= int(M['m10']/M['m00'])  
                cy= int(M['m01']/M['m00'])
                cv2.putText(frame, "Mavi"+ sekil_adi, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2)

    for cnt in contours3:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt , 0.01 * peri, True)
        if area > 5000: 
            cv2.drawContours(frame, [cnt], -1, (255,0,0),-1)
            cv2.drawContours(Blur, [cnt], -1, (255,0,0),-1)

            if len(approx) == 15:
                sekil_adi = "Daire"
               
                #x,y = approx[0][0] 
                M = cv2.moments(cnt)  
                cx= int(M['m10']/M['m00'])  
                cy= int(M['m01']/M['m00'])
                cv2.putText(frame, "Yesil"+ sekil_adi, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2)


    cv2.imshow("Webcam",frame)
    cv2.imshow("Red Mask", red)
    cv2.imshow("Blur",Blur)
    cv2.imshow("Blue Mask", blue)
    cv2.imshow("Green Mask", green)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
