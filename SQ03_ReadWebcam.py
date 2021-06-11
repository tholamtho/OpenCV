import cv2
#tạo video từ camera máy tính
video= cv2.VideoCapture(0)
#đặt kích thước cho video
width= int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height= int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#nơi lưu video, tốc độ khung hình 15 FPS
writer= cv2.VideoWriter('Ketqua.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 15, (width,height))
#Ghi hình


while True:
    ret,frame= video.read()
    i=0
    writer.write(frame)
    cv2.imshow('Live', frame)
    k = cv2.waitKey(1)
    if k == ord('a'):
       cv2.imwrite('a.jpg', frame)
    elif k == ord('b'):
       cv2.imwrite('b.jpg', frame)
    elif k == ord('c'):
       cv2.imwrite('c.jpg', frame)
    elif k == ord('d'):
       cv2.imwrite('d.jpg', frame)
# Nhấn ESC để ngừng quay
    elif cv2.waitKey(1) & 0xFF == 27:
        break
video.release()
writer.release()
cv2.destroyAllWindows()