from __future__ import print_function
import os
import cv2

alpha = 0.5

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3
print(''' Simple Linear Blender
-----------------------
Enter alpha [0.0-1.0]: ''')
input_alpha = float(raw_input().strip())
if 0 <= alpha <= 1:
    alpha = input_alpha

# input images
filePath = r'/home/system/Desktop/ws/myPy/data/'
src1 = cv2.imread(os.path.join(filePath,'seatle-skyline-kingwu.jpg'))
src2 = cv2.imread(os.path.join(filePath,'somerset.jpg'))
src1 = cv2.resize(src1,(400,400))
src2 = cv2.resize(src2,(400,400))

# [load]
if src1 is None:
    print("Error loading src1")
    exit(-1)
elif src2 is None:
    print("Error loading src2")
    exit(-1)
# [blend_images]
beta = (1.0 - alpha)
dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)
# [blend_images]
# [display]
cv2.imshow('dst', dst)
cv2.waitKey(0)
# [display]     
cv2.destroyAllWindows()