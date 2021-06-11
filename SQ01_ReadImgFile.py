import cv2

path = r'D:\OpenCV_Project\IMG\Troang.jpg' #path link given

img = cv2.imread(path)
while True:
    cv2.imshow('New', img)
    k = cv2.waitKey(1)
    if k == ord('q'):
        new_name = 'NewImg.png'
        cv2.imwrite(new_name, img)
        cv2.waitKey(15)
        break