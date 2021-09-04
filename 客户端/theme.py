#!/usr/bin/env python3


import sys
from PyQt5.QtWidgets import *


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
#import pp
from PyQt5.Qt import *
from game import gp
# from PyQt5.QtGui import QIcon ,  QBrush , QColor
# from PyQt5.QtCore import Qt
from Global import globalmanager

class  theme(QWidget):
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter3 = QPainter(self)
        if globalmanager.flag_zt==1:
            pixmap3 = QPixmap("蓝色背景.jpg")
        else:
            pixmap3 = QPixmap("绿色背景.jpg")
        painter3.drawPixmap(self.rect(), pixmap3)

    def theme_1(self):
        globalmanager.flag_zt=1
        self.close()
    def theme_2(self):
        globalmanager.flag_zt=2
        self.close()

    def __init__(self, parent=None):
        super(theme, self).__init__(parent)

        self.setGeometry(300, 200, 720, 540)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(250, 60, 200, 50))
        self.label.setObjectName("label")

        self.label.setStyleSheet("QLabel{color:white}"
                                       "QLabel:hover{color:blue}"
                                       "QLabel{background-color:None}"
                                       "QLabel{border:0px}"
                                       "QLabel{border-radius:20px}"
                                       "QLabel{padding:2px 4px}"
                                       "QLabel{font:20pt\"幼圆\"}")
        self.label.setText("更换主题")

        self.blue = QtWidgets.QPushButton(self)
        self.blue.setGeometry(QtCore.QRect(0, 200, 400, 200))
        self.blue.setStyleSheet("QPushButton{color:white}"
                                 "QPushButton:hover{color:blue}"
                                 "QPushButton{background-color:None}"
                                 "QPushButton{border:0px}"
                                 "QPushButton{border-radius:20px}"
                                 "QPushButton{padding:2px 4px}"
                                 "QPushButton{font:20pt\"幼圆\"}")
        self.blue.setText("月光水岸\nMoonlight Bay")
        #self.blue.clicked.connect(self.theme_1)

        self.green = QtWidgets.QPushButton(self)
        self.green.setGeometry(QtCore.QRect(320, 200, 400, 200))
        self.green.setStyleSheet("QPushButton{color:white}"
                                 "QPushButton:hover{color:blue}"
                                 "QPushButton{background-color:None}"
                                 "QPushButton{border:0px}"
                                 "QPushButton{border-radius:20px}"
                                 "QPushButton{padding:2px 4px}"
                                 "QPushButton{font:20pt\"幼圆\"}")
        self.green.setText("春野\nOne day in Spring")
        #self.green.clicked.connect(self.theme_2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    theme1 = theme()
    theme1.show()
    sys.exit(app.exec_())
