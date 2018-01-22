# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 20:17:30 2017

@author: satyanarayan pande
"""
#import numpy as np
#from PIL import ImageGrab
import cv2
from process_img import process_img


def main():
    path = 'D:\\Study\\SEM VIII\\FYP\\Density Based Traffic Control using Image Processing\\output_images\\'
    screen = cv2.imread('sample2_img.jpg')
    new_screen = process_img(screen)
    
    cv2.imshow('Canny Edge Detection', new_screen)
    cv2.imwrite(path + 'op6.jpg', new_screen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()