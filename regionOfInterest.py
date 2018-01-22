# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 21:07:58 2017

@author: satyanarayan pande
"""
import numpy as np
import cv2

def roi(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    
    return masked

