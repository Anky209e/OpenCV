import cv2 as cv

main_frame = cv.imread("images/csgo.jpg",0)
sub_frame = cv.imread("images/man.jpg",0)

result = cv.matchTemplate(main_frame,sub_frame,cv.TM_CCORR_NORMED)
print(result)
min_val,max_val,min_loc,max_loc = cv.minMaxLoc(result)

print("Min val:",min_val)
print("Max val:",max_val)
print("Min loc:",min_loc)
print("Max loc:",max_loc)

# it guves shape as Height and width 1 is height and 0 access width

sub_frame_height = sub_frame.shape[1]
sub_frame_width= sub_frame.shape[0]

#  max_loc guves us the top left corner of image found we have 
# to calculate bottom right before drawing boxes.

top_left_cd = max_loc 
bottom_right_cd = (top_left_cd[0]+sub_frame_width,top_left_cd[1]+sub_frame_height)
print(bottom_right_cd)

cv.rectangle(main_frame,top_left_cd,bottom_right_cd,color=(0,255,0),thickness=2,lineType=cv.LINE_4)
cv.imwrite("images/marked_csgo_enemy.jpg",main_frame)
cv.imshow("FInal",main_frame)


cv.waitKey(0)
cv.destroyAllWindows()

