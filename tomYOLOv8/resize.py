from PIL import Image
import os

file_path = r"C:/Users/Lzd/tomato/2024.6.15采集数据/tomato"  # 原始图像路径
save_path = r"C:/Users/Lzd/tomato/2024.6.15采集数据/resizetomato"  # 修改后图像存储的路径

if not os.path.exists(save_path):  # 如果没有这个文件夹，就新建
    os.makedirs(save_path)

for root, dirs, files in os.walk(file_path):
    for file in files:  # 展现各文件
        picture_path = os.path.join(root, file)  # 得到图像的绝对路径
        pic_org = Image.open(picture_path)  # 打开图像
        pic_new = pic_org.resize((1280, 960),)  # 图像尺寸修改
        pic_new_path = os.path.join(save_path, file)  # 新图像存储绝对路径
        pic_new.save(pic_new_path)  # 存储文件
        print("%s 已裁切完成!" % pic_new_path)