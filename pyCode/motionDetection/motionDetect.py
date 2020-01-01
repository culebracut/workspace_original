import cv2, time
import numpy as np


def getFrame (): 
    check, frame = video.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21), 0)
    return (frame,gray) 

def trackbar_callback(idx, value):
    foobar = value

video = cv2.VideoCapture(0)
frame, first_frame = getFrame()

while True:
    frame, gray = getFrame()

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_delta = cv2.dilate(thresh_delta, None, iterations=0)

    contours, hierarchy = cv2.findContours(thresh_delta, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0, 255,0),3)

    cv2.imshow('frame',frame)
    cv2.moveWindow('frame',1000,0)

    cv2.imshow('capturing',gray)
    cv2.moveWindow('capturing',1000,1000)
    cv2.imshow('thresh',thresh_delta)
    cv2.moveWindow('thresh',0,0)
    cv2.imshow('delta',delta_frame)
    cv2.moveWindow('delta',0,1000)

    key = cv2.waitKey(1)
    if key == 27:
        break
    if key == ord('r'):
        frame, first_frame = getFrame()

video.release()
cv2.destroyAllWindows

