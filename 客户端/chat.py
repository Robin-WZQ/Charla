from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
#import pp
from PyQt5 import QtCore, QtGui, QtWidgets
#from module.items import *
import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import * 		# QSize
from Global import globalmanager
return_id=0
path=''
class  chat(QWidget):
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter8 = QPainter(self)
        if globalmanager.flag_zt==1:
            pixmap8 = QPixmap("蓝色背景.jpg")
        else:
            pixmap8 = QPixmap("绿色背景.jpg")
        painter8.drawPixmap(self.rect(), pixmap8)
    def __init__(self, parent=None):
        super( chat, self).__init__(parent)
        group=self
        group.setObjectName("group")
        group.resize(811, 680)
        self.id=72
        self.textEdit = QtWidgets.QTextEdit(group)
        self.textEdit.setGeometry(QtCore.QRect(10, 480, 601, 161))
        self.textEdit.setStyleSheet("font: 13pt \"幼圆\";"
                                    "border:none;"
                                    "background-color:rgba(255,255,255,170);"
                                    )
        self.textEdit.setObjectName("textEdit")
        self.send = QtWidgets.QPushButton(group)
        self.send.setGeometry(QtCore.QRect(520, 645, 93, 28))
        self.send.setStyleSheet("font: 12pt \"幼圆\";"
                                "border:none;"
                                "background-color:rgba(255,255,255);"
                                )
        self.send.setObjectName("send")

        self.closep = QtWidgets.QPushButton(group)
        self.closep.setGeometry(QtCore.QRect(390, 645, 93, 28))
        self.closep.setStyleSheet("font: 12pt \"幼圆\";"
                                "border:none;"
                                "background-color:rgba(255,255,255);"
                                )
        self.closep.setObjectName('closep')
        self.closep.setText("退出")
        #self.closep.clicked.connect(self.close)

        self.line = QtWidgets.QFrame(group)
        self.line.setGeometry(QtCore.QRect(610, 10, 20, 651))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(group)
        self.line_2.setGeometry(QtCore.QRect(200, 455, 401, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.textBrowser = QtWidgets.QTextBrowser(group)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 601, 441))
        self.textBrowser.setStyleSheet("font: 13pt \"幼圆\";"
                                       "border:none;"
                                       "background-color:rgba(255,255,255,170);"
                                       )
        self.textBrowser.setObjectName("textBrowser")
        self.emo = QtWidgets.QPushButton(group)
        self.emo.setGeometry(QtCore.QRect(10, 455, 41, 21))
        self.emo.setStyleSheet("font: 10pt \"幼圆\";"
                               "border:none;"
                               "background-color:rgba(255,255,255);"
                               )
        self.emo.setObjectName("emo")
        self.pap = QtWidgets.QPushButton(group)
        self.pap.setGeometry(QtCore.QRect(60, 455, 41, 21))
        self.pap.setStyleSheet("font: 10pt \"幼圆\";"
                               "border:none;"
                               "background-color:rgba(255,255,255);"
                               )
        self.pap.setObjectName("pap")
        self.dak = QtWidgets.QPushButton(group)
        self.dak.setGeometry(QtCore.QRect(160, 455, 41, 21))
        self.dak.setObjectName("emotion")
        self.dak.setToolTip('情感打卡')
        self.dak.setText('daka')
        self.dak.setStyleSheet("font: 10pt \"幼圆\";"
                            "border:none;"
                            "background-color:rgba(255,255,255);"
                            )

        self.line_3 = QtWidgets.QFrame(group)
        self.line_3.setGeometry(QtCore.QRect(620, 220, 191, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.adver1 = QtWidgets.QLabel(group)
        self.adver1.setGeometry(QtCore.QRect(630, 20, 171, 191))
        self.adver1.setStyleSheet("font: 10pt \"幼圆\";"
                               "border:none;"
                               "color:white;"
                               )
        self.adver1.setObjectName("adver1")
        self.adver2 = QtWidgets.QLabel(group)
        self.adver2.setGeometry(QtCore.QRect(630, 230, 171, 191))
        self.adver2.setStyleSheet("font: 10pt \"幼圆\";"
            "border:none;"
            "color:white;"
        )
        self.adver2.setObjectName("adver2")
        self.line_4 = QtWidgets.QFrame(group)
        self.line_4.setGeometry(QtCore.QRect(620, 420, 191, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.pushButton_4 = QtWidgets.QPushButton(group)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 455, 41, 21))
        self.pushButton_4.setStyleSheet("font: 10pt \"幼圆\";"
                                        "border:none;"
                                        "background-color:rgba(255,255,255);"
                                        )
        self.pushButton_4.setObjectName("pushButton_4")
        self.listwidget = QtWidgets.QListWidget(group)
        self.listwidget.setGeometry(QtCore.QRect(620, 430, 191, 231))
        self.listwidget.setStyleSheet("font: 13pt \"幼圆\";"
                                      "border:none;"
                                      "background-color:rgba(255,255,255,170);"
                                      )
        self.listwidget.setObjectName("listwidget")
        self.groupall = QtWidgets.QLabel(group)
        self.groupall.setGeometry(QtCore.QRect(620, 400, 121, 25))
        self.groupall.setStyleSheet("font: 10pt \"幼圆\";"
                                    "border:none;"
                                    "color:white;"
                                    )
        self.groupall.setObjectName("groupall")


        


        self.retranslateUi(group)
        QtCore.QMetaObject.connectSlotsByName(group)


        
        self.send.setToolTip('回车也可以发送消息哦~')
        self.listwidget.doubleClicked.connect(lambda :self.twog())
       # self.emo.clicked.connect(lambda :self.wa())

    def retranslateUi(self, group):
        _translate = QtCore.QCoreApplication.translate
        group.setWindowTitle(_translate("group", "一个群聊"))
        self.send.setText(_translate("group", "send"))
        self.emo.setText(_translate("group", "emo"))
        self.pap.setText(_translate("group", "pap"))
        self.adver1.setText(_translate("group", "广告招商"))
        self.adver2.setText(_translate("group", "广告招商"))
        self.pushButton_4.setText(_translate("group", "rec"))
        self.groupall.setText(_translate("group", "聊天用户"))
    
    def wa(self):
        box = QtWidgets.QMessageBox()
        box.warning(self, '提示', '还没开发')
    #####接口
    #回车和发送后回先发送到服务端，如果有图片就是一个符号，如果没有的话，就是另一个符号
    #接受到服务端的符号之后，先判断是自己还是别人，然后判断有没有图片。
    #有图片的话用   特殊符号把图片第几个隔开$$$$1$$$$
    #之后显示
    
    def twog(self):
        item = QListWidgetItem(self.listwidget.currentItem())
        print(item.text())
        ##打开单独聊天界面
from PyQt5.QtWidgets import QApplication, QTableWidget, QWidget, QHeaderView, QPushButton, QTableWidgetItem, QFrame
import sys
from PyQt5.QtGui import QBrush, QColor, QFont, QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
class emot(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(540,182)
        self.setWindowTitle('emo')
        self.table = QTableWidget(self)  # 创建空表格
        self.table.resize(540, 270)
        # self.table = QTableWidget(4,3,self)  #创建4行3列的表格
        self.table.setRowCount(6)  # 设置行数--不包括标题列
        self.table.setColumnCount(12)  # 设置列数
        self.table.setAlternatingRowColors(True)  # 行是否自动变色
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置列宽的适应方式
        s = self.table.columnCount()  # 返回列数
        QTableWidget.resizeRowsToContents(self.table)  # 设置行高与内容匹配"""
        self.table.horizontalHeader().setVisible(False)  # 水平表格头是否隐藏
        self.table.verticalHeader().setVisible(False)  #垂直表格头是否隐藏
        """path='E:/emopho/0.jpg'
        newItem = QTableWidgetItem(QIcon(path),"0")  # 创建表格项---图片项目
        self.table.setItem(0, 0, newItem)"""
        label = QLabel(self)
        label.setPixmap(QtGui.QPixmap("E:/emopho/0.jpg"))
        self.table.setCellWidget(0,0, label)
        for i in range(6):
            for j in range(12):
                label = QLabel(self)
                x=i*12+j
                label.setPixmap(QtGui.QPixmap("E:/emopho/"+str(x)+".jpg"))
                self.table.setCellWidget(i, j, label)
        #self.table.setFocusPolicy(Qt.NoFocus)
        # 重写选中背景
        #self.table.setStyleSheet("QTableWidget::item:selected{ background-color:skyblue}")
        self.table.cellPressed.connect(self.getPosContent)
    def getPosContent(self,row,col):
        self.id=int(row)*12+int(col)
        print( int(row)*12+int(col))
        global return_id
        return_id=self.id

        global path
        path = 'E:/emopho/' + str(return_id) + '.jpg>'
        path = '<img src=' + path
        print(path)
        self.close()
        """
        newItem = QTableWidgetItem(QIcon("./大象.png"), "大象")  # 创建表格项---图片项目
        # 参数2  描述
        self.table.setIconSize(QSize(100, 100))  # 设置图片大小
        newItem.setFlags(Qt.ItemIsEnabled)  # 用户点击表格时，图片被选中"""
        """self.table.setColumnWidth(2, 100)  # 设置指定列的列宽
        self.table.setRowHeight(2, 100)  # 设置指定行的行高"""
        """self.table.setItem(2, 2, newItem)  # 给指定单元格设置图片项

        # self.table.clear()  #清除所有数据--包括标题头
        self.table.clearContents()  # 清除所有数据--不包括标题头

        print(s)"""


import sys
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    globalmanager.set_value1(2)
    chat1=chat()
    emot1=emot()
    chat1.emo.clicked.connect(lambda :emot1.show())
    emot1.table.cellPressed.connect(lambda :chat1.textEdit.append(path))
    chat1.show()
    sys.exit(app.exec_())