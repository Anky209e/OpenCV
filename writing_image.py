import cv2


# path of image--
path = r'Photos\demo.jpg'
img = cv2.imread(path, 1) # 1 is used as parameter for color modee

cv2.imshow('Window Title',img)

# making image write

cv2.imwrite('filename.jpg',img)

# making window stop

cv2.waitKey(0)

cv2.destroyAllWindows()

