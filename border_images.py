import cv2
# adding border:-
# Syntax: cv2.copyMakeBorder(src, top, bottom, left, right, borderType, value)
# ----------Border Types---------
# borderType: It depicts what kind of border to be added. It is defined by flags like
# ---------
# cv2.BORDER_CONSTANT: It adds a constant colored border. The value should be given as next argument.
# cv2.BORDER_REFLECT: The border will be mirror reflection of the border elements. Suppose, if image contains letters “abcdefg” then output will be “gfedcba|abcdefg|gfedcba“.
# cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT: It does the same works as cv2.BORDER_REFLECT but with slight change. Suppose, if image contains letters “abcdefgh” then output will be “gfedcb|abcdefgh|gfedcba“.
# cv2.BORDER_REPLICATE: It replicates the last element. Suppose, if image contains letters “abcdefgh” then output will be “aaaaa|abcdefgh|hhhhh“.
#----------------------------------------------------------------
img = cv2.imread('Photos\cat.png',1)

bordered_img = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT)

cv2.imshow('Bordered Image',bordered_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
