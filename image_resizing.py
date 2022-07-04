import cv2

import numpy as np




'''-------------------------------------------------------
Choice of Method for resizing:-
1) cv2.INTER_AREA:-  This is used when we need need to shrink an image.
2) cv2.INTER_CUBIC:- This is slow but more efficient.
3) cv2.INTER_LINEAR:- This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.
--------------------------------------------------------------'''

img = cv2.imread('Photos\demo.jpg',1)

half = cv2.resize(img, (0,0), fx=0.1,fy=0.1)

cv2.imshow('window',half)

cv2.waitKey(0)
cv2.destroyAllWindows()