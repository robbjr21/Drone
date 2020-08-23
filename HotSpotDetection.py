import cv2
import numpy as np

def viewImage(image):
    cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
    cv2.imshow('Display', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Method 1
#***********************************************
img = cv2.imread('Thermal.jpg')
viewImage(img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
viewImage(img_hsv)

# lower mask (0-10)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join my masks
mask = mask0+mask1

# set my output img to zero everywhere except my mask
output_img = img.copy()
output_img[np.where(mask==0)] = 0
viewImage(output_img)
#***********************************************

## converting the HSV image to Gray inorder to be able to apply
## may need to be output_hsv
RGB_again = cv2.cvtColor(output_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
viewImage(gray) ## 3

ret, threshold = cv2.threshold(gray, 90, 255, 0)
viewImage(threshold) ## 4

contours, hierarchy =  cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
viewImage(img)

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
        if i < 13500:
            area.remove(i)
    return largest_area, largest_contour_index, area

largest_area, largest_contour_index, area = findGreatesContour(contours)
print("Largest area is {}".format(largest_area))
print("Largest contour index is {}".format(largest_contour_index))
print("Number of contours is {}".format(len(contours)))
print("Size of area array is {}".format(len(area)))
