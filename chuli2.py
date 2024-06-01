import os
import random
import cv2

folder_list1 = ('train', 'test')  # 训练集和测试集
folder_list2 = (
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'
)  # 类标签，同时也是文件夹名
img_path = 'dataset2'  # 图片存储位置
folder_path = 'processed_dataset'  # 结构化文件夹数据集位置

judge = 25  # 将25%的数据放入测试集
blur_prob = 0.5  # 模糊概率
brightness_prob = 0.5  # 亮度改变概率

# 第一部分：创建结构化文件夹
for folder_name1 in folder_list1:
    for folder_name2 in folder_list2:
        os.makedirs(os.path.join(folder_path, folder_name1, folder_name2))

# 第二部分：图片分类预处理
for index, label in enumerate(folder_list2):
    for img in os.listdir(os.path.join(img_path, label)):
        full_file_name = os.path.join(img_path, label, img)
        if os.path.isfile(full_file_name):
            temp = cv2.imread(full_file_name, 1)  # 读取图片
            if temp is not None:
                temp = cv2.resize(temp, (96, 96))  # 将图片像素设置为96*96
                
                # 随机应用模糊
                if random.random() < blur_prob:
                    temp = cv2.GaussianBlur(temp, (5, 5), 0)
                
                # 随机改变亮度
                if random.random() < brightness_prob:
                    brightness_factor = random.uniform(0.5, 2.0)  # 生成一个随机亮度因子
                    temp = cv2.convertScaleAbs(temp, alpha=brightness_factor, beta=0)

                # 判断图片属于哪个数据集
                flag = random.randrange(0, 100)
                if flag < judge:
                    output_folder = os.path.join(folder_path, 'test', label)
                else:
                    output_folder = os.path.join(folder_path, 'train', label)

                # 保存预处理后的图片
                cv2.imwrite(os.path.join(output_folder, img), temp)
                print(folder_name1, ":", folder_name2)