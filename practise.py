import cv2
import numpy as np

img=cv2.imread("lena.jpg",1)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(3,3),0)
canny=cv2.Canny(img,2,2)



cv2.imshow("simple",img)
cv2.imshow("gray image",gray)
cv2.imshow("blur image",blur)
cv2.imshow("canny image",canny)
cv2.waitKey(0)