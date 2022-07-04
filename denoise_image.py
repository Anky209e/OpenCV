import cv2

import numpy

img = cv2.imread('Photos\cat.png',1)

denoised_img = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,15)



stck_images = numpy.hstack((img,denoised_img))

cv2.imshow('denoised images',stck_images)

cv2.waitKey(0)
cv2.destroyAllWindows()