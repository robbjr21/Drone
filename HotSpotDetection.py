import cv2
import numpy as np

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Computing red color
red = np.uint8([[[255, 0, 0 ]]])
red_hsv = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print(red_hsv)

img = cv2.imread('Thermal.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# viewImage(img_hsv)

green_low = np.array([45 , 100, 50] )
green_high = np.array([75, 255, 255])
curr_mask = cv2.inRange(img_hsv, green_low, green_high)
img_hsv[curr_mask > 0] = ([75,255,200])
viewImage(img_hsv) ## 2

# viewImage(output_hsv)

## converting the HSV image to Gray inorder to be able to apply
## may need to be output_hsv
RGB_again = cv2.cvtColor(img_hsv, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
viewImage(gray) ## 3
ret, threshold = cv2.threshold(gray, 90, 255, 0)
# viewImage(threshold) ## 4
contours, hierarchy =  cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)

def findGreatesContour(contours):
    largest_area = 0
    largest_contour_index = -1
    i = 0
    area = []
    total_contours = len(contours)
    while (i < total_contours ):
        AREA = cv2.contourArea(contours[i])
        area.append(AREA)
        if(AREA > largest_area):
            largest_area = AREA
            largest_contour_index = i
        i+=1
    for i in area:
        if i < 13000:
            area.remove(i)
    return largest_area, largest_contour_index, area

largest_area, largest_contour_index, area = findGreatesContour(contours)
# print("Largest area is {}".format(largest_area))
# print("Largest contour index is {}".format(largest_contour_index))
# print("Number of contours is {}".format(len(contours)))
# print("Size of area array is {}".format(len(area)))
