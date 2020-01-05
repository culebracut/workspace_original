import os
import cv2
import numpy as np

def nothing(x):
    pass

# input images
filePath  = r'/home/system/Desktop/workspace/pySandbox/data/images/'
src1 = cv2.imread(os.path.join(filePath,'seatle-skyline-kingwu.jpg'))
src2 = cv2.imread(os.path.join(filePath,'somerset.jpg'))
#src1 = cv2.resize(src1,(900,600))
src2 = cv2.resize(src2,(900,600))
img = src2

# Create a black image, a window
cv2.namedWindow('image')
cv2.createTrackbar('R','image',0,255,nothing)

#
while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions 
    r = cv2.getTrackbarPos('R','image')
    rFloat = float(r)/float(255)

    #
    img = cv2.addWeighted(src1, rFloat, src2, 1-rFloat, 0.0)
    cv2.imshow('image',img)

cv2.destroyAllWindows()