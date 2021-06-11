import cv2
import numpy as np
# Mô tả đặc trưng của người
def is_inside(o, i):
    ox, oy, ow, oh = o
    ix, iy, iw, ih = i
    return ox > ix and oy > iy and ox + ow < ix + iw and oy + oh <iy + ih
def draw_person(image, person):
    x, y, w, h = person
    # Khung hình chữ nhật bao xung quanh người
    cv2.rectangle (img1, (x, y), (x + w, y + h), (0, 255, 255), 2)
    cv2.rectangle (img2, (x, y), (x + w, y + h), (0, 255, 255), 2)
# Đọc ảnh
img1 = cv2.imread("people3.jpg")
img2 = cv2.imread("people4.jpg")
# Sử dụng bộ dò người mặc định
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
# Sử dụng phương pháp nhận dạng khuôn mặt detectMultiScale
found, w = hog.detectMultiScale(img1)
found, w = hog.detectMultiScale(img2)
#Phương thức phát hiện sẽ trả về một mảng các hình chữ nhật, đây sẽ là một
#nguồn thông tin để chúng ta bắt đầu vẽ các hình trên ảnh. Một số hình chữ nhật
#hoàn toàn được chứa trong các hình chữ nhật khác. Một hình chữ nhật nằm hoàn toàn bên trong một hình chữ nhật khác có thể bị loại bỏ bằng cách dùng một hàm is_inside và lặp qua lặp lại kết quả phát hiện để loại bỏ kết quả dương tính giả.
found_filtered = []
for ri, r in enumerate(found):
    for qi, q in enumerate(found):
        if ri != qi and is_inside(r, q):
            break
        else:
            found_filtered.append(r)
for person in found_filtered:
    draw_person(img1, person)
    draw_person(img2, person)
# Hiển thị ảnh
cv2.imshow("people detection1", img1)
cv2.imshow("people detection2", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
