from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QPushButton, QLineEdit, QMenuBar, QStatusBar,QDialog
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from functools import partial
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Global import globalmanager


class log(QWidget):

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        if globalmanager.flag_zt==1:
            pixmap = QPixmap("login1.jpg")
        else :
            pixmap = QPixmap("login2.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    def __init__(self, parent=None):
        # super这个用法是调用父类的构造函数
        # parent=None表示默认没有父Widget，如果指定父亲Widget，则调用之
        super(log, self).__init__(parent)
        self.setWindowTitle('登录')

        #self.setStyleSheet("background-image:url(login1.jpg)")
        self.setGeometry(800, 350, 400, 400)
        #self.setStyleSheet("background-color:green")

       # MainWindow.setStyleSheet('background - image: url(imges / bc1.png)')

        self.login_usr = QLineEdit(self)
        self.login_usr.setGeometry(QRect(200, 70, 120, 20))
        self.login_usr.setInputMask("")
        self.login_usr.setText("")
        self.login_usr.setObjectName("login_usr")
        self.login_usr.setStyleSheet("font: 9pt \"幼圆\";"
                                     "border:none;"
                                     "background-color:rgba(255,255,255,180);"
                                     )
        self.login_pwd = QLineEdit(self)


        self.login_pwd.setGeometry(QRect(200, 152, 120, 20))
        self.login_pwd.setObjectName("login_pwd")
        self.login_pwd.setEchoMode(QLineEdit.Password)
        self.login_pwd.setStyleSheet("font: 9pt \"幼圆\";"
                                     "border:none;"
                                     "background-color:rgba(255,255,255,180);"
                                     )

        self.login_loginBtn = QtWidgets.QPushButton(self)
        self.login_loginBtn.setGeometry(QRect(70, 210, 72, 72))
        self.login_loginBtn.setStyleSheet("QPushButton{color:white}"
                                          "QPushButton:hover{color:blue}"
                                          "QPushButton{background-color:None}"
                                          "QPushButton{border:0px}"
                                          "QPushButton{border-radius:20px}"
                                          "QPushButton{padding:2px 4px}"
                                          "QPushButton{font:15pt\"幼圆\"}")
        self.login_loginBtn.setObjectName("login_loginBtn")


        self.login_signBtn = QtWidgets.QPushButton(self)
        self.login_signBtn.setGeometry(QtCore.QRect(260, 210, 72, 72))
        self.login_signBtn.setStyleSheet("QPushButton{color:white}"
                                         "QPushButton:hover{color:blue}"
                                         "QPushButton{background-color:None}"
                                         "QPushButton{border:0px}"
                                         "QPushButton{border-radius:20px}"
                                         "QPushButton{padding:2px 4px}"
                                         "QPushButton{font:15pt\"幼圆\"}")
        self.login_signBtn.setObjectName("login_signBtn")



        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 59, 59))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")




        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 39, 39))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")


        self.scrollAreaWidgetContents_5 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_5.setGeometry(QtCore.QRect(0, 0, 39, 39))
        self.scrollAreaWidgetContents_5.setObjectName("scrollAreaWidgetContents_5")
        self.login_forgetBtn = QtWidgets.QPushButton(self)
        self.login_forgetBtn.setGeometry(QtCore.QRect(160, 300, 91, 23))
        self.login_forgetBtn.setStyleSheet("QPushButton{color:white}"
                                           "QPushButton:hover{color:blue}"
                                           "QPushButton{background-color:None}"
                                           "QPushButton{border:0px}"
                                           # "QPushButton{border-radius:36px}"
                                           "QPushButton{padding:2px 4px}"
                                           "QPushButton{font:9pt\"幼圆\"}")
        self.login_forgetBtn.setAutoFillBackground(True)
        self.login_forgetBtn.setObjectName("login_forgetBtn")
        #_
     #   self.login_loginBtn.clicked.connect(self.close)
        #需要添加loginbtn的跳转，结合密码是否正确来做
        #_
        _translate = QtCore.QCoreApplication.translate
        self.login_usr.setToolTip(_translate("Dialog", "<html><head/><body><p>工号</p><p><br/></p></body></html>"))
        self.login_usr.setWhatsThis(_translate("Dialog", "<html><head/><body><p>工号</p></body></html>"))
        self.login_usr.setPlaceholderText(_translate("Dialog", "工号"))
        self.login_pwd.setToolTip(_translate("Dialog", "<html><head/><body><p>密码</p><p><br/></p></body></html>"))
        self.login_pwd.setWhatsThis(_translate("Dialog", "<html><head/><body><p>密码</p><p><br/></p></body></html>"))
        self.login_pwd.setPlaceholderText(_translate("Dialog", "密码"))
        self.login_loginBtn.setText(_translate("Dialog", "登录"))
        self.login_signBtn.setText(_translate("Dialog", "注册"))
        self.login_forgetBtn.setText(_translate("Dialog", "忘记密码?"))

        #设置主题
        self.login_theme = QtWidgets.QPushButton(self)
        self.login_theme.setGeometry(QtCore.QRect(340, 30, 50, 50))
        self.login_theme.setStyleSheet("QPushButton{color:white}"
                                          "QPushButton:hover{color:blue}"
                                          "QPushButton{background-color:None}"
                                          "QPushButton{border:0px}"
                                          "QPushButton{border-radius:20px}"
                                          "QPushButton{padding:2px 4px}"
                                          "QPushButton{font:10pt\"幼圆\"}")
        self.login_theme.setObjectName("login_loginBtn")
        self.login_theme.setText(_translate("Dialog", "设置"))
        self.login_theme.setObjectName("login_theme")






if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()

    log1=log()
    log1.show()
    sys.exit(app.exec_())


