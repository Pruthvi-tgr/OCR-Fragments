# -*- coding: utf-8 -*-
"""
Created on Thu feb 08:42:40 2021

@author: Pruthvi tgr
"""

import numpy as np
import cv2 as cv
import imutils
import os

TEST_DIR     = "IMG_ALL\\"
TEST_FILE    = "03.jpg"

file_name = TEST_DIR+TEST_FILE;

def image_to_angle(file_name):
   
    input_image = cv.imread(file_name)  
    #cv.imshow('Test Character',input_image)
    #cv.waitKey()
    roi = input_image
   
    gray = cv.cvtColor(input_image,cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray,50,150,apertureSize = 3)
   
    lines = cv.HoughLines(edges,1,np.pi/180,3)
    #print(lines)
    for rho,theta in lines[0]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 2000*(-b))
        y1 = int(y0 + 2000*(a))
        x2 = int(x0 - 2000*(-b))
        y2 = int(y0 - 2000*(a))
        degree_Values = np.degrees(theta)
        #print('Theta in Deg:', degree_Values)
       
    cv.line(roi,(x1,y1),(x2,y2),(0,0,255),2)
    cv.imshow('ROI with line Image',roi)
    cv.waitKey()
    return degree_Values,gray

 
dir = 'rotated'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

dir = 'cropped'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
 
icnt = 0
input_image = cv.imread(file_name)  
cv.imshow('Test Image',input_image)
cv.waitKey()

#(threshold,Grayimg) = cv.threshold(input_image, 200, 255, cv.THRESH_BINARY)
grayImage = cv.cvtColor(~input_image, cv.COLOR_BGR2GRAY)
#cv.imshow('Grayimg Test Image',grayImage)
#cv.waitKey()

#edge_img = cv.Canny(Grayimg,225,900)
(thresh, edge_img) = cv.threshold(grayImage, 127, 255, cv.THRESH_BINARY)
#cv.imshow('edge',edge_img)
#cv.waitKey()

contours = cv.findContours(edge_img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv.contourArea, reverse=True)

for c in contours:
    (x, y, w, h) = cv.boundingRect(c)
    contours_area = w * h
    if w < 5:
        break
    crp = input_image[y:y + h, x:x + w]
    cv.imshow('CROP Test Image',crp)
    cv.waitKey()
    
    #print('crop done')

    fn = 'cropped/'+str(icnt)+'.jpg'
    #print('imwrite Path',fn)
    cv.imwrite(fn,crp)

    degree,Grayimg = image_to_angle(fn)
    if degree > 80:
        tilt = 180-degree
    else:
        tilt = degree
    print('Tilt Angle',tilt)
   
    result_img = imutils.rotate(Grayimg, tilt)
    #result_img = rotate_Image( Grayimg, tilt )
    fnr = 'rotated/'+str(icnt)+'.jpg'
    cv.imwrite(fnr,result_img)
    icnt = icnt+1
   
    cv.imshow('rotated Image',result_img)
    cv.waitKey()
   
dir = 'rotated'
if TEST_FILE == '01.jpg':
    ser = [7,0,6,11,9,1,8,10,4,2,12,3]
elif TEST_FILE == '02.jpg':
    ser = [6,5,12,12,1,4,9,3,2,11,12,1]
elif TEST_FILE == '03.jpg':
    ser = [0,1,4,7,3,2]
elif TEST_FILE == '04.jpg':
    ser = [0,6,4,5,2,3,7]
elif TEST_FILE == '05.jpg':
    ser = [2,3,7,6,0,1,4]
   
fcnt = 0
   
for f in ser:
    pathr = 'rotated/'+str(f)+'.jpg'
    i_image = cv.imread(pathr)
    rzimg = cv.resize(i_image,(50,100))
   
    if fcnt == 0:
        full_image = rzimg;
        fcnt = fcnt+1;
        cv.imshow('Rotated Character',rzimg)
        cv.waitKey()
    else:
        full_image = cv.hconcat([full_image,rzimg])
        cv.imshow('Rotated Character',rzimg)
        cv.waitKey()
   
cv.imshow('Final Image',full_image)
cv.waitKey()
cv.imwrite('Final_Image.jpg',full_image)
