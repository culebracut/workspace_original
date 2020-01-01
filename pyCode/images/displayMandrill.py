import cv2
import numpy as np
import matplotlib.pyplot as plt  

# test of github 2
img = cv2.imread('/home/system/Desktop/ws/myPy/data/baboon.jpg',cv2.IMREAD_COLOR)
cv2.imshow('img',img)
cv2.waitKey(0)

cv2.destroyAllWindows()
