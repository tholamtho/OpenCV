import cv2
from matplotlib import pyplot as plt
import  numpy as np

path = r'IMG\Troang.jpg'

img = cv2.imread(path)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

cv2.imshow('Original',img)
cv2.imshow('HSV',hsv)
cv2.imshow('RGB', rgb)
cv2.imshow('YUV',yuv)

cv2.waitKey(0)
cv2.destroyWindow()