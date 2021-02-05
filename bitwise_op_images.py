import cv2

img1 = cv2.imread('Photos\demo.jpg',1)
img2 = cv2.imread('Photos\l1demo.jpg',1)

# there are four bitwise operaters
# 1) AND 2)OR 3) XOR 4) NOT

#----------AND operator-----------
# syntex: cv2.bitwise_and(source1,source2,dest.,mask)

# bit_and = cv2.bitwise_and(img1,img2,mask=None)

# cv2.imshow('AND operator',bit_and)

#------------OR operator--------

# bit_or = cv2.bitwise_or(img1,img2,mask=None)

# cv2.imshow('OR operator',bit_or)

#----------XOR operator----------

# bit_xor = cv2.bitwise_xor(img1,img2,mask=None)

# cv2.imshow('XOR operator',bit_xor)

#----------NOT operator--------

bit_nor1 = cv2.bitwise_not(img1,mask=None)
bit_nor2 = cv2.bitwise_not(img2,mask=None)

finalimg = cv2.add(bit_nor1,bit_nor2,)

cv2.imshow('NOT operator',finalimg)



cv2.waitKey(0)

cv2.destroyAllWindows()
