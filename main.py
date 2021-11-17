import numpy as np
import cv2 as cv


def modify_contrast_and_brightness(img):
    # 公式： Out_img = alpha*(In_img) + beta
    # alpha: alpha參數 (>0)，表示放大的倍数 (通常介於 0.0 ~ 3.0之間)，能夠反應對比度
    # a>1時，影象對比度被放大， 0<a<1時 影象對比度被縮小。
    # beta:  beta参数，用來調節亮度
    # 常數項 beta 用於調節亮度，b>0 時亮度增強，b<0 時亮度降低。

    array_alpha = np.array([2.0]) # contrast
    array_beta = np.array([0.0]) # brightness

    # add a beta value to every pixel
    img = cv.add(img, array_beta)

    # multiply every pixel value by alpha
    img = cv.multiply(img, array_alpha)

    # 所有值必須介於 0~255 之間，超過255 = 255，小於 0 = 0
    img = np.clip(img, 0, 255)

    print("增加對比度 - 網路上常見的方法 (但沒有實現黑的更黑這件事): ")
    return img





img = cv.imread(r'OCR/4/2.jpg')

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
cv.imshow('org', img)
cv.imshow('eq', equalize_img)
cv.imshow('cl', clahe_img)
cv.imshow('usm', usm)
cv.imshow('binary', binary)
cv.imshow('result',result)
cv.waitKey(0)


cv.destroyAllWindows()