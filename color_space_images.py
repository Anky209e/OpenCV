import cv2
import numpy as np

img = cv2.imread('Photos\cat.png',1)

chng_img = cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)



lab_img = cv2.cvtColor(img,cv2.COLOR_BGR2LAB)

stck_img = np.hstack((img,chng_img,lab_img))

#edge map

lapli_img = cv2.Laplacian(img,cv2.CV_64F)
stck_img = np.hstack((img,lapli_img))

cv2.imshow('YCrCb',stck_img)


cv2.waitKey(0)
cv2.destroyAllWindows()