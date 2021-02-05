import cv2

img1 = cv2.imread('Photos\demo.jpg',1)
img2 = cv2.imread('Photos\l1demo.jpg',1)

# added_image = cv2.add(img1,img2)

# cv2.imshow("Added images",added_image)

subt_image = cv2.subtract(img2,img1)

cv2.imshow('Subtracted image',subt_image)

cv2.waitKey(0)
cv2.destroyAllWindows()