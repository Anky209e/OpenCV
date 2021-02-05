import cv2 
import numpy as np

img = cv2.imread('Photos\cat.png',1)

# --------Gaussian Blur----
gauss_img = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian blurred image',gauss_img)

#-----Median blur--------

med_img = cv2.medianBlur(img,7)
cv2.imshow('Median blurred image',med_img)

#------Bilateral blur------
bilateral_img = cv2.bilateralFilter(img,9,80,80)
cv2.imshow('Bilateral blurred image',bilateral_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
