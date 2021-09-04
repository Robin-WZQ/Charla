# -----建立模型、创建数据集-----#-----建立模型、创建数据集-----

import os
import cv2
import numpy as np
from PIL import Image

# 导入pillow库，用于处理图像
# 设置之前收集好的数据文件路径
path = 'data'

# 初始化识别的方法
recog = cv2.face.LBPHFaceRecognizer_create()

# 调用熟悉的人脸分类器
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# 创建一个函数，用于从数据集文件夹中获取训练图片,并获取id
# 注意图片的命名格式为User.id.sampleNum
def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    # 新建连个list用于存放
    face_samples = []
    ids = []

    # 遍历图片路径，导入图片和id添加到list中
    for image_path in image_paths:

        # 通过图片路径将其转换为灰度图片
        img = Image.open(image_path).convert('L')

        # 将图片转化为数组
        img_np = np.array(img, 'uint8')

        if os.path.split(image_path)[-1].split(".")[-1] != 'jpg':
            continue

        # 为了获取id，将图片和路径分裂并获取
        id = int(os.path.split(image_path)[-1].split(".")[1])
        faces = detector.detectMultiScale(img_np)

        # 将获取的图片和id添加到list中
        for (x, y, w, h) in faces:
            face_samples.append(img_np[y:y + h, x:x + w])
            ids.append(id)
    return face_samples, ids


# 调用函数并将数据喂给识别器训练
print('Training...')
faces, ids = get_images_and_labels(path)
# 训练模型
recog.train(faces, np.array(ids))
# 保存模型
recog.save('trainner/trainner.yml')