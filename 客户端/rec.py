from PyQt5 import QtCore, QtGui, QtWidgets


import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import socket
class recc(QWidget):
    def __init__(self, parent=None):
        super(recc, self).__init__()
        self.setObjectName("漂流瓶bottle")
        Form=self
        Form.resize(540, 270)
        Form.setStyleSheet("")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 541, 271))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

