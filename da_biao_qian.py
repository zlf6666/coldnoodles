# 导入所需要的库
import cv2
import numpy as np

# 定义保存图片函数
# image:要保存的图片名字
# addr；图片地址与相片名字的前部分
# num: 相片，名字的后缀。int 类型
def save_image(image,addr,num):
    address = addr + str(num)+ '.jpg'
    cv2.imwrite(address,image)

# 读取视频文件
videoCapture = cv2.VideoCapture("D:/xf500_color_video/000000/P01_01_00_0_color.avi")
# 通过摄像头的方式
# videoCapture=cv2.VideoCapture(1)

#读帧
success, frame = videoCapture.read()
i = 0
while success :
    i = i + 1
    save_image(frame,'D:/daBiaoQian/img_',i)
    if success:
        print('save image:',i)
    success, frame = videoCapture.read()