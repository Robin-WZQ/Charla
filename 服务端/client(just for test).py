import socket
new_socket = socket.socket() #创建socket对象
ip = "192.168.166.128"          
port = 40000              # 设置默认端口
new_socket.connect((ip,port))
i=0
print("欢迎来到聊天室！大家畅所欲言吧！")
x = "B00000;1120190892;[('1','王嘉楠','0'),('1','litong','1120191063')]"
y = "B00001"+";"+"112193160" +";"+ "1120190347"
z = "A00000;王中琦;后勤部;1120190892;13671275167;2485794339@qq.com;wzq2163;您的生日是？;1月1日"
e = "A00001;1120190892;wzq2163"
d = "A00011;112019089"
k = "A00100;112019089;1月1日"
g = "A01000;2"
f = "C00001;1120190892;2;11201908"
l = "C00010;112;2"
i = "C00011;11201908;1120190892;2"
d = "A00001;112ww;1"
p = "A01010"
q = "A00110;1120190892"
r = "D00000;1120193160;2021-08-31 12:11:59;baibai;74"
new_socket.sendall(r.encode())
back_str2 = new_socket.recv(1024).decode() #结束数据
if back_str2 !=None:
    print("2")
    print(back_str2)

# import socket
# from threading import Thread
# new_socket = socket.socket() #创建socket对象
# ip = "10.194.59.81"          
# port = 12323              # 设置默认端口
# new_socket.connect((ip,port))
# p = "A01010"
# new_socket.sendall(p.encode())
# def fun1():
#     while True:
#         back_str1 = new_socket.recv(1024).decode() #结束数据
#         if back_str1 != None:
#             print("1")
#             print(back_str1)

# def fun2():
#     while True:
        # back_str2 = new_socket.recv(1024).decode() #结束数据
        # if back_str2 !=None:
        #     print("2")
        #     print(back_str2)

# t1 = Thread(target=fun1).start()
# t2 = Thread(target=fun2).start()


# back_str = new_socket.recv(1024).decode() #结束数据
# if back_str != None:
#     print(back_str)
# new_socket.close() #关闭客户端
#     #print("客户端结束运行")
        