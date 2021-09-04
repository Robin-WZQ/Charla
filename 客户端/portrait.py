from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, \
    QPushButton, QLineEdit, QMenuBar, QStatusBar,QDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import QPalette, QBrush, QPixmap, QPainter
from Global import globalmanager

class por(QWidget):
    def paintEvent(self, a1: QtGui.QPaintEvent) -> None:
        painter2 = QPainter(self)
        painter2.setBrush(Qt.black)
        painter2.drawRect(self.rect())


    def __init__(self, parent=None):
        super(por, self).__init__(parent)
        self.setWindowTitle('更换头像')
        self.setGeometry(700, 400, 340, 340)

        self.tx1 =QtWidgets.QPushButton(self)
        self.tx1.setGeometry(QtCore.QRect(10, 10, 100, 100))
        self.tx1.setStyleSheet("border-image:url(tx1.jpg)")


        self.tx2 = QtWidgets.QPushButton(self)
        self.tx2.setGeometry(QtCore.QRect(120, 10, 100, 100))
        self.tx2.setStyleSheet("border-image:url(tx2.jpg)")

        self.tx3 = QtWidgets.QPushButton(self)
        self.tx3.setGeometry(QtCore.QRect(230, 10, 100, 100))
        self.tx3.setStyleSheet("border-image:url(tx3.jpg)")

        self.tx4 =QtWidgets.QPushButton(self)
        self.tx4.setGeometry(QtCore.QRect(10, 120, 100, 100))
        self.tx4.setStyleSheet("border-image:url(tx4.jpg)")

        self.tx5 = QtWidgets.QPushButton(self)
        self.tx5.setGeometry(QtCore.QRect(120, 120, 100, 100))
        self.tx5.setStyleSheet("border-image:url(tx5.jpg)")

        self.tx6 = QtWidgets.QPushButton(self)
        self.tx6.setGeometry(QtCore.QRect(230, 120, 100, 100))
        self.tx6.setStyleSheet("border-image:url(tx6.jpg)")

        self.tx7 = QtWidgets.QPushButton(self)
        self.tx7.setGeometry(QtCore.QRect(10, 230, 100, 100))
        self.tx7.setStyleSheet("border-image:url(tx7.jpg)")

        self.tx8 = QtWidgets.QPushButton(self)
        self.tx8.setGeometry(QtCore.QRect(120, 230, 100, 100))
        self.tx8.setStyleSheet("border-image:url(tx8.jpg)")

        self.tx9 = QtWidgets.QPushButton(self)
        self.tx9.setGeometry(QtCore.QRect(230, 230, 100, 100))
        self.tx9.setStyleSheet("border-image:url(tx9.jpg)")

import sys
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow=QtWidgets.QMainWindow()
    ui=por()
    ui.show()
    sys.exit(app.exec_())
    print(flag_tx)