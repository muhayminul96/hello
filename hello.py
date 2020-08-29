import numpy as np
import cv2,time

video = cv2.VideoCapture(0)

while True:

    success,img=video.read()
    cv2.imshow("video",img)
    if cv2.waitKey(12) & 0xFF ==ord('q'):
        break
video.release()
cv2.destroyAllWindows()


