import cv2 as cv
cap =cv.VideoCapture("D:/xf500_color_video/000000/P01_01_00_0_color.avi")
isOpened = cap.isOpened
print(isOpened)
fps = cap.get(cv.CAP_PROP_FPS)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(fps,width,height)
i = 0
while(isOpened):
    if i == 60:
        break
    else:
        i = i + 1
    (flag,frame) = cap.read()#读取每一张 flag frame
    fileName = 'image' + str(i)+'.jpg'
    print(fileName)
    if flag == True:
        cv.imwrite(fileName,frame,[cv.IMWRITE_JPEG_LUMA_QUALITY,100])
print('end!')