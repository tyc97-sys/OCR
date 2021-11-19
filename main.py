import argparse
import numpy as np
import cv2 as cv
import usm
import os

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--method", type=str, help="Choice your method", default='usm')
args = parser.parse_args()
print(args.method)
path = '5/32.jpg'
img = cv.imread(path)

if args.method == 'usm':
    result = usm.usm(img, 9)
elif args.method == 'usm+eq':
    result = usm.usm(img, 9)
    result = usm.eq(result)
elif args.method == 'eq':
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    result = usm.eq(img)



cv.imshow('usm', result)
cv.waitKey(0)
cv.destroyAllWindows()

cv.imwrite(os.path.join("test", path), result)