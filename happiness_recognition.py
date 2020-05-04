# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 01:28:58 2020

@author: Desktop
"""

import cv2


smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        debut = y+2*h//3
        print(debut)
        roi_face_gray = gray[debut:y+h,x:x+w]
        roi_face_frame = frame[debut:y+h,x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_face_gray,1.7,22)
        for (sx,sy,sw,sh) in smiles:
            cv2.rectangle(roi_face_frame,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)
            break


            
    return frame
        
    



video_capture = cv2.VideoCapture(0)

while True:
    _,frame = video_capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    canvas = detect(gray,frame)
    cv2.imshow('Video0',canvas)
    if cv2.waitKey(1) == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
    
