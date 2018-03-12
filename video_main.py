# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""

#import numpy as np
import cv2
   
cap = cv2.VideoCapture("Bang_traffic.mp4")

if(cap.isOpened() == False):
    print("Error opening")
while(cap.isOpened()):    
    fgbg = cv2.BackgroundSubtractorMOG2()

    while(True):
        ret, frame = cap.read()
        
        if ret == True:
            
            fgmask = fgbg.apply(frame)
            cv2.imshow('frame', fgmask)
            
            if cv2.waitKey(25) & 0xff == ord('q'):
                break
            
        else:
            break
    
cap.release()
cv2.destroyAllWindows() 