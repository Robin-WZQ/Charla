# -----获取人脸样本-----
import cv2

# 调用笔记本内置摄像头，参数为0，如果有其他的摄像头可以调整参数为1,2
cap = cv2.VideoCapture(0)
# 调用人脸分类器，要根据实际路径调整3
face_detector = cv2.CascadeClassifier(r'haarcascade_frontalface_default_2.xml')  # 待更改

# sampleNum用来计数样本数目
count = 0

while True:
    # 从摄像头读取图片
    success, img = cap.read()
    # 转为灰度图片，减少程序符合，提高识别度
    if success is True:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        break
    # 检测人脸，将每一帧摄像头记录的数据带入OpenCv中，让Classifier判断人脸
    # 其中gray为要检测的灰度图像，1.3为每次图像尺寸减小的比例，5为minNeighbors
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    # 框选人脸，for循环保证一个能检测的实时动态视频流
    for (x, y, w, h) in faces:
        # xy为左上角的坐标,w为宽，h为高，用rectangle为人脸标记画框
        cv2.rectangle(img, (x, y), (x + w, y + w), (255, 0, 0))
        # 成功框选则样本数增加
        count += 1
        # 保持画面的连续。waitkey方法可以绑定按键保证画面的收放，通过q键退出摄像
    # k = cv2.waitKey(1)
    # if k == '27':
    #     break
    #     # 或者得到200个样本后退出摄像，这里可以根据实际情况修改数据量，实际测试后800张的效果是比较理想的
    # elif count >= 200:
    #     break

    # 显示图像
    cv2.imshow('image', img)  # 显示视频到窗口
    c = cv2.waitKey(10)
    if c & 0xFF == ord('q'):  # 键盘按q退出视频
        break


# 关闭摄像头，释放资源
cap.release()
cv2.destroyAllWindows()
