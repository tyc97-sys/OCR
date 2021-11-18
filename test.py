import cv2 as cv
import numpy as np
import os

img_list = os.listdir('5')
for img in img_list:
    print(os.path.join('5', img))
    img_name = os.path.join('5', img)
    print(img_name)
    img = cv.imread(os.path.join('5', img), 0)
    ret, img_bin = cv.threshold(img, 156, 255, cv.THRESH_BINARY)

    cv.imshow('img_bin', img_bin)
    cv.waitKey(0)
    cv.destroyAllWindows()


    cv.imwrite(os.path.join('test', img_name), img_bin)
    print(os.path.join('test', img_name))


# img = cv.imread(r'2/22.jpg', 0)
# ret, img_bin = cv.threshold(img, 156, 255, cv.THRESH_BINARY)
#
# cv.imshow('img_bin', img_bin)
# cv.waitKey(0)
# cv.destroyAllWindows()
#
# cv.imwrite('test/1.jpg', img_bin)