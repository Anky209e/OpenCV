import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # threshold of blue 
    lower_blue = np.array([35,140,60])
    upper_blue = np.array([255,255,180])

    # overlaying mask
    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    cv2.imshow('frame',hsv)

    cv2.waitKey(0)

cv2.destroyAllWindows()
cap.release()