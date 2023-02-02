#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)   # 1'e basınca y eksenine göre yansıma alır
    edge = cv2.Canny(frame,100,200,5)

    _, contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt , 0.01 * peri, True)
        if area > 5000: 
                
            if(len(approx) == 4 ):
                sekil_adi = "Halka"
                cv2.drawContours(frame, [cnt], -1, (255,0,0),-1)
                M = cv2.moments(cnt) 
                cx= int(M['m10']/M['m00'])  
                cy= int(M['m01']/M['m00'])
                cv2.putText(frame+ sekil_adi, (cx,cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2)
    
    cv2.imshow("Webcam",frame)
     
    cv2.imshow("Kenar",edge)

    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()
