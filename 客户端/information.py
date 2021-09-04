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

class  infor(QWidget):
    def paintEvent(self, a: QtGui.QPaintEvent) -> None:
        painter3 = QPainter(self)
        if globalmanager.flag_zt==1:
            pixmap3 = QPixmap("蓝色背景.jpg")
        else:
            pixmap3 = QPixmap("绿色背景.jpg")
        painter3.drawPixmap(self.rect(), pixmap3)
    def __init__(self, parent=None):
        super( infor, self).__init__(parent)
        self.setWindowTitle('个人信息information')
        self.setGeometry(QtCore.QRect(200, 100, 400, 800))

        self.namelabel=QtWidgets.QLabel(self)
        self.namelabel.setGeometry(QtCore.QRect(180, 50, 130, 20))
        self.namelabel.setObjectName('名字串')
        self.namelabel.setText('[开发部]李桐')
        self.namelabel.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:None}"
                                "QLabel{border:0px}"
                                "QLabel{border-radius:20px}"
                                "QLabel{padding:2px 4px}"
                                "QLabel{font:11pt\"幼圆\"}")

        self.namelabel1=QtWidgets.QLabel(self)
        self.namelabel1.setGeometry(QtCore.QRect(150, 80, 200, 40))
        self.namelabel1.setObjectName('串')
        self.namelabel1.setText('您还不是尊敬的vip、彩钻用户嗷~\n充值让您变强~')
        self.namelabel1.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:None}"
                                "QLabel{border:0px}"
                                "QLabel{border-radius:20px}"
                                "QLabel{padding:2px 4px}"
                                "QLabel{font:8pt\"幼圆\"}")


        self.photo = QtWidgets.QLabel(self)
        self.photo.setGeometry(QtCore.QRect(50, 10, 100, 100))
        self.photo.setObjectName("photo")
        self.photo.setText("TextLabel")
        # 必须放在这里
        if globalmanager.flag_tx==1:
            self.photo.setPixmap(QtGui.QPixmap("tx1.jpg"))
        elif globalmanager.flag_tx==2:
            self.photo.setPixmap(QtGui.QPixmap("tx2.jpg"))
        elif globalmanager.flag_tx==3:
            self.photo.setPixmap(QtGui.QPixmap("tx3.jpg"))
        elif globalmanager.flag_tx==4:
            self.photo.setPixmap(QtGui.QPixmap("tx4.jpg"))
        elif globalmanager.flag_tx==5:
            self.photo.setPixmap(QtGui.QPixmap("tx5.jpg"))
        elif globalmanager.flag_tx==6:
            self.photo.setPixmap(QtGui.QPixmap("tx6.jpg"))
        elif globalmanager.flag_tx==7:
            self.photo.setPixmap(QtGui.QPixmap("tx7.jpg"))
        elif globalmanager.flag_tx==8:
            self.photo.setPixmap(QtGui.QPixmap("tx8.jpg"))
        elif globalmanager.flag_tx==9:
            self.photo.setPixmap(QtGui.QPixmap("tx9.jpg"))

        self.game = QtWidgets.QToolButton(self)
        self.game.setGeometry(QtCore.QRect(205, 130, 100, 30))
        self.game.setStyleSheet("QToolButton{color:white}"
                                "QToolButton{background-color:None}"
                                "QToolButton{border:0px}"
                                "QToolButton{border-radius:20px}"
                                "QToolButton{padding:2px 4px}"
                                "QToolButton{font:11pt\"幼圆\"}")

        self.game.setObjectName("game")
        self.game.setText('去game快乐')


        self.addi=QPushButton(self)
        self.addi.setText('删除群聊')
        self.addi.setGeometry(QtCore.QRect(20, 130, 80, 30))
        #self.addi.setStyleSheet("font: 9pt \"幼圆\";")
        self.addi.setStyleSheet("QPushButton{color:white}"
                                          "QPushButton{background-color:None}"
                                          "QPushButton{border:0px}"
                                          "QPushButton{border-radius:20px}"
                                          "QPushButton{padding:2px 4px}"
                                          "QPushButton{font:11pt\"幼圆\"}")

        self.deli=QPushButton(self)
        self.deli.setGeometry(QtCore.QRect(115, 130, 80, 30))
        self.deli.setText('删除好友')
        self.deli.setStyleSheet("QPushButton{color:white}"
                                "QPushButton{background-color:None}"
                                "QPushButton{border:0px}"
                                "QPushButton{border-radius:20px}"
                                "QPushButton{padding:2px 4px}"
                                "QPushButton{font:11pt\"幼圆\"}")


        self.txti = QPushButton(self)
        self.txti.setGeometry(QtCore.QRect(305, 130, 80, 30))
        self.txti.setText('漂流瓶')
        self.txti.setStyleSheet("QPushButton{color:white}"
                                "QPushButton{background-color:None}"
                                "QPushButton{border:0px}"
                                "QPushButton{border-radius:20px}"
                                "QPushButton{padding:2px 4px}"
                                "QPushButton{font:11pt\"幼圆\"}")


        self.group_btn = QtWidgets.QPushButton(self)
        self.group_btn.setGeometry(QtCore.QRect(25, 600, 350, 28))
        self.group_btn.setObjectName("group_btn")
        self.group_btn.setText('没有想要联系的对象吗？点击这里发起聊天')
        self.group_btn.setStyleSheet("QPushButton{color:white}"
                                "QPushButton{background-color:None}"
                                "QPushButton{border:0px}"
                                "QPushButton{border-radius:20px}"
                                "QPushButton{padding:2px 4px}"
                                "QPushButton{font:11pt\"幼圆\"}")

        #self.addi.clicked.connect(self.addTreeNodeBtn)
        # self.deli.clicked.connect(self.delTreeNodeBtn)
        # self.txti.clicked.connect(self.delTreeNodeBtn)

        self.tree = QTreeWidget(self)
        self.tree.setGeometry(QtCore.QRect(20, 190, 360, 380))
        self.tree.setStyleSheet("font: 11pt \"幼圆\";"
                                "border:none;"
                                "background-color:rgba(255,255,255,170);"
                                )
        # 设置列数
        self.tree.setColumnCount(2)
        # 设置头的标题
        self.tree.setHeaderLabels(['分组', 'id'])

        self.root1 = QTreeWidgetItem(self.tree)
        self.root1.setText(0,'常用联系人id')
        self.root1.setText(1, '常用联系人')

        self.root2 = QTreeWidgetItem(self.tree)
        self.root2.setText(0,'常用群聊id' )
        self.root2.setText(1,'常用群聊' )
        """
        child1 = QTreeWidgetItem(root)
        child1.setText(0, 'child1')
        child1.setText(1, '1')

        child2 = QTreeWidgetItem(root)
        child2.setText(0, 'child2')
        child2.setText(1, '2')

        child3 = QTreeWidgetItem(root)
        child3.setText(0, 'child3')
        child3.setText(1, '3')

        child4 = QTreeWidgetItem(child3)
        child4.setText(0, 'child4')
        child4.setText(1, '4')

        child5 = QTreeWidgetItem(child3)
        child5.setText(0, 'child5')
        child5.setText(1, '5')
        """
        

     
        """ mainLayout = QVBoxLayout(self);
        mainLayout.addLayout(operatorLayout);
        mainLayout.addWidget(self.tree);
        self.setLayout(mainLayout)"""

    def onTreeClicked(self, qmodelindex):
        item = self.tree.currentItem()
        print("key=%s ,value=%s" % (item.text(0), item.text(1)))
    def item_click(self, item):
        #print (item, str(item.text()))
        print(item.text())
        # 添加跳转聊天页面
    def addTreeNodeBtn(self):
        print('--- addTreeNodeBtn ---')
        item = self.tree.currentItem()
        node = QTreeWidgetItem(item)
        node.setText(0, 'newNode')
        node.setText(1, '10')

    def updateTreeNodeBtn(self):
        print('--- updateTreeNodeBtn ---')
        item = self.tree.currentItem()
        item.setText(0, 'updateNode')
        item.setText(1, '20')

    def delTreeNodeBtn(self):
        print('--- delTreeNodeBtn ---')
        item = self.tree.currentItem()
        root = self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            (item.parent() or root).removeChild(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    infor1 = infor()
    globalmanager.set_value1(1)
    gp1 = gp()
    infor1.game.clicked.connect(lambda: gp1.show())
    infor1.game.clicked.connect(lambda:  infor1.close())
    infor1.show()
    sys.exit(app.exec_())

