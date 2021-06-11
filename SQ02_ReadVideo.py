import cv2
import numpy as np

path = r''
img = cv2.imread('a.jpg')
image_to_show = np.copy(img)

videoCapture = cv2.VideoCapture(path)
fps = videoCapture.get(cv2.CAP_PROP_FPS)
size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
videoWriter = cv2.VideoWriter('Output.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)
success, frame = videoCapture.read()
cv2.namedWindow('image')
i = 0

while True:
    draw()
    cv2.imshow('image', image_to_show)
    k = cv2.waitKey(1)
    if k == ord('s'): #bam s luu anh
        cv2.imwrite('Anh'+str(i)+'.png', image_to_show)
        i = i + 1
    elif k == 27 :
        break
        cv2.destroyAllWindown()