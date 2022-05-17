import cv2 as cv
from cv2 import rectangle
import numpy as np

main_frame = cv.imread("images/csgo.jpg",0)
sub_frame = cv.imread("images/man.jpg",0)
sub_frame_height = sub_frame.shape[1]
sub_frame_width= sub_frame.shape[0]
result = cv.matchTemplate(main_frame,sub_frame,cv.TM_SQDIFF_NORMED)

min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)
threshold = 0.2
locations = np.where(result<=threshold)
locations = list(zip(*locations[::-1]))

# we will create a list of rectangles to prevent from overdrawing
# [x,y,w,h]
rectangles = []
for loc in locations:
    rect = [int(loc[0]),int(loc[1]),sub_frame_width,sub_frame_height]
    rectangles.append(rect)

# prevention of rectangle overlapping
rectangles,weights = cv.groupRectangles(rectangles,1,0.5)


if len(rectangles):
    print("Found Image")

    line_color = (0,255,0)
    line_type = cv.LINE_4

    for (x,y,w,h) in rectangles:
        top_left_cd = (x,y)
        bottom_right_cd = (x+h,y+w)
        cv,rectangle(main_frame,top_left_cd,bottom_right_cd,line_color,line_type)

    cv.imshow("Images",main_frame)
    cv.waitKey(0)
else:
    print("Not Found")




