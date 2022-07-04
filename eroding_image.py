import cv2
import numpy as np
# Syntax: cv2.erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

img = cv2.imread('Photos\demo.jpg',1)

kernel = np.ones((7,7),np.uint8)

erod_img = cv2.erode(img,kernel)

cv2.imshow('Erroded image',erod_img)

cv2.waitKey(0)
cv2.destroyAllWindows()