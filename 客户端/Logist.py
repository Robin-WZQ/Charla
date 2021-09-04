from add_group import ag
from information import *
from login import log
from register import reg
from find import find
from find2 import find2
import warning
import tips
from chat import chat
from rec import recc
from tools import *
from game import gp
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QListWidget, QListWidgetItem, QHBoxLayout
from PyQt5.QtWidgets import QDialog, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import socket
from Global import globalmanager
from portrait import por
from theme import theme
import time
from datetime import datetime
from threading import Thread
import pp
from emotion import emo
from bottle import bot
import base64
import random
import camera
# import main
# import trainner
# import recognizer
from chebotid import botid
#————————————————————————————————————————————————————
emo1flag=0#——————————————————————————————————————————————————————
tempid = ''   #存储工号
temp_list = [] #临时列表,用于向服务端发起群聊申请
temp_constuser = {} #存储常用联系人，用于避免重复添加常用联系人
temp_groupid = ''#群聊id
flag = 0
clo = 0
templist=[]

filename=''
filepath=''

recfileflag=0
recfiletext=''
recfilelist = []
#与服务器建立通信

new_socket = socket.socket() #创建socket对象
ip = "10.195.54.156"
port = 12323              # 设置默认端口
new_socket.connect((ip,port))

return_id=0
path=''

def send_clock():
    global tempid
    global temp_groupid
    global clo
    #__________________
    global recfileflag
    #____________
    while True:
        time.sleep(0.5)
        global filename
        global filepath
        global emo1flag
        if filename!='':
            with open(filepath, 'rb')as f:
                print(1)
                buf = base64.b64encode(f.read())
                print(2)
                now = datetime.now()
                date_time = now.strftime("%Y-%m-%d-%H:%M:%S")
                a = 'D00001;["' + str(temp_groupid) + '","' + str(tempid) + '","' + filename + '","' + date_time + '"]'
                print(a)
                #a=str(a, encoding = "utf8")
                new_socket.sendall(str(a).encode(encoding='utf-8'))
                print(a)
                new_socket.send(buf)
                print(1)

                f.close()
            filename = ''
            filepath = ''
        elif recfileflag==1:
            recfileflag=0
            a = 'D00007' +";" +str(tempid) + ';' + str(temp_groupid)
            new_socket.sendall(str(a).encode(encoding='utf-8'))
        elif recfileflag==2:
            recfileflag = 0
            a = 'D00008' + ";" + str(tempid) + ';' + str(temp_groupid)+';'+str(recfiletext)
            new_socket.sendall(str(a).encode(encoding='utf-8'))


        elif emo1flag==1:
            now = datetime.now()  # current date and time
            date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
            a = ['我已经打卡啦~，每天都要快乐工作嗷', '开心工作每一天~', 'have a good day！']
            a = random.choice(a)
            x = "D00000" + ';' + tempid + ";" + date_time + ";" + a + ";" + temp_groupid
            new_socket.sendall(x.encode())
            emo1flag=0
        else:
            x = "E00000;"+tempid+";"+temp_groupid
            new_socket.sendall(x.encode("utf-8"))
            if clo == 1:
                clo=0
                break



def handle():
    #chat1.show()
    # chat1.closep.clicked.connect(closechat)
    print("正在与服务端建立稳定链接······")
    global flag
    global templist
    global clo
    Thread(target=send_clock).start()
    while True:
        temp1=[]
        
        back_str = new_socket.recv(4096).decode()
        back_info = back_str.split(";")
        if  back_info[0] == "D00004":
            clo = 1
            break
        elif back_info[0]=='D00007':

            global recfilelist
            recfilelist = []
            recfilelist=eval(back_info[2])
            print(recfilelist)
            print("REC" + str(recfilelist))

        elif back_info[0]=='D00008':
            global recfileflag
            recfileflag=3
        elif back_info[0] == 'E00000' :
            #chat1.textBrowser.clear()
            meslist=eval(back_info[2])
            print('新的：'+str(meslist))
            print('原来的'+str(templist))
            if meslist==templist:
                continue
            else:
                if len(templist)>9:
                    templist=templist[:9]
                # leno=len(templist)
                # lenn=len(meslist) 
                temp1=[]
                temp1=meslist.copy()
                for i in templist:
                    if i in meslist:
                        temp1.remove(i)
                templist=meslist.copy()
                # temp1=[]
                # temp1=meslist.copy()
                # for i in temp1:
                #     if i in templist:
                #         temp1.remove(i)
                # templist=meslist.copy()
            
                id=''
                x=''
                a=''
                
                for i in temp1:
                    id=i[0]
                    
                    a=i[1]
                    if "￥￥发了图$$" in a:
                        b=''
                        a,b=a.split("￥￥发了图$$")
                        a=a+b
                    x=i[4]+'-'+i[3]+'-'+i[0]+'-'+i[2]

                    if id == tempid:

                        chat1.textBrowser.append("<font color='green'>"  +"<font size ='2'>"+"<font location>"+x)#姓名
                        chat1.textBrowser.append("<font color='black'>" +"<font size ='3'>"+a)#话
                        chat1.textBrowser.moveCursor(chat1.textBrowser.textCursor().End) # 文本框显示到底部
                    else:
                        chat1.textBrowser.append("<font color='blue'>"  +"<font size ='2'>"+"<font location>"+x)#姓名
                        chat1.textBrowser.append("<font color='black'>" +"<font size ='3'>"+a)#话
                        chat1.textBrowser.moveCursor(chat1.textBrowser.textCursor().End) # 文本框显示到底部
        
    flag = 0
    print("1")
    chat1.close()
    chat1.textBrowser.clear()
    back_str = new_socket.recv(4096).decode()


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
    global infor1
    por1.close()
    globalmanager.set_value2(1)

    infor1 = infor()
def portrait_2():
    global infor1
    por1.close()
    globalmanager.set_value2(2)

    infor1 = infor()
def portrait_3():
    global infor1
    por1.close()
    globalmanager.set_value2(3)

    infor1 = infor()
def portrait_4():
    global infor1
    por1.close()
    globalmanager.set_value2(4)

    infor1 = infor()
def portrait_5():
    global infor1
    por1.close()
    globalmanager.set_value2(5)

    infor1 = infor()
def portrait_6():
    global infor1
    por1.close()
    globalmanager.set_value2(6)

    infor1 = infor()
def portrait_7():
    global infor1
    por1.close()
    globalmanager.set_value2(7)

    infor1 = infor()
def portrait_8():
    global infor1
    por1.close()
    globalmanager.set_value2(8)

    infor1 = infor()
def portrait_9():
    global infor1
    por1.close()
    globalmanager.set_value2(9)

    infor1 = infor()


def user_login(log1):     #登录申请
    userid = log1.login_usr.text()
    global tempid
    global infor1
    pwd = log1.login_pwd.text()
    x = "A00001"+";"+str(userid)+";"+str(pwd)    
    new_socket.sendall(x.encode())
    back_str = new_socket.recv(4096).decode()
    back_info = back_str.split(";")
    print(back_info)
    if back_info[1] == "1": #登陆成功
        globalmanager.flag_tx=eval(back_info[2])
        infor1 = infor()
        infor1.group_btn.clicked.connect(infor2ag)  #通讯录跳转到拉取群聊
        infor1.deli.clicked.connect(partial(delTreeNodeBtn,infor1))
        infor1.tree.doubleClicked.connect(item_click)
        infor1.addi.clicked.connect(partial(delgroup,infor1))
        infor1.game.clicked.connect(lambda: gp1.show())
        # #infor1.game.clicked.connect(lambda: infor1.close())
        infor1.txti.clicked.connect(lambda: bot1.show())
        tempid = userid
        log1.close()
        global temp_constuser
        x = "A00110;"+userid
        new_socket.sendall(x.encode())
        back_str = new_socket.recv(4096).decode()
        back_info = back_str.split(";")
        if back_info[1] == "1":
            print(back_info)
            frequent_Contacts=eval(back_info[2])
            # temp_constuser = frequent_Contacts
            for i in frequent_Contacts:
                item = QTreeWidgetItem(infor1.root1)
                item.setText(0,str(i))   #工号
                item.setText(1,str(frequent_Contacts[i])) #部门-名字
                item.setToolTip(0,'双击用户发起群聊')
                item.setToolTip(1, '双击用户发起群聊')
                infor1.tree.addTopLevelItem(infor1.root1)
        else :
            warn_page.warn_label.setText(back_info[1])
            warnWindow.show()
        x = "A00111;"+userid
        new_socket.sendall(x.encode())
        back_str = new_socket.recv(4096).decode()        
        back_info = back_str.split(";")
        print("back_infor",back_info)
        if back_info[1] =="1":
            frequent_group = eval(back_info[2])
            for i in frequent_group:
                item = QTreeWidgetItem(infor1.root2)
                item.setText(0,str(i[0]))  #群聊ID
                item.setText(1,str(i[1]))  #群聊名称
                item.setToolTip(0,'双击用户发起群聊')
                item.setToolTip(1, '双击用户发起群聊')
                infor1.tree.addTopLevelItem(infor1.root2)
            infor1.show()
        else :
            warn_page.warn_label.setText(back_info[1])
            warnWindow.show()

        
    else :
        warn_page.warn_label.setText(back_info[1])
        warnWindow.show()
    
def logi2regi():  #登录跳转注册
    register_refresh(reg1)
    reg1.show()
    login_refresh(log1)
    log1.close()

def logi2find():  #登录跳转找回密码
    login_refresh(log1)
    log1.close()
    find_refresh(find_1)
    find_1.show()

def user_register(regi_page):  #用户注册申请
    regi_name = regi_page.register_name.text()
    regi_dep = regi_page.register_dep.currentText()
    regi_num = regi_page.register_num.text()
    regi_tel = regi_page.register_tel.text()
    regi_e = regi_page.register_email.text()
    regi_pwd = regi_page.register_pwd.text()
    regi_repwd = regi_page.register_repwd.text()
    regi_ask = regi_page.register_ask.currentText()
    regi_ans = regi_page.register_ans.text()
    regi_tx = globalmanager.get_value2()
    if regi_pwd != regi_repwd:
        regi_page.register_pwd.clear()
        regi_page.register_repwd.clear()
        warn_page.warn_label.setText("密码与确认密码不一致！")
        warnWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) #置顶
        warnWindow.show()
    else:
        x= "A00000"+";"+regi_name+";"+regi_dep+";"+regi_num+";"+regi_tel+";"+regi_e+";"+regi_pwd+";"+regi_ask+";"+regi_ans+";"+str(regi_tx)
        new_socket.sendall(x.encode())
        back_str = new_socket.recv(4096).decode()
        back_info = back_str.split(";")
        if back_info[1] =="1":
            reg1.close()
            tipWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) #置顶
            tip_page.label.setText("注册成功！请将面部对准摄像机3——5秒")
            
            tipWindow.show()

            log1.show()

        else :
            warn_page.warn_label.setText(back_info[1])
            register_refresh(regi_page)
            warnWindow.show()
        print(back_str)

def register_cancel(regi_page):  #注册界面-取消按钮
    reg1.close()
    regi_page.register_name.clear()
    regi_page.register_num.clear()
    regi_page.register_tel.clear()
    regi_page.register_email.clear()
    regi_page.register_pwd.clear()
    regi_page.register_repwd.clear()
    log1.show()

def user_password_forget(): #找回密码-确认
    x= find_1.find_name.text()   #收集工号
    global tempid
    tempid = x
    x = "A00011;"+x
    new_socket.sendall(x.encode())
    back_str = new_socket.recv(4096).decode()
    back_info = back_str.split(";")
    if back_info[1] =="1":
        find_1.close()
        find_refresh_2(find_2)
        find_2.find_ask.setText(back_info[2])
        find_2.find_ask.setReadOnly(True)
        find_2.show()
    else :
        warn_page.warn_label.setText(back_info[1])
        find_refresh(find_1)
        warnWindow.show()

def find_can(): # 找回密码-取消
    find_refresh(find_1)
    find_1.close()
    log1.show()

def user_password_forget_2():
    global tempid
    x= "A00100;"+tempid+";"+find_2.find_answer.text()
    print(tempid)
    print(x)
    new_socket.sendall(x.encode())
    back_str = new_socket.recv(4096).decode()
    back_info = back_str.split(";")
    print(back_str)
    if back_info[1] =="1":
        find_2.close()
        tipWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint) #置顶
        tip_page.label.setText("您的密码是："+back_info[2])
        tipWindow.show()
        log1.show()
    else :
        warn_page.warn_label.setText(back_info[1])
        find_refresh(find_1)
        warnWindow.show()

def find_can2():
    find_refresh_2(find_2)
    find_2.close()
    log1.show()

def infor2ag(): #转到拉取群聊界面
    x = "A01010"
    new_socket.sendall(x.encode())
    back_str = new_socket.recv(4096).decode()
    back_info = back_str.split(";")
    if back_info[1] == "1":
        member_all = eval(back_info[2])
        ag1.listwidget_1.clear()
        for i in member_all:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../pp/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(i[0]+"-"+i[2]+"-"+i[1])
            ag1.listwidget_1.addItem(item)
        member_selected = []
        for i in member_selected:
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../pp/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(i)
            ag1.listwidget_2.addItem(item)


        ag1.show()
    else:
        pass

# 槽函数，点击listwidget_1中的某一item，为listwidget_2添加item,点击listwidget_2中的某一item,去除该item
def change_func(listwidget):
    global temp_list
    if listwidget == ag1.listwidget_1:
        item = QListWidgetItem(ag1.listwidget_1.currentItem())
        ag1.listwidget_2.addItem(item)
        info = item.text().split("-")
        x= (info[0],info[1],info[2])  #部门，名字，工号
        if x[2] != tempid:
            temp_list.append(x)
        print(ag1.listwidget_2.count())

    else:
        item = QListWidgetItem(ag1.listwidget_1.currentItem())
        info = item.text().split("-")
        x= (info[0],info[1],info[2])
        try:
            temp_list.remove(x)
        except:
            pass
        ag1.listwidget_2.takeItem(ag1.listwidget_2.currentRow())
        ag1.listwidget_2.count()

def addfriends():
    global temp_list
    global tempid
    x = "B00000;"+tempid+";"+str(temp_list)
    new_socket.sendall(x.encode())
    back_str = new_socket.recv(4096).decode()
    back_info =back_str.split(";")
    if back_info[1] =='1':
        tip_page.label.setText(back_info[2])
        tipWindow.show()
        frequent_Contacts=eval(back_info[3])
        infor1.root1.takeChildren()
        for i in frequent_Contacts:
            item = QTreeWidgetItem(infor1.root1)
            item.setText(0,str(i))   #工号
            item.setText(1,str(frequent_Contacts[i])) #部门-名字
            item.setToolTip(0,'双击用户发起群聊')
            item.setToolTip(1, '双击用户发起群聊')
            infor1.tree.addTopLevelItem(infor1.root1)
    else:
        warn_page.warn_label.setText(back_info[1])
        warnWindow.show()

def delTreeNodeBtn(infor1):
    print('--- delTreeNodeBtn ---')
    global tempid
    item = infor1.tree.currentItem()
    # print(item.text(0))
    # root = infor1.tree.invisibleRootItem()
    # for item in infor1.tree.selectedItems():
    #     (item.parent() or root).removeChild(item)
    x = "B00001;"+tempid+";"+item.text(0)
    new_socket.sendall(x.encode())
    back_str = new_socket.recv(4096).decode()
    back_info = back_str.split(";")
    if back_info[1] =="1":
        tip_page.label.setText("删除成功！")
        tipWindow.show()
        frequent_Contacts=eval(back_info[2])
        infor1.root1.takeChildren()
        for i in frequent_Contacts:
            item = QTreeWidgetItem(infor1.root1)
            item.setText(0,str(i))   #工号
            item.setText(1,str(frequent_Contacts[i])) #部门-名字
            infor1.tree.addTopLevelItem(infor1.root1)
    
    else:
        warn_page.warn_label.setText(back_info[1])
        warnWindow.show()

def delgroup(infor1):
    print('--- delTreeNodeBtn ---')
    global tempid
    item = infor1.tree.currentItem()
    # print(item.text(0))
    # root = infor1.tree.invisibleRootItem()
    # for item in infor1.tree.selectedItems():
    #     (item.parent() or root).removeChild(item)
    x = "C00100;"+tempid+";"+item.text(0)
    new_socket.sendall(x.encode())
    print(x)
    back_str = new_socket.recv(4096).decode()
    back_info = back_str.split(";")
    print(back_info)
    if back_info[1] =="1":
        tip_page.label.setText("删除成功！")
        tipWindow.show()
        frequent_Contacts=eval(back_info[2])
        infor1.root2.takeChildren()
        for i in frequent_Contacts:
            item = QTreeWidgetItem(infor1.root2)
            item.setText(0,str(i[0]) )  #群id
            item.setText(1,str(i[1])) #群名
            infor1.tree.addTopLevelItem(infor1.root2)
    
    else:
        warn_page.warn_label.setText(back_info[1])
        warnWindow.show()


def item_click():
    global temp_groupid
    #print (item, str(item.text()))
    item = infor1.tree.currentItem()
    print("key=%s ,value=%s" % (item.text(0), item.text(1)))
    x='A01000;'+str(tempid)+";"+str(item.text(0))
    temp_groupid = item.text(0)
    print(x)
    new_socket.sendall(x.encode())
    print(new_socket)
    back_str = new_socket.recv(4096).decode()#返回id 
    print(back_str)
    back_info=back_str.split(';')

    if back_info[1]=="1":
        members =eval(back_info[2])  #参与聊天者,回执格式：list【xx部-xx-工号，···】
        chat1.listwidget.clear()
        for i in members:
            i=str(i)
            item = QtWidgets.QListWidgetItem()
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("../pp/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item.setIcon(icon)
            item.setText(i)
            item.setToolTip('双击开始单独聊天')
            #self.listwidget.setIconSize(QSize(50,50))
            chat1.listwidget.addItem(item)
        chat1.show()
        t1 = Thread(target = handle)
        t1.start()
        t1.join()
        # chat1.close()
        # chat1.textBrowser.clear()
    else:
        print('错误！')
        #这里应该有个界面弹出告诉你错误

def a_g():     #生成聊天界面
    global flag
    global temp_list
    global temp_groupid
    if flag == 2:
        warn_page.warn_label.setText("请勿重复打开聊天界面！")
        warnWindow.show()
    else:
        flag = 2
        tl=[]
        for i in temp_list:
            tl.append(i[2])
        x='C00000;'+str(tempid)+';'+str(tl)
        print(x)
        new_socket.sendall(x.encode())
        print(new_socket)
        back_str = new_socket.recv(4096).decode()#返回id 
        print(back_str)
        back_info=back_str.split(';')

        if back_info[1]=="1":
            back_str=back_info[2] # 群id
            temp_groupid = back_str
            item = QTreeWidgetItem(infor1.root2)
            item.setText(0, str(back_str))  # 群id
            item.setText(1, str('群号为'+str(back_str)+'的群聊~') ) # 部门-名字
            item.setToolTip(0, '双击用户发起群聊')
            item.setToolTip(1, '双击用户发起群聊')
            infor1.tree.addTopLevelItem(infor1.root2)

            members =eval(back_info[3])  #参与聊天者,回执格式：list【xx部-xx-工号，···】
            chat1.listwidget.clear()
            for i in members:
                item = QtWidgets.QListWidgetItem()
                icon = QtGui.QIcon()
                #icon.addPixmap(QtGui.QPixmap("E:/python_code/QT/pp/2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item.setIcon(icon)
                item.setText(i)
                item.setToolTip('双击开始单独聊天')
                #self.listwidget.setIconSize(QSize(50,50))
                chat1.listwidget.addItem(item)
            chat1.show()
            t1 = Thread(target = handle).start()
        else:
            print('错误！')
            #这里应该有个界面弹出告诉你错误

#发起群聊________


def sendtxt():
    a=chat1.textEdit.toPlainText()
    print(a)
    now = datetime.now() # current date and time
    date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
    global path
    if path!='':
        a = a +"￥￥发了图$$"+ path
        path=''
    x = "D00000"+';'+tempid+";"+date_time+";"+a+";"+temp_groupid
    new_socket.sendall(x.encode())
    print(x)
    chat1.textEdit.clear()

def text_changed():
    a=chat1.textEdit.toPlainText()
    if "\n" == a[-1:] :
        a = chat1.textEdit.toPlainText()
        print(a)
        now = datetime.now()  # current date and time
        date_time = now.strftime("%Y-%m-%d, %H:%M:%S")
        global path
        if path != '':
            a = a + "￥￥发了图$$"+path
            path = ''
        x = "D00000" + ';' + tempid + ";" + date_time + ";" + a + ";" + temp_groupid
        new_socket.sendall(x.encode())
        print(x)
        chat1.textEdit.clear()


def closechat():
    global flag
    x = "D00004"
    new_socket.sendall(x.encode())
    flag = 0
    print("closechat")


        
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
        """path='E:/python_code/QT/pp/emopho/0.jpg'
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
        #print(path)
        self.close()



        
        

# def text_changed():  #回车发送
#     global tempid
#     a=chat1.textEdit.toPlainText()
#     if '\n' in a:
#         x = '[管理员]-lt-1' + '\n'
        
        
#         if id == tempid:
#             chat1.textBrowser.append("<font color='green'>" + "<font size ='2'>" + "<font location>" +x)#名字(xx部-xxx-1120··· 时间)
#             chat1.textBrowser.append("<font color='black'>" + "<font size ='3'>" + a)#话
#         else:
#             chat1.textBrowser.append("<font color='blue'>" + "<font size ='2'>" + "<font location>" + x)
#             chat1.textBrowser.append("<font color='black'>" + "<font size ='3'>" + a)
        # +"<horizontal ='AlighLift'>"
        # self.textBrowser.append(a)
        # self.textBrowser.setTextColor(a,'red')
        # print (self.textBrowser.textColor())
        # self.textBrowser.setTextBackgroundColor()
        # chat1.textEdit.clear()

def emotioncheck():
    global  emo1flag
    emo1flag=1

    


def openfile():
    chat1.dir_path = QFileDialog.getOpenFileName(chat1, "请选择文件夹路径", "D:\\")
    """print(chat1.dir_path)
    print(chat1.dir_path)
    print(str(chat1.dir_path[0]))"""
    x = ''
    x = str(chat1.dir_path[0]).split('/')[-1]
    print(x)
    print(str(chat1.dir_path[0]))
    global filepath
    global filename
    filename=x
    filepath=str(chat1.dir_path[0])

def drift_bot():
    x=bot1.drift_txt.toPlainText()
    print(x)
    print(type(x))
    print('扔瓶子'+x+'结束')
    a='F00000'+';'+tempid+';'+str(x)
    print(a)
    new_socket.sendall(a.encode(encoding='utf-8'))
    bot1.drift_txt.clear()
    back_str = new_socket.recv(4096).decode()
def change_bot():
    #x=[1,2,3,4,5,6,78,7,87,8,78,'hhhhhh','xswl','我爱上了lt','lt真棒嘻嘻嘻']
    #y=random.sample(x, 1)
    #self.bottle_txt.setText(str(y))
    a='F00001'
    new_socket.sendall(a.encode(encoding='utf-8'))
    back_str = new_socket.recv(4096).decode()
    bot1.bottle_txt.setText(back_str)
    
def recfile():
    global recfileflag
    recfileflag=1
def dlfile():
    global recfileflag
    recfileflag=2
    item = QListWidgetItem(recc1.listwidget_1.currentItem())
    print(item.text())
    recfiletext=item.text()
    recc1.close()    


if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)

    warnWindow = QDialog()
    warn_page = warning.Ui_Dialog()  
    warn_page.setupUi(warnWindow)

    tipWindow = QDialog()
    tip_page = tips.Ui_Dialog()
    tip_page.setupUi(tipWindow)


    log1=log() #登录界面
    reg1=reg() #注册界面
    #infor1 = infor() #
    ag1=ag() #
    find_1 = find()
    find_2 = find2()
    chat1 = chat()
    emot1=emot()
    emo1=emo()
    bot1=bot()

    recc1 = recc()
    recfilelist=['1.jpg']
    for i in recfilelist:
        item = QtWidgets.QListWidgetItem()
        icon = QtGui.QIcon()
        item.setIcon(icon)
        item.setText(i)
        recc1.listWidget.addItem(item)
        print(1)

    botid1=botid()

    log1.show()

    #更换皮肤和主题

    por1=por()
    theme1=theme()
    #########################
    #log1.login_loginBtn.clicked.connect(lambda: infor1.show() )
    #log1.login_signBtn.clicked.connect(lambda: reg1.show())
    #_______________________
    gp1 = gp()
    # infor1.game.clicked.connect(lambda: gp1.show())
    # #infor1.game.clicked.connect(lambda: infor1.close())
    # infor1.txti.clicked.connect(lambda: bot1.show())
    #____________________________________________________________________
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


#登录界面    
    log1.login_loginBtn.clicked.connect(partial(user_login,log1))  #登录按钮
    log1.login_signBtn.clicked.connect(logi2regi)  #登录跳转注册
    log1.login_forgetBtn.clicked.connect(logi2find) #登录跳转找回

#注册界面
    reg1.register_conBtn.clicked.connect(partial(user_register,reg1))
    reg1.register_canBtn.clicked.connect(partial(register_cancel,reg1))

#警告界面    
    warn_page.warn_conBtn.clicked.connect(partial(warn_con,warnWindow))

#提示界面
    tip_page.conBtn.clicked.connect(partial(tip_con,tipWindow))

#密码找回界面
    find_1.find_conBtn.clicked.connect(user_password_forget)
    find_1.find_canBtn.clicked.connect(find_can)
    
#密保确认界面
    find_2.find_conBtn.clicked.connect(user_password_forget_2)
    find_2.find_canBtn.clicked.connect(find_can2)
    
#通讯录界面
    # infor1.group_btn.clicked.connect(infor2ag)  #通讯录跳转到拉取群聊
    # infor1.deli.clicked.connect(partial(delTreeNodeBtn,infor1))
    # infor1.tree.doubleClicked.connect(item_click)
    # infor1.addi.clicked.connect(partial(delgroup,infor1))
#拉取群聊界面
    ag1.addfriend.clicked.connect(addfriends)   #添加常用联系人
    ag1.listwidget_1.clicked.connect(partial(change_func,ag1.listwidget_1))
    ag1.listwidget_2.clicked.connect(partial(change_func,ag1.listwidget_2))
    ag1.addgroup.clicked.connect(lambda :a_g())
    
#聊天界面
    chat1.send.clicked.connect(sendtxt)
    chat1.closep.clicked.connect(closechat)
    chat1.textEdit.textChanged.connect(text_changed)  # 将该事件绑定到text_changed方法上
    
    chat1.emo.clicked.connect(lambda :emot1.show())
    emot1.table.cellPressed.connect(lambda :chat1.textEdit.append(path))
    recc1.listWidget.clicked.connect(lambda: recc1.close())

    chat1.pap.clicked.connect(openfile)
    chat1.dak.clicked.connect(lambda : emo1.show())
    chat1.dak.clicked.connect(emotioncheck)
    bot1.changebot.clicked.connect(change_bot)
    bot1.drift.clicked.connect(drift_bot)
    bot1.bottle_txt.setText("我永远喜欢李桐，嘻嘻~~")
    bot1.chaeckbotid.clicked.connect(lambda: botid1.show())
    chat1.pushButton_4.clicked.connect( lambda :recc1.show())

    sys.exit(app.exec_())
