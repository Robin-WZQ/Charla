# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Emotion.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from real_time_video_me import Emotion_Rec
from os import getcwd
import numpy as np
import cv2
import time
import sys
import logging
from base64 import b64decode
from os import remove
from slice_png import img as bgImg
import image1_rc
# from PyQt5.QtWidgets import QApplication,QMainWindowp;
from PyQt5.QtMultimediaWidgets import QVideoWidget
from myVideoWidget import myVideoWidget
import imutils

class emo(QMainWindow):
    def __init__(self):
        super(emo, self).__init__()
        self.path = getcwd()
        self.timer_camera = QtCore.QTimer()  # 定时器

        MainWindow=self
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 849)
        MainWindow.setAutoFillBackground(False)


        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.wgt_video = myVideoWidget(self.centralwidget)
        self.wgt_video.setObjectName("centralwidget")
        self.wgt_video.setGeometry(QtCore.QRect(10, 10, 1051, 631))
        # self.wgt_video.setAlignment(QtCore.Qt.AlignCenter)
        self.wgt_video.setObjectName("wgt_video")

        self.label_face = QtWidgets.QLabel(self.centralwidget)
        self.label_face.setGeometry(QtCore.QRect(10, 10, 401, 301))
        self.label_face.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_face.setFont(font)
        self.label_face.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_face.setStyleSheet("border-image: url(:/newPrefix/images_test/scan.gif);")
        self.label_face.setObjectName("label_face")

        # 后加的
        # self.pushButton_op
        self.pushButton_op = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_op.setGeometry(QtCore.QRect(10, 770, 130, 50))
        self.pushButton_op.setObjectName("实时分析")

        self.label_scanResult = QtWidgets.QLabel(self.centralwidget)
        self.label_scanResult.setGeometry(QtCore.QRect(50, 720, 281, 31))
        self.label_scanResult.setAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_scanResult.setFont(font)
        # self.label_scanResult.setStyleSheet("color: rgb(0, 189, 189);")
        self.label_scanResult.setObjectName("label_scanResult")


        self.label_outputResult = QtWidgets.QLabel(self.centralwidget)
        self.label_outputResult.setGeometry(QtCore.QRect(10, 360, 401, 281))
        self.label_outputResult.setText("")
        self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test/ini.png);")
        self.label_outputResult.setObjectName("label_outputResult")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 720, 71, 31))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(450, 20, 20, 800))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 330, 421, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 670, 411, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1544, 22))
        self.menubar.setObjectName("menubar")

        self.pushButton_op.setText("我准备好啦~~~")

        self.label.setText("结果")
        self.label_scanResult.setText("None")
        self.label_face.setText("<html><head/><body><p align=\"center\"><br/></p></body></html>")

        self.slot_init()  # 槽函数设置
        # 设置界面动画
        gif = QMovie(':/newPrefix/images_test/scan.gif')
        self.label_face.setMovie(gif)
        gif.start()

        self.cap = cv2.VideoCapture()  # 屏幕画面对象
        self.CAM_NUM = 0  # 摄像头标号
        self.model_path = None  # 模型路径
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)  # 视频播放输出的widget，就是上面定义的

        self.timePlay = ' '
    # 定义槽函数
    def slot_init(self):

        self.pushButton_op.clicked.connect(self.button_open_camera_click)  # 后加的

        self.timer_camera.timeout.connect(self.show_camera)

    # 打开摄像头  实时分析
    def button_open_camera_click(self):
        if self.timer_camera.isActive() == False:  # 检查定时状态
            flag = self.cap.open(self.CAM_NUM)  # 检查相机状态
            if flag == False:  # 相机打开失败提示
                msg = QtWidgets.QMessageBox.warning(self.centralwidget, u"Warning",
                                                    u"请检测相机与电脑是否连接正确！ ",
                                                    buttons=QtWidgets.QMessageBox.Ok,
                                                    defaultButton=QtWidgets.QMessageBox.Ok)
            else:
                # 准备运行识别程序
                QtWidgets.QApplication.processEvents()
                self.label_face.setText('正在启动识别系统...\n\nleading')
                # 新建对象
                self.emotion_model = Emotion_Rec(self.model_path)
                QtWidgets.QApplication.processEvents()
                # 打开定时器
                self.timer_camera.start(30)
        else:
            # 定时器未开启，界面回复初始状态
            self.timer_camera.stop()
            self.cap.release()
            self.label_face.clear()
            gif = QMovie(':/newPrefix/images_test/scan.gif')
            self.label_face.setMovie(gif)
            gif.start()
            self.label_outputResult.clear()
            self.label_outputResult.setStyleSheet("border-image: url(:/newPrefix/images_test/ini.png);")

            self.label_scanResult.setText('None')

    def show_camera(self):
        # 定时器槽函数，每隔一段时间执行
        flag, self.image = self.cap.read()  # 获取画面
        self.image = cv2.flip(self.image, 1)  # 左右翻转

        tmp = open('slice.png', 'wb')
        tmp.write(b64decode(bgImg))
        tmp.close()
        canvas = cv2.imread('slice.png')  # 用于数据显示的背景图片
        remove('slice.png')

        # 使用模型预测
        result = self.emotion_model.run(self.image, canvas, self.label_face, self.label_outputResult)
        self.logFile = '[' + self.timePlay + ']' + str(self.emotion_model.preds)
        # self.logFile=str(self.emotion_model.preds)  #完全可以的呀
        # print(self.timePlay)
        # print(self.logFile)
        # print(self.emotion_model.preds)
        logging.info(self.logFile)
        # 在界面显示结果
        if result != 'happy':
            result='请开心一些'
            self.label_scanResult.setText(result)
        else:

            result='祝您开心每一天~~~'
            self.label_scanResult.setText(result)
            self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = emo()
    w.show()
    sys.exit(app.exec_())
