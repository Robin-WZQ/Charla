# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gamepage.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pp

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
import os
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
from Global import globalmanager
class gp(QWidget):
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter8 = QPainter(self)
        if globalmanager.flag_zt==1:
            pixmap8 = QPixmap("背景_6.jpg")
        else:
            pixmap8 = QPixmap("背景_06.jpg")
        painter8.drawPixmap(self.rect(), pixmap8)
    def __init__(self):
        super(gp, self).__init__()
        Form=self
        Form.resize(550, 378)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 61, 61))
        #self.pushButton.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 20, 61, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 20, 61, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 20, 61, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(380, 20, 61, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(470, 20, 61, 61))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 100, 61, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(110, 100, 61, 61))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(200, 100, 61, 61))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(290, 100, 61, 61))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(380, 100, 61, 61))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(470, 100, 61, 61))
        self.pushButton_12.setObjectName("pushButton_12")

        self.pushButton_12.setStyleSheet("border-image: url(:/photo/3.png);")

        self.pushButton_13 = QtWidgets.QPushButton(Form)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 190, 61, 61))
        self.pushButton_13.setText('扫雷')
        self.pushButton_13.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(Form)
        self.pushButton_14.setGeometry(QtCore.QRect(110, 190, 61, 61))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(Form)
        self.pushButton_15.setGeometry(QtCore.QRect(200, 190, 61, 61))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(Form)
        self.pushButton_16.setGeometry(QtCore.QRect(290, 190, 61, 61))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(Form)
        self.pushButton_17.setGeometry(QtCore.QRect(380, 190, 61, 61))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_18 = QtWidgets.QPushButton(Form)
        self.pushButton_18.setGeometry(QtCore.QRect(470, 190, 61, 61))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_19 = QtWidgets.QPushButton(Form)
        self.pushButton_19.setGeometry(QtCore.QRect(20, 280, 61, 61))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_20 = QtWidgets.QPushButton(Form)
        self.pushButton_20.setGeometry(QtCore.QRect(110, 280, 61, 61))
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_20.setStyleSheet("border-image: url(:/photo/3.png);")
        self.pushButton_21 = QtWidgets.QPushButton(Form)
        self.pushButton_21.setGeometry(QtCore.QRect(200, 280, 61, 61))
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(Form)
        self.pushButton_22.setGeometry(QtCore.QRect(290, 280, 61, 61))
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(Form)
        self.pushButton_23.setGeometry(QtCore.QRect(380, 280, 61, 61))
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(Form)
        self.pushButton_24.setGeometry(QtCore.QRect(470, 280, 61, 61))
        self.pushButton_24.setObjectName("pushButton_24")

        self.pushButton.clicked.connect(lambda: self.sg1())
        self.pushButton_2.clicked.connect(lambda: self.sg2())
        self.pushButton_3.clicked.connect(lambda: self.sg3())
        self.pushButton_4.clicked.connect(lambda: self.sg4())
        self.pushButton_5.clicked.connect(lambda: self.sg5())
        self.pushButton_6.clicked.connect(lambda: self.sg6())
        self.pushButton_7.clicked.connect(lambda: self.sg7())
        self.pushButton_8.clicked.connect(lambda: self.sg8())
        self.pushButton_9.clicked.connect(lambda: self.sg9())
        self.pushButton_10.clicked.connect(lambda: self.sg10())
        self.pushButton_11.clicked.connect(lambda: self.sg11())
        self.pushButton_12.clicked.connect(lambda: self.sg12())
        self.pushButton_13.clicked.connect(lambda: self.sg13())
        self.pushButton_14.clicked.connect(lambda: self.sg14())
        self.pushButton_15.clicked.connect(lambda: self.sg15())
        self.pushButton_16.clicked.connect(lambda: self.sg16())
        self.pushButton_17.clicked.connect(lambda: self.sg17())
        self.pushButton_18.clicked.connect(lambda: self.sg18())
        self.pushButton_19.clicked.connect(lambda: self.sg19())
        self.pushButton_20.clicked.connect(lambda: self.sg20())
        self.pushButton_21.clicked.connect(lambda: self.sg21())
        self.pushButton_22.clicked.connect(lambda: self.sg22())
        self.pushButton_23.clicked.connect(lambda: self.sg23())
        self.pushButton_24.clicked.connect(lambda: self.sg24())

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "game!"))
        if globalmanager.flag_zt==1:
            self.pushButton.setText(_translate("Form", "蚂蚁"))
            self.pushButton.setStyleSheet("QPushButton{color:white}"
                                          "QPushButton{background-color:rgba(87,97,150,150)}"
                                          "QPushButton{border:0px}"
                                          "QPushButton{border-radius:5px}"
                                          "QPushButton{padding:2px 4px}"
                                          "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_2.setText(_translate("Form", "百吉饼"))
            self.pushButton_2.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_3.setText(_translate("Form", "反弹"))
            self.pushButton_3.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_4.setText(_translate("Form", "加农\n 大炮 "))
            self.pushButton_4.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_5.setText(_translate("Form", "五子棋"))
            self.pushButton_5.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_6.setText(_translate("Form", "加密"))
            self.pushButton_6.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_7.setText(_translate("Form", "fidget"))
            self.pushButton_7.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_8.setText(_translate("Form", "别撞\n黑点"))
            self.pushButton_8.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_9.setText(_translate("Form", "猜数字"))
            self.pushButton_9.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(87,97,150,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_10.setText(_translate("Form", "生活"))
            self.pushButton_10.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_11.setText(_translate("Form", "迷宫"))
            self.pushButton_11.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_12.setText(_translate("Form", "记忆\n数字"))
            self.pushButton_12.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_13.setText(_translate("Form", "扫雷"))
            self.pushButton_13.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_14.setText(_translate("Form", "吃豆子"))
            self.pushButton_14.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_15.setText(_translate("Form", "画图"))
            self.pushButton_15.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_16.setText(_translate("Form", "挡球"))
            self.pushButton_16.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_17.setText(_translate("Form", "记忆\n图象"))
            self.pushButton_17.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_18.setText(_translate("Form", "贪吃蛇"))
            self.pushButton_18.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_19.setText(_translate("Form", "吃豆子"))
            self.pushButton_19.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_20.setText(_translate("Form", "井字棋"))
            self.pushButton_20.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_21.setText(_translate("Form", "数字\n华容道"))
            self.pushButton_21.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_22.setText(_translate("Form", "井字棋"))
            self.pushButton_22.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_23.setText(_translate("Form", "特隆"))
            self.pushButton_23.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_24.setText(_translate("Form", "安装\n游戏"))
            self.pushButton_24.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(87,97,150,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
        else:
            self.pushButton.setText(_translate("Form", "蚂蚁"))
            self.pushButton.setStyleSheet("QPushButton{color:white}"
                                          "QPushButton{background-color:rgba(94,148,98,150)}"
                                          "QPushButton{border:0px}"
                                          "QPushButton{border-radius:5px}"
                                          "QPushButton{padding:2px 4px}"
                                          "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_2.setText(_translate("Form", "百吉饼"))
            self.pushButton_2.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_3.setText(_translate("Form", "反弹"))
            self.pushButton_3.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_4.setText(_translate("Form", "加农\n 大炮 "))
            self.pushButton_4.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_5.setText(_translate("Form", "五子棋"))
            self.pushButton_5.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_6.setText(_translate("Form", "加密"))
            self.pushButton_6.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_7.setText(_translate("Form", "fidget"))
            self.pushButton_7.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_8.setText(_translate("Form", "别撞\n黑点"))
            self.pushButton_8.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_9.setText(_translate("Form", "猜数字"))
            self.pushButton_9.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{background-color:rgba(94,148,98,150)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            "QPushButton{padding:2px 4px}"
                                            "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_10.setText(_translate("Form", "生活"))
            self.pushButton_10.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_11.setText(_translate("Form", "迷宫"))
            self.pushButton_11.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_12.setText(_translate("Form", "记忆\n数字"))
            self.pushButton_12.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_13.setText(_translate("Form", "扫雷"))
            self.pushButton_13.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_14.setText(_translate("Form", "吃豆子"))
            self.pushButton_14.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_15.setText(_translate("Form", "画图"))
            self.pushButton_15.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_16.setText(_translate("Form", "挡球"))
            self.pushButton_16.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_17.setText(_translate("Form", "记忆\n图象"))
            self.pushButton_17.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_18.setText(_translate("Form", "贪吃蛇"))
            self.pushButton_18.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_19.setText(_translate("Form", "吃豆子"))
            self.pushButton_19.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_20.setText(_translate("Form", "井字棋"))
            self.pushButton_20.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_21.setText(_translate("Form", "数字\n华容道"))
            self.pushButton_21.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_22.setText(_translate("Form", "井字棋"))
            self.pushButton_22.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_23.setText(_translate("Form", "特隆"))
            self.pushButton_23.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")
            self.pushButton_24.setText(_translate("Form", "安装\n游戏"))
            self.pushButton_24.setStyleSheet("QPushButton{color:white}"
                                             "QPushButton{background-color:rgba(94,148,98,150)}"
                                             "QPushButton{border:0px}"
                                             "QPushButton{border-radius:5px}"
                                             "QPushButton{padding:2px 4px}"
                                             "QPushButton{font:11pt\"幼圆\"}")

    def sg1(self):
        cmd = "python  -m freegames.ant"
        val = os.system(cmd)
        print(val)

    def sg2(self):
        cmd = "python  -m freegames.bagels"
        val = os.system(cmd)
        print(val)

    def sg3(self):
        cmd = "python  -m freegames.bounce "
        val = os.system(cmd)
        print(val)

    def sg4(self):
        cmd = "python  -m freegames.cannon"
        val = os.system(cmd)
        print(val)

    def sg5(self):
        cmd = "python  -m freegames.connect"
        val = os.system(cmd)
        print(val)

    def sg6(self):
        cmd = "python  -m freegames.crypto"
        val = os.system(cmd)
        print(val)

    def sg7(self):
        cmd = "python  -m freegames.fidget "
        val = os.system(cmd)
        print(val)

    def sg8(self):
        cmd = "python  -m freegames.flappy"
        val = os.system(cmd)
        print(val)

    def sg9(self):
        cmd = "python  -m freegames.guess"
        val = os.system(cmd)
        print(val)

    def sg10(self):
        cmd = "python  -m freegames.life"
        val = os.system(cmd)
        print(val)

    def sg11(self):
        cmd = "python  -m freegames.maze "
        val = os.system(cmd)
        print(val)

    def sg12(self):
        cmd = "python  -m freegames.memory"
        val = os.system(cmd)
        print(val)

    def sg13(self):
        cmd = "python  -m freegames.minesweeper"
        val = os.system(cmd)
        print(val)

    def sg14(self):
        cmd = "python  -m freegames.pacman"
        val = os.system(cmd)
        print(val)

    def sg15(self):
        cmd = "python  -m freegames.paint"
        val = os.system(cmd)
        print(val)

    def sg16(self):
        cmd = "python  -m freegames.pong "
        val = os.system(cmd)
        print(val)

    def sg17(self):
        cmd = "python  -m freegames.simonsays"
        val = os.system(cmd)
        print(val)

    def sg18(self):
        cmd = "python  -m freegames.snake"
        val = os.system(cmd)
        print(val)

    def sg19(self):
        cmd = "python  -m freegames.pacman"
        val = os.system(cmd)
        print(val)

    def sg20(self):
        cmd = "python  -m freegames.tictactoe"
        val = os.system(cmd)
        print(val)

    def sg21(self):
        cmd = "python  -m freegames.tiles "
        val = os.system(cmd)
        print(val)

    def sg22(self):
        cmd = "python  -m freegames.tron "
        val = os.system(cmd)
        print(val)

    def sg23(self):
        cmd = "python  -m freegames.tron"
        val = os.system(cmd)
        print(val)

    def sg24(self):
        cmd = 'pip install freegames'
        val = os.system(cmd)

import sys
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    globalmanager.set_value1(2)
    ui=gp()
    ui.show()

    sys.exit(app.exec_())