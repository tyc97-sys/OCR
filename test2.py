import numpy as np
import cv2 as cv

img = cv.imread(r'5/3.jpg')

blur = cv.GaussianBlur(img, (0, 0), 5)
usm = cv.addWeighted(img, 1.5, blur, -0.5, 0)
usm = cv.cvtColor(usm, cv.COLOR_BGR2GRAY)
equalize_img = cv.equalizeHist(usm)

clahe = cv.createCLAHE()
clahe_img = clahe.apply(usm)

binary = cv.adaptiveThreshold(equalize_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

se = cv.getStructuringElement(cv.MORPH_RECT, (1, 1))
se = cv.morphologyEx(se, cv.MORPH_OPEN, (2, 2))
mask = cv.dilate(binary, se)

mask1 = cv.bitwise_not(mask)
binary = cv.bitwise_and(usm, mask)
result = cv.add(binary, mask1)




############
# cv.imshow('org', img)
# cv.imshow('eq', equalize_img)
# cv.imshow('cl', clahe_img)
cv.imshow('usm', usm)
# cv.imshow('binary', binary)
# cv.imshow('result',result)
cv.waitKey(0)
cv.destroyAllWindows()