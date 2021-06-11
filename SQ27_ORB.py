import numpy as np
import cv2

#Compare  Pics to Others
from matplotlib import pyplot as plt
img1 = cv2.imread('anh1.png',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('anh2.jpg',cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('anh3.png',cv2.IMREAD_GRAYSCALE)
img4 = cv2.imread('anh4.jpg',cv2.IMREAD_GRAYSCALE)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
kp3, des3 = orb.detectAndCompute(img3,None)
kp4, des4 = orb.detectAndCompute(img4,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches1 = bf.match(des1,des2)
matches1 = sorted(matches1, key = lambda x:x.distance)
matches2 = bf.match(des3,des4)
matches2 = sorted(matches2, key = lambda x:x.distance)
img5 = cv2.drawMatches(img1,kp1,img2,kp2, matches1[:40],img2,flags=2)
img6 = cv2.drawMatches(img3,kp3,img4,kp4, matches2[:40],img4,flags=2)
plt.imshow(img5),plt.show()
plt.imshow(img6),plt.show()
