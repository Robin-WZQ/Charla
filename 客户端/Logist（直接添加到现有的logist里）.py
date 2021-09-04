from add_group import ag
from information_1 import infor
from login_1 import log
from register_1 import reg
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow
from functools import partial
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from portrait import por
from theme import theme
from Global import globalmanager

def theme_1():
    theme1.close()
    globalmanager.set_value1(1)
    log1.repaint()

def theme_2():
    theme1.close()
    globalmanager.set_value1(2)
    print(globalmanager.flag_zt)
    log1.repaint()

def portrait_1():
    reg1.close()
    por1.close()
    globalmanager.set_value2(1)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_2():
    reg1.close()
    por1.close()
    globalmanager.set_value2(2)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_3():
    reg1.close()
    por1.close()
    globalmanager.set_value2(3)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_4():
    reg1.close()
    por1.close()
    globalmanager.set_value2(4)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_5():
    reg1.close()
    por1.close()
    globalmanager.set_value2(5)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_6():
    reg1.close()
    por1.close()
    globalmanager.set_value2(6)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_7():
    reg1.close()
    por1.close()
    globalmanager.set_value2(7)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_8():
    reg1.close()
    por1.close()
    globalmanager.set_value2(8)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()
def portrait_9():
    reg1.close()
    por1.close()
    globalmanager.set_value2(9)
    print(globalmanager.flag_tx)
    reg2=reg()
    reg2.show()

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()

    log1=log()

    reg1=reg()


    #更换皮肤和主题

    por1=por()
    theme1=theme()
    #########################
    log1.login_loginBtn.clicked.connect(lambda: infor1.show() )
    log1.login_signBtn.clicked.connect(lambda: reg1.show())





    reg1.register_picture.clicked.connect(lambda :por1.show())
    log1.login_theme.clicked.connect(lambda :theme1.show())
    theme1.blue.clicked.connect(theme_1)
    theme1.green.clicked.connect(theme_2)
    por1.tx1.clicked.connect(portrait_1)
    por1.tx2.clicked.connect(portrait_2)
    por1.tx3.clicked.connect(portrait_3)
    por1.tx4.clicked.connect(portrait_4)
    por1.tx5.clicked.connect(portrait_5)
    por1.tx6.clicked.connect(portrait_6)
    por1.tx7.clicked.connect(portrait_7)
    por1.tx8.clicked.connect(portrait_8)
    por1.tx9.clicked.connect(portrait_9)

    infor1 = infor()
    infor1.group_btn.clicked.connect(lambda: ag1.show())
    ag1 = ag()
    log1.show()

    print(globalmanager.flag_zt)
    sys.exit(app.exec_())

