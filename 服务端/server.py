# -*- coding: utf-8 -*-
"""
@File    : 基于TCP协议的socket_server端.py
@Time    : 2021/8/31 20:17
@Author  : wzq+lyh
@Software: VScode
"""

import base64
import random
import socket
import sqlite3
from os import TMP_MAX
from threading import Thread

global clocker
is_file = 0
file_information = ''
ONLINE_USERS = []

#用户管理部分的函数
def user_register(_conn, addr, c)  -> str:
    '''A00000'''
    #"A00000;王中琦;后勤部;1120190892;13671275167;2485794339@qq.com;wzq2163;您的生日是？;1月1日"
    user_infor = _conn.split(';')
    user_name = user_infor[1]
    user_depart = user_infor[2]
    user_id = user_infor[3].split(" ")
    user_tele = user_infor[4]
    user_email = user_infor[5]
    user_psd = user_infor[6]
    user_question = user_infor[7]
    user_answer = user_infor[8]
    user_face = user_infor[9]
    user_ip =list(addr)[0]
    result = ""
    try:
        if len(user_id[0]) != 10:
            result = "A00000;请输入10位工号"
        else:
            sql = "select * from login_info where id = ?"
            cursor = c.execute(sql, user_id).fetchall()
            if len(cursor) >= 1:
                result = "A00000;该用户已存在"
            else:
                sql2 = "select * from login_info where ip = ?"
                cursor2 = c.execute(sql2, user_ip.split(" ")).fetchall()
                if len(cursor2) >= 1:
                    result = "A00000;该电脑IP已经被注册"
                else:
                    sql = "insert into login_info (ip, id, password) values (?, ?, ?)"
                    c.execute(sql, (user_ip, user_id[0], user_psd))
                    sql = "insert into user_basic_info (ip, name, dname, id, phone, email, question, answer, face)\
                                values (?, ?, ?, ?, ?, ?, ?, ?, ?)"
                    c.execute(sql, (user_ip, user_name, user_depart, user_id[0], user_tele, user_email, user_question, user_answer, user_face))
                    result = "A00000;1"
    except:
        result = "A00000;服务器出错了"
    finally:
        return result

def user_login(_conn, addr, c) -> str:
    '''A00001'''
    #"A00001;1120190892;wzq2163"
    user_infor = _conn.split(';')
    _sql = []
    user_id = user_infor[1]
    user_psd = user_infor[2]
    user_ip =list(addr)[0]
    _sql.append(user_id)
    _sql.append(user_psd)
    _sql.append(user_ip)
    result = ""
    try:
        cursor = c.execute("select id from login_info\
            where id = ? and password = ?", _sql[:2]).fetchall()
        if len(cursor)==0:
            result = "A00001;用户名或密码错误"
        else:
            cursor = c.execute("select id from login_info\
            where id = ? and password = ? and ip = ?", _sql).fetchall()
            if len(cursor) == 0:
                result = "A00001;非法登入"
            else:
                _sql2 = "update login_info set is_online = 1 where id = ?"
                c.execute(_sql2, user_id.split(" "))
                _sql3 = "select face from user_basic_info where id = ?"
                user_face = c.execute(_sql3, user_id.split(" ")).fetchall()[0][0]
                result = "A00001;1;" + user_face
    except:
        result = "A00001;服务器出错了"
    finally:
        return result

def user_change_infor(_conn, addr,c) -> str:
    '''A00010'''
    user_infor = _conn.split(';')
    user_name = user_infor[1]
    user_depart = user_infor[2]
    user_id = user_infor[3]
    user_tele = user_infor[4]
    user_email = user_infor[5]
    user_ip = list(addr)[0]
    _sql = []
    _sql.append(user_id)
    _sql.append(user_ip)
    try:
        cursor = c.execute("select id from login_info\
                where id = ? and ip = ?", _sql).fetchall()
        if len(cursor)==0:
            result = "A00010;非法登入"
        else:
            _sql2 = "update user_basic_info set name = ?, dname = ?, phone = ?, email = ?\
                where id = ?"
            cursor = c.execute(_sql2, (user_name, user_depart, user_tele, user_email, user_id))
            result = "A00010;1"
    except:
        result = "A00010;服务器出错了"
    finally:
        return result

def user_password_forget(_conn, addr,c) -> str :
    '''A00011'''
    #"A00011;1120190892"
    user_infor = _conn.split(';')
    user_id = user_infor[1].split(" ")
    try:
        cursor = c.execute("select * from user_basic_info\
            where id = ?", user_id).fetchall()
        if len(cursor) == 0:
            result = "A00011;用户不存在"
        else:
            result = "A00011;1;" + cursor[0][7]
    except:
        result = "A00011;服务器出错了"
    finally:
        return result
        
def user_password_forget_2(_conn, addr, c) -> str :
    '''A00100'''
    #"A00100;112019089;1月1日"
    user_infor = _conn.split(';')
    user_id = user_infor[1].split(" ")
    user_answer = user_infor[2]
    try:
        cursor = c.execute("select * from user_basic_info\
            where id = ?", user_id).fetchall()
        if cursor[0][8] == user_answer:
            cursor2 = c.execute("select * from login_info\
                where id = ?", user_id).fetchall()
            result = "A00100;1;"+cursor2[0][1]
        else:
            result = "A00100;密保答案错误"
    except:
        result = "A00100;服务器错误"
    finally:
        return result


def user_get_infor(user_id0,c) -> str:
    '''A00101'''
    #"1120190892"
    user_id = user_id0.split(" ")
    try:
        cursor = c.execute("select * from ubi_view\
            where id = ?", user_id).fetchall()
        if len(cursor) == 0:
            result = "A00101;用户不存在"
        else:
            cursor = cursor[0]
            result = "A00101;1"
            user_name = cursor[0]
            user_dpart = cursor[1]
            user_id = cursor[2]
            user_tele = cursor[3]
            user_emial = cursor[4]
            result = "A00101;1;"+str((user_name, user_id, user_dpart))
    except:
        result = "A00101;服务器出错了"
    finally:
        return result


def get_user_friend(_conn, addr, c) -> str:
    '''A00110'''
    #"A00110;111"
    result = ""
    try:
        friends = []
        dicts = {}
        user_infor = _conn.split(';')
        user_id = user_infor[1].split(" ")
    
        _sql = "select A.gid from group_info A, group_user B\
        where A.gid = B.gid and gtype = 0 and uid = ?"
        group_id = c.execute(_sql, user_id).fetchall()

        for id in group_id:
            temp = []
            _sql = "select uid, unreads from group_user where gid = ? and uid != ?"
            temp.append(id[0])
            temp.append(user_id[0])
            friend_id = c.execute(_sql, temp).fetchall()
            if len(friend_id) == 1:
                friends.append((user_get_infor(friend_id[0][0], c), friend_id[0][1]))
        for friend in friends:
            f = friend[0].split(";")

            k = eval(f[2])
            dicts[k[1]] = k[2]+"-"+k[0]+"("+str(friend[1])+")"
        result = "A00110;1;"+str(dicts)
    except:
        result = "A00110;服务器出错了"
    finally:
        return result

def get_user_group(_conn, addr, c) -> str:
    '''A00111'''
    # "A00111;222"
    user_infor = _conn.split(';')
    user_id = user_infor[1].split(" ")
    try:
        _sql = "select A.gid, gname from group_info A, group_user B \
        where A.gid = B.gid and uid = ? and gtype = 1"
        groups = c.execute(_sql, user_id).fetchall()
        result = "A00111;1;" + str(groups)   
    except:
        result = "A00111;服务器出错了"
    finally:
        return result
###
def get_group_info(_conn, addr, c) -> str:
    '''A01000'''
    #"A01000;1"
    group_infor = _conn.split(";")
    my_ID = group_infor[1]
    group_ID = group_infor[2]

    if len(group_ID) == 10:
        group_ID = transform(c,group_ID,my_id=my_ID)

    try:
        group_users = []
        _sql2 = "select uid from group_user where gid = ?"
        result2 = c.execute(_sql2, group_ID.split(" ")).fetchall()
        for id in result2:
            user = user_get_infor(id[0], c).split(";")[2]
            user = eval(user)
            name, ID, department = user[0], user[1], user[2]
            group_users.append(department + "-" + name + "-" + ID)
        result = "A01000;1;" + str(group_users)
    except:
        result = "A01000;服务器错误"
    return result

def del_user_all(_conn,addr,c)-> str:
    '''A01001'''
    #"A01001;1120190892"
    user_infor = _conn.split(";")
    user_id = user_infor[1].split(" ")
    try:
        _sql = "PRAGMA foreign_keys=ON"
        c.execute(_sql)
        _sql = "delete from login_info where id = ?"
        c.execute(_sql, user_id)
        result = "1"
    except:
        result = "服务器错误"
    finally:
        return result

def get_all_user_infor(c):
    '''A01010'''
    #'A01010'
    users = []
    _sql = "select id, name, dname from user_basic_info"
    cursor = c.execute(_sql)
    for row in cursor:
        user_to_id = row[0]
        user_to_name = row[1]
        user_to_dname = row[2]
        users.append((user_to_dname,user_to_id,user_to_name))
    return "A01010;1;"+str(users)

#好友管理部分
def add_friend(_conn, addr, c, database) -> str:
    '''B00000'''
    #"B00000;1120190892;[('1','王嘉楠','0'),('1','litong','1120191063')]"
    result = "B00000;未选中用户"
    friend_infor = _conn.split(";")
    my_id = friend_infor[1].split(" ")
    friends_id = eval(friend_infor[2])
    try:
        _sql1 = "select group_info.gid from group_info, group_user \
        where group_info.gid = group_user.gid and uid = ? and gtype = 0"
        groups = c.execute(_sql1, my_id).fetchall()
        friends = []
        for group in groups:
            _sql2 = "select uid from group_user where gid = ? and uid != ?"
            use = c.execute(_sql2, (group[0], my_id[0])).fetchall()
            if len(use) == 0:
                continue
            friends.append(use[0][0])
        for friend_id in friends_id:
            friend_id = friend_id[2]
            if friend_id in friends:
                continue
            _sql = "insert into group_info(ld_id, gtype) values(?, 0)"
            result = c.execute(_sql, my_id)
            database.commit()
            _sql = "select max(gid) from group_info"
            corrent_gid = c.execute(_sql).fetchall()[0][0]
            _sql = "insert into group_user(gid, uid) values(?, ?)"
            c.execute(_sql, (corrent_gid, my_id[0]))
            c.execute(_sql, (corrent_gid, friend_id))
            friends.append(friend_id)
        friends = get_user_friend("A00110;" + my_id[0], addr, c).split(";")[2]
        result = "B00000;1;添加成功;" + friends
    except:
        result = "B00000;添加失败，请检查网络连接"
    finally:
        return result

def del_friend(_conn, addr,c) -> str:
    '''B00001'''
    #"B00001;111;222"
    result = ""
    user_infor = _conn.split(";")
    user_id = user_infor[1].split(" ")
    friend_id = user_infor[2].split(" ")
    try:
        _sql = "select A.gid from group_info A, group_user B where gtype = 0 and uid = ?"
        gids = c.execute(_sql, user_id).fetchall()
        for gid in gids:
            _sql = "select gid from group_user where gid = ? and uid = ?"
            re = c.execute(_sql, (gid[0], friend_id[0])).fetchall()
            if len(re) == 0:
                continue
            _sql = "PRAGMA foreign_keys = ON"
            c.execute(_sql)
            _sql = "delete from group_info where gid = ?"
            c.execute(_sql, list(gid))
        friends = get_user_friend(_conn, addr, c).split(";")[2]
        result = "B00001;1;" + friends
    except:
        result = "B00001;服务器错误"
    finally:   
        return result


#群组管理
def create_group(_conn, addr,c,database) -> str:
    '''C00000'''
    # "C00000;111;['333','444']"
    group_infor = _conn.split(";")
    my_ID = group_infor[1]
    users_infor = eval(group_infor[2])
    users_infor.append(my_ID)
    users_infor = list(set(users_infor))
    try:
        _sql = "insert into group_info(ld_id, gtype)\
                values(?, 1)"
        result = c.execute(_sql, my_ID.split(" "))
        database.commit()
        _sql = "select max(gid) from group_info"
        corrent_gid = c.execute(_sql).fetchall()[0][0]
        for user in users_infor:
            _sql = "insert into group_user(gid, uid) values(?, ?)"
            c.execute(_sql, (corrent_gid, user))
        try:
            re = get_group_info("A01000;"  + my_ID+";" + str(corrent_gid) , addr, c).split(";")[2]
            result = "C00000;1;" + str(corrent_gid) + ";" + re
        except:
            result = "C00000;服务器错误"
    except:
        result = "C00000;服务器错误"
    finally:
        return result

def change_group(_conn, addr,c) -> str:
    '''C00001'''
    # 修改群主
    group_infor = _conn.split(";")
    admin_ID = group_infor[1]
    group_ID = group_infor[2].split(" ")
    new_admin_ID = group_infor[3]
    try:
        _sql = "select ld_id from group_info where gid = ?"
        result = c.execute(_sql, group_ID).fetchall()
        if admin_ID == result[0][0]:
            _sql2 = "update group_info set ld_id = ? where gid = ?"
            c.execute(_sql2, (new_admin_ID, group_ID[0]))
            result = "1"
        else:
            result = "无操作权限"
    except:
        result ="服务器错误"
    finally:
        return result

def join_group(_conn, addr,c) -> str:
    '''C00010'''
    group_infor = _conn.split(";")
    user_ID = group_infor[1]
    group_ID = group_infor[2].split(" ")
    try:
        _sql = "select * from group_info where gid = ?"
        result = c.execute(_sql, group_ID).fetchall()
        if len(result) == 0:
            result = "此群不存在"
        else:
            _sql2 = "select * from group_user where gid = ? and uid = ?"
            ls = [group_ID[0], user_ID]
            result2 = c.execute(_sql2, ls).fetchall()
            if len(result2) > 0:
                result = "您已在此群中"
            else:
                _sql3 = "insert into group_user(gid, uid) values(?, ?)"
                c.execute(_sql3, ls)
                result = "1"
    except:
        result = "服务器错误"
    finally:
        return result

def hand_group_request(_conn, addr,c) -> str:
    '''C00010'''
    pass

def del_user_group(_conn,addr,c) ->str:
    '''C00011'''
    group_infor = _conn.split(";")
    user_ID = group_infor[1]
    del_ID = group_infor[2]
    group_ID = group_infor[3].split(" ")
    try:
        _sql = "select ld_id from group_info where gid = ?"
        ld_id = c.execute(_sql, group_ID).fetchall()[0][0]
        # 不是群主还想删别人
        if user_ID != ld_id and del_ID != user_ID:
            result = "无删除权限"
        if user_ID == ld_id and del_ID == ld_id:
            new_ld_id = ""
            _sql2 = "select uid from group_user where gid = ?"
            users = c.execute(_sql2, group_ID).fetchall()
            for user in users:
                if user[0] != ld_id:
                    new_ld_id = user[0]
                    break
            _sql3 = "update group_info set ld_id = ? where gid = ?"
            c.execute(_sql3, (new_ld_id, group_ID[0]))
        _sql4 = "delete from group_user where gid = ? and uid = ?"
        c.execute(_sql4, [group_ID[0], user_ID])
        result =  "1"
    except:
        result = "服务器错误"
    finally:
        return result

def del_group(_conn,addr,c) ->str:
    '''C00100'''
    group_infor = _conn.split(";")
    user_ID = group_infor[1]
    group_ID = group_infor[2].split(" ")
    result = ""
    try:
        _sql = "select ld_id from group_info where gid = ?"
        ld_id = c.execute(_sql, group_ID).fetchall()[0][0]
        if user_ID == ld_id:
            new_ld_id = ""
            _sql2 = "select uid from group_user where gid = ?"
            users = c.execute(_sql2, group_ID).fetchall()
            for user in users:
                if user[0] != ld_id:
                    new_ld_id = user[0]
                    break
            _sql3 = "update group_info set ld_id = ? where gid = ?"
            c.execute(_sql3, (new_ld_id, group_ID[0]))
        _sql4 = "delete from group_user where gid = ? and uid = ?"
        c.execute(_sql4, [group_ID[0], user_ID])
        result = "C00100;1;" + get_user_group("A00111;" + user_ID, addr, c).split(";")[2]
    except:
        result = "C00100;服务器错误"
    finally:
        return result

#消息处理
def user_send_message(_conn, addr,c) -> str:
    '''D00000'''
    message_infor = _conn.split(";")
    message_sender_id = message_infor[1]
    message_time = message_infor[2]
    message_context = message_infor[3]
    group_ID = message_infor[4]
    result = ""
    try:
        f = open("sen_advertisement.txt", "r+", encoding='utf-8')
        for line in f.readlines():
            line = line.strip()
            if message_context.find(line) >= 0:
                message_context = message_context.replace(line, "*" * len(line))
    except IOError:
        print("Error:没有找到文件或读取文件失败！")
    else:
        print("Success!")
        f.close()

    if len(group_ID) == 10:
        group_ID = transform(c,group_ID,my_id=message_sender_id)
    try:
        _sql = "select name, dname from user_basic_info where id = ?"
        sname, sdname = c.execute(_sql, message_sender_id.split(" ")).fetchall()[0]
        _sql1 = "insert into all_information(gid, uid, content, send_time, name, dname)\
        values(?, ?, ?, ?, ?, ?)"
        c.execute(_sql1, (group_ID, message_sender_id, message_context, message_time, sname, sdname))
        _sql2 = "select uid from group_user where gid = ?"
        recipients = c.execute(_sql2, group_ID.split(" ")).fetchall()
        for recipient in recipients:
            _sql3 = "select unreads from group_user where gid = ? and uid = ?"
            new_unreads = c.execute(_sql3, [group_ID, recipient[0]]).fetchall()[0][0] + 1
            _sql4 = "update group_user set unreads = ? where gid = ? and uid = ?"
            c.execute(_sql4, (new_unreads, group_ID, recipient[0]))
        result = "D00000;1"
    except:
        result = "D00000;服务器错误"
    return result

def user_send_file(_conn, addr,c) -> str:
    '''D00001'''
    global is_file
    global file_information
    file_infor = _conn.split(";")
    file_information = eval(file_infor[1])
    # 将文件传输标识置为1
    is_file = 1
    
    
def recieve_file(_infor,addr,c) -> str:
    '''不需要标识'''
    global file_name
    global file_information
    try:
        gid = int(file_information[0])
        uid = file_information[1]
        file_name = file_information[2]
        send_time = file_information[3]
        with open(r'C:/Users/WZQ/Desktop/all_files/'+file_name,'ab+') as f:
            f.write(_infor)
        _sql = "insert into all_files(gid, uid, file_path, send_time) values(?, ?, ?, ?)"
        c.execute(_sql, (gid, uid, 'C:/Users/WZQ/Desktop/all_files/' + file_name, send_time))
        return "发送成功"
    except:
        return "发送失败"

def user_send_emotion(_conn, addr,c) -> str:
    '''D00011'''
    pass

def user_send_close(_conn,addr,c) -> str:
    '''D00004'''
    # 告诉客户端 那边的线程已经结束
    message_infor = _conn.split(";")
    result = message_infor[0]
    return result

def group_files(_conn,addr,c) -> str:
    '''D00007'''
    files_info = _conn.split(";")
    message_sender_id = files_info[1]
    group_ID = files_info[2]
    
    if len(group_ID) == 10:
        group_ID = transform(c,group_ID,my_id=message_sender_id)
    try:
        files_all = []
        _sql = "select file_path from all_files where gid = ?"
        files = c.execute(_sql,group_ID.split(" ")).fetchall()
        for file in files:
            files_all.append(file[0].split("/")[-1])
        result =  "D00007;1;"+str(files_all)
    except:
        result = "服务器错误"
    finally:
        return result
    

def download_file(_conn, addr, c):
    '''D00008'''
    download_file = _conn.split(";")
    message_sender_id = download_file[1]
    group_ID = download_file[2]
    file_name = download_file[3]
    if len(group_ID) == 10:
        group_ID = transform(c,group_ID,my_id=message_sender_id)

    _sql = "select file_path from all_files where gid = ?"
    files = c.execute(_sql,group_ID.split(" ")).fetchall()
    for file in files:
        if file.split("/")[-1] == file_name:
            with open("C:/Users/WZQ/Desktop/all_files/"+file_name,'rb') as f:
                buf=base64.b64encode(f.read())
                _conn.send(buf)
            break

def transform(c,group_ID,my_id):
    _sql = "select A.gid from group_info A, group_user B where gtype = 0 and uid = ?"
    gids = c.execute(_sql, my_id.split(" ")).fetchall()
    for gid in gids:
        _sql = "select gid from group_user where gid = ? and uid = ?"
        g_ID = c.execute(_sql, (gid[0], group_ID)).fetchall()
        if len(g_ID) == 0:
            continue
        group_ID = str(g_ID[0][0])
        break
    return group_ID 

#服务器消息
def get_unread_message(_conn, addr, c) -> str:
    '''E00000'''
    try:
        unread_message_infor = _conn.split(";")
        unreader = unread_message_infor[1]
        group_ID = unread_message_infor[2]
        result = ""

        if len(group_ID) == 10:
            group_ID = transform(c,group_ID,my_id=unreader)

        _sql1 = "update group_user set unreads = 0 where uid = ? and gid = ?"
        c.execute(_sql1, (unreader, group_ID))
        _sql2 = "select uid, content, send_time, name, dname from all_information\
        where gid = ? order by send_time DESC"
        message = c.execute(_sql2, group_ID.split(" ")).fetchall()
        if len(message) > 10:
            message = message[:10]
        result = "E00000;1;" + str(message)
    except:
        result = "E00000;服务器错误"
    finally:
        return result

def user_send_bottle(_conn, addr, c) -> str:
    '''F00000'''
    bottom_infor = _conn.split(";")
    bottom_sender = bottom_infor[1]
    bottom_time = "None"
    bottom_context = bottom_infor[2]
    _sql = "insert into drifting_bottle(sid, s_time, s_content) values(?, ?, ?)"
    c.execute(_sql, (bottom_sender, bottom_time, bottom_context))
    result = "F00000;"
    return result

def user_recieve_bottle(_conn, addr, c) -> str:
    '''F00001'''
    try:
        _sql = "select s_content from drifting_bottle"
        bottles = c.execute(_sql).fetchall()
        bottle_id = random.randint(0, len(bottles) - 1)
        result = bottles[bottle_id][0]
    except:
        result = "服务器错误"
    finally:
        return result

def all_message_recieve(_conn) -> str:
    global is_file
    if is_file == 1:
        _infor = _conn.recv(204800)
        _infor = base64.b64decode(_infor)
        _type = "doc"
        is_file = 0
    else:
        _infor = _conn.recv(1024)
        _infor = str(_infor, "utf-8")
        _type = _infor.split(";")[0]
    return _infor, _type

# 处理请求线程的执行方法
def handle(_conn, addr):
        try:
            #获取在线用户
            print("当前在线用户数量：",len(ONLINE_USERS)+1)
            ONLINE_USERS.append((_conn,addr))
            #打开数据库
            database = sqlite3.connect('server.db')
            print("Opened database successfully")
            c = database.cursor()            
            while True:
                if_return = 1
                #定义默认值
                _succ = "default"
                # 获取请求类型
                _infor,_type = all_message_recieve(_conn)
                if list(_type)[0] == 'A':
                    if _type == 'A00000':
                        _succ = user_register(_infor, addr,c)
                    elif _type == 'A00001':
                        _succ = user_login(_infor, addr,c)
                    elif _type == 'A00010':
                        _succ = user_change_infor(_infor, addr,c)
                    elif _type == 'A00011':
                        _succ = user_password_forget(_infor, addr,c)
                    elif _type == 'A00100':
                        _succ = user_password_forget_2(_infor, addr,c)
                    elif _type == "A00101":
                        _succ = user_get_infor(_infor, addr,c)
                    elif _type == "A00110":
                        _succ = get_user_friend(_infor, addr,c)
                    elif _type == "A00111":
                        _succ = get_user_group(_infor, addr,c)
                    elif _type == "A01000":
                        _succ = get_group_info(_infor, addr,c)
                    elif _type == "A01001":
                        _succ = del_user_all(_infor, addr,c)
                    elif _type == "A01010":
                        _succ = get_all_user_infor(c)
                    else:
                        pass
                elif list(_type)[0] == 'B':
                    if _type == "B00000":
                        _succ = add_friend(_infor, addr,c,database)
                    elif _type == "B00001":
                        _succ = del_friend(_infor, addr,c)
                    else:
                        pass
                elif list(_type)[0] == 'C':
                    if _type == "C00000":
                        _succ = create_group(_infor, addr,c,database)
                    elif _type == "C00001":
                        _succ = change_group(_infor, addr,c)
                    elif _type == "C00010":
                        _succ = join_group(_infor, addr,c)
                    elif _type == "C00011":
                        _succ = del_user_group(_infor, addr,c)
                    elif _type == "C00100":
                        _succ = del_group(_infor, addr, c)
                    else:
                        pass
                elif list(_type)[0] == 'D':
                    if _type == "D00000":
                        _succ = user_send_message(_infor, addr,c)
                    elif _type =="D00001":
                        _succ = user_send_file(_infor, addr,c)
                    elif _type == "D00010":
                        _succ = user_send_emotion(_infor, addr,c)
                    elif _type == "D00004":
                        _succ = user_send_close(_infor,addr,c)
                    elif _type == "D00007":
                        _succ = group_files(_infor,addr,c)
                    elif _type == "D00008":
                        if_return = 0
                    else:
                        pass
                elif list(_type)[0] == 'E':
                    if _type == "E00000":
                        _succ = get_unread_message(_infor, addr,c)
                    else:
                        pass
                elif list(_type)[0] == 'F':
                    if _type == "F00000":
                        _succ = user_send_bottle(_infor, addr, c)
                    elif _type == "F00001":
                        _succ = user_recieve_bottle(_infor, addr, c)
                    else:
                        pass
                elif list(_type)[0] == 'd':
                    _succ = recieve_file(_infor,addr,c)
                print(_succ)
                if if_return == 1:
                    _conn.sendall(str(_succ).encode(encoding='utf-8'))
                else:
                    if_return = 0
                database.commit()  
        except Exception as e:
            print(str(addr) + " 连接异常，准备断开: " + str(e))
            # 退出用户记录
            ONLINE_USERS.remove((_conn,addr))
            _sql = "update login_info set is_online = 0 where ip = ?"
            c.execute(_sql, addr[0].split(" "))
            database.commit()
        finally:
            try:
                _conn.close()
            except:
                print(str(addr) + "连接关闭异常")

if __name__ == "__main__":
    try:
        ONLINE_USERS.clear()
        sk = socket.socket()
        sk.bind(('10.195.54.156', 12323))  # 服务器端口及ip地址
        # 最大挂起数
        sk.listen(10)
        print("服务器启动成功，开始监听...")
        while True:
            conn, addr = sk.accept()
            Thread(target=handle, args=(conn, addr)).start()
    except Exception as e:
        print("服务器出错: " + str(e))