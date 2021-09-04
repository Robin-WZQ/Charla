from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QPushButton, QLineEdit, QMenuBar, QStatusBar,QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
import portrait
from Global import globalmanager

class reg(QWidget):
    #self.flag = por.flag_tx
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter1 = QPainter(self)
        if globalmanager.flag_zt==1:
            pixmap1 = QPixmap("背景_1.jpg")
        else:
            pixmap1 = QPixmap("背景_01.jpg")
        painter1.drawPixmap(self.rect(), pixmap1)
    def __init__(self, parent=None):
        super(reg, self).__init__(parent)
        self.setWindowTitle('注册')
        self.setGeometry(300, 200, 540, 720)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(100, 60, 108, 30))
        self.label.setStyleSheet("font: 15pt \"幼圆\";"
                                 )
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(100, 120, 54, 30))
        self.label_2.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(100, 180, 54, 30))
        self.label_3.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(100, 240, 54,30))
        self.label_4.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(100, 300, 54, 30))
        self.label_5.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(100, 420, 110, 30))
        self.label_6.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(100, 360, 54, 30))
        self.label_7.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(100, 480, 140, 30))
        self.label_8.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(100, 540, 80, 30))
        self.label_9.setStyleSheet("font: 15pt \"幼圆\";")
        self.label_9.setObjectName("label_9")

        self.register_ask = QtWidgets.QComboBox(self)
        self.register_ask.setGeometry(QtCore.QRect(220, 480, 130, 30))
        self.register_ask.setStyleSheet("font: 13pt \"幼圆\";"

                                        )
        self.register_ask.setObjectName("register_ask")
        self.register_ask.addItem("")
        self.register_ask.addItem("")
        self.register_ask.addItem("")
        self.register_ask.setItemText(0, "您的生日")
        self.register_ask.setItemText(1,"母亲姓名")
        self.register_ask.setItemText(2, "父亲姓名")

        self.register_ans = QtWidgets.QLineEdit(self)
        self.register_ans.setGeometry(QtCore.QRect(220, 540, 200, 30))
        self.register_ans.setStyleSheet("font: 13pt \"幼圆\";"
                                        )
        self.register_ans.setObjectName("register_ans")

        self.label_8.setText( "密保问题")
        self.label_9.setText( "答案")

        self.register_conBtn = QtWidgets.QPushButton(self)
        self.register_conBtn.setGeometry(QtCore.QRect(100, 600, 100, 50))
        if globalmanager.flag_zt==1:
            self.register_conBtn.setStyleSheet("QPushButton{color:white}"
                                           "QPushButton{background-color:#000115}"
                                           "QPushButton{border:0px}"
                                           "QPushButton{border-radius:5px}"
                                           "QPushButton{padding:2px 4px}"
                                           "QPushButton{font:15pt\"幼圆\"}")
        else:
            self.register_conBtn.setStyleSheet("QPushButton{color:white}"
                                               "QPushButton{background-color:#375033}"
                                               "QPushButton{border:0px}"
                                               "QPushButton{border-radius:5px}"
                                               "QPushButton{padding:2px 4px}"
                                               "QPushButton{font:15pt\"幼圆\"}")
        self.register_conBtn.setObjectName("register_conBtn")

        self.register_canBtn = QtWidgets.QPushButton(self)
        self.register_canBtn.setGeometry(QtCore.QRect(350, 600, 100,50))
        if globalmanager.flag_zt==1:
            self.register_canBtn.setStyleSheet("QPushButton{color:white}"
                                           "QPushButton{background-color:#000115}"
                                           "QPushButton{border:0px}"
                                           "QPushButton{border-radius:5px}"
                                           "QPushButton{padding:2px 4px}"
                                           "QPushButton{font:15pt\"幼圆\"}")
        else:
            self.register_canBtn.setStyleSheet("QPushButton{color:white}"
                                               "QPushButton{background-color:#375033}"
                                               "QPushButton{border:0px}"
                                               "QPushButton{border-radius:5px}"
                                               "QPushButton{padding:2px 4px}"
                                               "QPushButton{font:15pt\"幼圆\"}")
        self.register_canBtn.setObjectName("register_canBtn")

        self.register_name = QtWidgets.QLineEdit(self)
        self.register_name.setGeometry(QtCore.QRect(220, 60, 100, 30))
        self.register_name.setStyleSheet("font: 13pt \"幼圆\";")
        self.register_name.setObjectName("register_name")
        self.register_num = QtWidgets.QLineEdit(self)
        self.register_num.setGeometry(QtCore.QRect(220, 180, 200, 30))
        self.register_num.setStyleSheet("font: 13pt \"幼圆\";")
        self.register_num.setObjectName("register_num")
        self.register_tel = QtWidgets.QLineEdit(self)
        self.register_tel.setGeometry(QtCore.QRect(220, 240, 200, 30))
        self.register_tel.setStyleSheet("font: 13pt \"幼圆\";")
        self.register_tel.setObjectName("register_tel")
        self.register_email = QtWidgets.QLineEdit(self)
        self.register_email.setGeometry(QtCore.QRect(220, 300, 200, 30))
        self.register_email.setStyleSheet("font: 13pt \"幼圆\";")
        self.register_email.setObjectName("register_email")
        self.register_pwd = QtWidgets.QLineEdit(self)
        self.register_pwd.setGeometry(QtCore.QRect(220, 360, 200, 30))
        self.register_pwd.setStyleSheet("font: 13pt \"幼圆\";")
        self.register_pwd.setObjectName("register_pwd")
        self.register_repwd = QtWidgets.QLineEdit(self)
        self.register_repwd.setGeometry(QtCore.QRect(220, 420, 200, 30))
        self.register_repwd.setStyleSheet("font: 13pt \"幼圆\";")
        self.register_repwd.setObjectName("register_repwd")

        self.register_dep = QtWidgets.QComboBox(self)
        self.register_dep.setGeometry(QtCore.QRect(220, 120, 100, 30))
        self.register_dep.setStyleSheet("font: 14pt \"幼圆\";")
        self.register_dep.setObjectName("register_dep")
        self.register_dep.addItem("")
        self.register_dep.addItem("")
        self.register_dep.addItem("")
        self.register_dep.addItem("")
        self.register_dep.addItem("")

        self.register_picture = QtWidgets.QPushButton(self)
        self.register_picture.setGeometry(QtCore.QRect(350, 40, 120, 120))

        if globalmanager.flag_tx == 1:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx1.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 2:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx2.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 3:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx3.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 4:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx4.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 5:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx5.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 6:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx6.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 7:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx7.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 8:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx8.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        elif globalmanager.flag_tx == 9:
            self.register_picture.setStyleSheet("QPushButton{color:white}"
                                                "QPushButton{border-image:url(tx9.jpg)}"
                                                "QPushButton{border:0px}"
                                                "QPushButton{border-radius:5px}"
                                                )
        self.register_picture.setStyleSheet("QPushButton{color:white}"
                                            "QPushButton{border-image:url(tx01.jpg)}"
                                            "QPushButton{border:0px}"
                                            "QPushButton{border-radius:5px}"
                                            )

        self.register_confirm = QtWidgets.QFrame(self)
        self.register_confirm.setGeometry(QtCore.QRect(430, 420, 30, 30))
        self.register_confirm.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_confirm.setFrameShadow(QtWidgets.QFrame.Raised)
        """if globalmanager.flag_zt == 1:
            self.register_confirm.setStyleSheet("border-image:url(图标1.jpg)")
        else:
            self.register_confirm.setStyleSheet("border-image:url(图标2.jpg)")"""


        self.label.setText("姓名")
        self.label_2.setText("部门")
        self.label_3.setText("工号")
        self.label_4.setText("电话")
        self.label_5.setText( "邮箱")
        self.label_6.setText( "确认密码")
        self.label_7.setText( "密码")
        self.register_conBtn.setText( "确认")
        self.register_canBtn.setText( "取消")
        self.register_pwd.setPlaceholderText("请勿输入“；”")
        self.register_dep.setItemText(0,"开发部")
        self.register_dep.setItemText(1, "外勤部")
        self.register_dep.setItemText(2, "人力部")
        self.register_dep.setItemText(3, "设计部")
        self.register_dep.setItemText(4, "运营部")

        #self.register_canBtn.clicked.connect(lambda :self.close())

import sys
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    globalmanager.set_value1(1)

    ui=reg()
    ui.show()
    sys.exit(app.exec_())
