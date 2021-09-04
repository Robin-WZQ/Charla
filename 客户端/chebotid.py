
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
#import pp
from PyQt5.Qt import *
# from PyQt5.QtGui import QIcon ,  QBrush , QColor
# from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtGui, QtWidgets


class botid(QWidget):
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter10 = QPainter(self)
        pixmap10 = QPixmap("bottle_1.jpg")
        painter10.drawPixmap(self.rect(), pixmap10)
    def __init__(self, parent=None):
        super(botid, self).__init__(parent)
        Form=self
        self.setObjectName("添加好友")
        self.resize(418, 411)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(60, 40, 301, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("money.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 161, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("font: 11pt \"幼圆\";")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "添加好友"))
        self.label_2.setText(_translate("Form", "付款后加添好友~~~~"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    bot1=botid()
    bot1.show()
    sys.exit(app.exec_())
