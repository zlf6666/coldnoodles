import numpy as np
from PIL import Image
import pickle
import matplotlib.pyplot as plt
img_22 = Image.open('D:/daBiaoQian/img_22.jpg')
img_36 = Image.open('D:/daBiaoQian/img_36.jpg')

# 显示图片
plt.imshow(img_22)

img_22_n = np.array(img_22)
img_36_n = np.array(img_36)
print(type(img_22_n))


# 创建一个空list，用于存储图像数据因为是两张图片所以创建2个(480, 640, 3)的矩阵。
image_data = []

# 把数据存放进来
image_data.append(img_22_n)
image_data.append(img_36_n)

# 添加标签，假设这两张图片是两个类别，把他们标注为类型1和2
image_data_label = np.empty(2)

image_data_label[0] = 1
image_data_label[1] = 2

# 把标签的类型转换成int类型,为了方便出来也把data转换成numpy.ndarray类型
image_data = np.array(image_data)
image_data_label=image_data_label.astype(np.int)
print(image_data_label)

plt.imshow(image_data[1])

# 把数据合并成一个元组进行保存
train_data = (image_data,image_data_label)

# 把数据写入pkl文件中
write_file=open('D:/daBiaoQian/train_data.pkl','wb')
pickle.dump(train_data,write_file)
write_file.close()

# 从pkl文件中读取图片数据和标签
read_file=open('D:/daBiaoQian/train_data.pkl','rb')

(train_data,lab_data)=pickle.load(read_file)
read_file.close()

# 查看读取出来的数据
print(train_data.shape)
plt.show(train_data[0])


