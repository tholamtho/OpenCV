import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('NewImg.png')
blur = cv.GaussianBlur(img,(5,5),0)
blur2 = cv.medianBlur(img,5)
cv.imshow('Original', img)
cv.imshow('Blur', blur)
cv.imshow('Median', blur2)

cv.waitKey(0)
cv.destroyWindow()