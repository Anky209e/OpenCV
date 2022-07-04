import cv2
import numpy as np
'''
Thresholding is a technique in OpenCV, which is the assignment of pixel 
values in relation to the threshold value provided.
In thresholding, each pixel value is compared with the threshold value. 
If the pixel value is smaller than the threshold, it is set to 0, 
otherwise, it is set to a maximum value (generally 255).
Thresholding is a very popular segmentation technique, 
used for separating an object considered as a foreground from its background.
'''
# syntax : cv2.threshold(source,thresholdvalue,maxvalue,technique)

'''
The different Simple Thresholding Techniques are:

cv2.THRESH_BINARY: If pixel intensity is greater than the set threshold, 
value set to 255, else set to 0 (black).

cv2.THRESH_BINARY_INV: Inverted or Opposite case of cv2.THRESH_BINARY.

cv.THRESH_TRUNC: If pixel intensity value is greater than threshold, it is truncated to the threshold. 
The pixel values are set to be the same as the threshold. All other values remain the same.

cv.THRESH_TOZERO: Pixel intensity is set to 0, for all the pixels intensity, 
less than the threshold value.

cv.THRESH_TOZERO_INV: Inverted or Opposite case of cv2.THRESH_TOZERO.


'''

img1 = cv2.imread('Photos\cat.png')
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

# applying all thresolds

ret,binary_thresh_img = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
ret,binary_inv_img = cv2.threshold(img,120,255,cv2.THRESH_BINARY_INV)
ret,trunc_img = cv2.threshold(img,120,255,cv2.THRESH_TRUNC)
ret,tozero_img = cv2.threshold(img,120,255,cv2.THRESH_TOZERO)
ret,tozero_inv_img = cv2.threshold(img,120,255,cv2.THRESH_TOZERO_INV)


cv2.imshow('Binary',binary_thresh_img)
cv2.imshow('Binary INV',binary_inv_img)
cv2.imshow('Trunc',trunc_img)
cv2.imshow('Tozero',tozero_img)
cv2.imshow('Tozer INV',tozero_inv_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

