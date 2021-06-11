import numpy as np
import cv2
from matplotlib import pyplot as plt
img1 = cv2.imread('anh1.png',0)
img2 = cv2.imread('anh2.jpg',0)
img3 = cv2.imread('anh3.png',0)
img4 = cv2.imread('anh4.jpg',0)
orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)
kp3, des3 = orb.detectAndCompute(img3,None)
kp4, des4 = orb.detectAndCompute(img4,None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches1 = bf.knnMatch(des1,des2, k=1)
matches2 = bf.knnMatch(des3,des4, k=1)
img5 = cv2.drawMatchesKnn(img1,kp1,img2,kp2, matches1,img2,flags=2)
img6 = cv2.drawMatchesKnn(img3,kp3,img4,kp4, matches2,img3,flags=2)
plt.imshow(img5),plt.show()
plt.imshow(img6),plt.show()
