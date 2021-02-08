import cv2
import numpy as np

img = cv2.imread('Photos\cat.png',1)

edge_img = cv2.Canny(img,100,200)

cv2.imshow('Edge detect',edge_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
