#工具函数

def login_refresh(log1): #登录界面全部清空
    log1.login_usr.clear()
    log1.login_pwd.clear()

def register_refresh(reg1):  #注册界面全部刷新
    reg1.register_name.clear()
    reg1.register_num.clear()
    reg1.register_tel.clear()
    reg1.register_email.clear()
    reg1.register_pwd.clear()
    reg1.register_repwd.clear()

def find_refresh(find_page):
    
    find_page.find_name.clear()
    
def find_refresh_2(find_page2):
    find_page2.find_ask.setReadOnly(False)
    find_page2.find_ask.clear()
    find_page2.find_answer.clear()

def warn_con(warnWindow):  #关闭警告窗
   warnWindow.close()

def tip_con(tipWindow):  #关闭提示窗
    tipWindow.close()