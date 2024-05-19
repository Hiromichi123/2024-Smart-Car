import os
import random
import cv2

folder_list1 = ('train', 'test')  # 训练集和测试集
folder_list2 = \
    (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'
    )  # 类标签，同时也是文件夹名
img_path = 'dataset2'  # 图片存储位置
folder_path = 'processed_dataset'  # 结构化文件夹数据集位置

judge = 25  # 将25%的数据放入测试集
flag = random.randrange(0, 100)  # 产生0-99的伪随机整数以判定图片所属数据集

for folder_name1 in folder_list1:
    for folder_name2 in folder_list2:
        os.makedirs(os.path.join(folder_path, folder_name1, folder_name2))
# 第一部分：创建结构化文件夹

for index, label in enumerate(folder_list2):
    for img in os.listdir(os.path.join(img_path, label)):
        temp = cv2.imread(os.path.join(img_path, label, img), 1)  # 读取图片
        if temp is not None:
            temp = cv2.resize(temp, (96, 96))  # 将图片像素设置为96*96
            flag = random.randrange(0, 100)
            full_file_name = os.path.join(img_path, label, img)
            print(label, img, flag)
            if (flag < judge) and (os.path.isfile(full_file_name)):
                cv2.imwrite(os.path.join(folder_path, 'test', label, img), temp)
            if (flag >= judge) and (os.path.isfile(full_file_name)):
                cv2.imwrite(os.path.join(folder_path, 'train', label, img), temp)
        else:
            break