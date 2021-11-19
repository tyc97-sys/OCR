import numpy as np
import cv2 as cv

def usm(img, kenel_size):

    blur = cv.GaussianBlur(img, (0, 0), kenel_size)
    usm = cv.addWeighted(img, 1.5, blur, -0.5, 0)
    usm = cv.cvtColor(usm, cv.COLOR_BGR2GRAY)

    return usm

def eq(img):
    equalize_img = cv.equalizeHist(img)
    return equalize_img