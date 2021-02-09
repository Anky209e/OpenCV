import cv2

'''
syntax : cv2.adaptiveThreshold(source,maxval,method,type,blocksize constant)
There are two adaptive methods:
cv2.ADAPTIVE_THRESH_MEAN_C
cv2.ADAPTIVE_THRESH_GAUSSIAN_C
'''

img = cv2.imread('Photos\cat.png',0)

thresh1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,199,5)
thresh2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,199,5)

cv2.imshow('Mean thresh',thresh1)
cv2.imshow('Gauss thresh',thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()