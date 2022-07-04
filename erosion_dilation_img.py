import cv2 
import numpy as np

img = cv2.imread('Photos\cat.png',1)

# taking matrixc of size five as kernal
kernal = np.ones((5,5),np.uint8)

# iteration is how much you want to erose or dilate

erosed_img = cv2.erode(img,kernal,iterations=2)

dilate_img = cv2.dilate(img,kernal,iterations=2)

cv2.imshow('Erosed imaage',erosed_img)

cv2.imshow('Dilated image',dilate_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

