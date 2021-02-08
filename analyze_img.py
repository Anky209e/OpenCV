import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread('Photos\cat.png',0)
# analyzing image using histogram 


# plt.hist(img.ravel(),200,[1,256])
# plt.show()


# Histogram equalization is a method in image processing of
# contrast adjustment using the image’s histogram.

#----------histogram equalistaion------

equalized_img = cv2.equalizeHist(img)

# stacking image side by side

stck_imges = np.hstack((img,equalized_img))

cv2.imshow('Images',stck_imges)

cv2.waitKey(0)
cv2.destroyAllWindows()