import cv2
import numpy as np
import matplotlib.pyplot as plt  

count = int(input("enter count"))

for i in range (0,count,1):
    print (i)

x = [1,2,3,4,5]
y = [3,5,7,9,11]

plt.plot(x,y,'r-*',linewidth=3, markersize=8)
plt.show()

img = cv2.imread("")
cv2.imshow("",img)