import cv2
im = cv2.imread('IMG/Coin.png') # read picture

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) # BGR to grayscale

ret, thresh = cv2.threshold(imgray, 200, 255, cv2.THRESH_BINARY)

countours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

epsilon = 0.1 * cv2.arcLength(countours[0], True)
approx = cv2.approxPolyDP(countours[0], epsilon, True)

cv2.drawContours(im, approx, -1, (0, 0, 255), 3)
cv2.imshow("Contour", im)

cv2.waitKey(0)
cv2.destroyAllWindows()
