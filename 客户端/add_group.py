import sys
import PyQt5

import sys
import cv2

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
from Global import globalmanager
class ag(QWidget):
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter4 = QPainter(self)
        if globalmanager.flag_zt == 1:
            pixmap4 = QPixmap("蓝色背景.jpg")
        else:
            pixmap4 = QPixmap("绿色背景.jpg")
        painter4.drawPixmap(self.rect(), pixmap4)
    def __init__(self):
        super(ag, self).__init__()
        #先定义
        #listwidget_1  是左侧的列表
        #listwidget_2  是右侧鹅列表
        self.setWindowTitle('发起群聊')
        self.setGeometry(770, 100, 760, 590)
        self.listwidget_1 = QtWidgets.QListWidget(self)
        self.listwidget_2 = QtWidgets.QListWidget(self)
        self.listwidget_1.setGeometry(QtCore.QRect(20, 30, 351, 471))
        self.listwidget_1.setStyleSheet("font: 11pt \"幼圆\";"
                                        "border:none;"
                                        "background-color:rgba(255,255,255,150);"
                                        )

        self.listwidget_1.setObjectName("listWidget")
        self.listwidget_2.setGeometry(QtCore.QRect(400, 30, 341, 471))
        self.listwidget_2.setStyleSheet("font: 11pt \"幼圆\";"
                                        "border:none;"
                                        "background-color:rgba(255,255,255,150);"
                                        )
        self.listwidget_2.setObjectName("listWidget_2")
        #按钮
        self.addfriend = QtWidgets.QPushButton(self)
        self.addfriend.setGeometry(QtCore.QRect(400, 515, 180, 41))
        self.addfriend.setStyleSheet(     "QPushButton{color:white}"
                                          "QPushButton:hover{color:blue}"
                                          "QPushButton{background-color:None}"
                                          "QPushButton{border:0px}"
                                          "QPushButton{border-radius:20px}"
                                          "QPushButton{padding:2px 4px}"
                                          "QPushButton{font:12pt\"幼圆\"}")
        self.addfriend.setObjectName("addgroup")
        self.addgroup = QtWidgets.QPushButton(self)
        self.addgroup.setGeometry(QtCore.QRect(640, 515, 100, 41))
        self.addgroup.setStyleSheet("QPushButton{color:white}"
                                     "QPushButton:hover{color:blue}"
                                     "QPushButton{background-color:None}"
                                     "QPushButton{border:0px}"
                                     "QPushButton{border-radius:20px}"
                                     "QPushButton{padding:2px 4px}"
                                     "QPushButton{font:12pt\"幼圆\"}")
        self.addgroup.setObjectName("addgroup")

        #加文字
        self.addfriend.setText("添加为常用联系人")
        self.addgroup.setText("发起群聊")

        #加图片
        #——————————————————————————————————————————————————————————————————————这里加获得当前在线信息
        # ——————————————————————————————————————————————————————————————————————这里加获得当前在线信息
        # ——————————————————————————————————————————————————————————————————————这里加获得当前在线信息
        # fff = ['[管理员]lt', 'a', 'b', 'c', '1', '2', '3', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
        #        '1']
        # for i in fff:
        #     item = QtWidgets.QListWidgetItem()

        #     icon = QtGui.QIcon()
        #     icon.addPixmap(QtGui.QPixmap("../pp/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #     item.setIcon(icon)
        #     item.setText(i)
        #     self.listwidget_1.addItem(item)
        # fff = ['a', 'b', 'c']
        # for i in fff:
        #     item = QtWidgets.QListWidgetItem()
        #     icon = QtGui.QIcon()
        #     icon.addPixmap(QtGui.QPixmap("../pp/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #     item.setIcon(icon)
        #     item.setText(i)
        #     self.listwidget_2.addItem(item)


        # #写槽函数
        # self.listwidget_1.doubleClicked.connect(lambda: self.change_func(self.listwidget_1))
        # self.listwidget_2.doubleClicked.connect(lambda: self.change_func(self.listwidget_2))


    # 槽函数，点击listwidget_1中的某一item，为listwidget_2添加item,点击listwidget_2中的某一item,去除该item
    # def change_func(self, listwidget):
    #     if listwidget == self.listwidget_1:
    #         item = QListWidgetItem(self.listwidget_1.currentItem())
    #         self.listwidget_2.addItem(item)
    #         print(item.text())
    #         print(self.listwidget_2.count())

    #     else:
    #         self.listwidget_2.takeItem(self.listwidget_2.currentRow())
    #         print(self.listwidget_2.count())

    # def S(self):
    #     self.show()
    # def D(self):
    #     self.close()


import sys
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=ag()
    sys.exit(app.exec_())