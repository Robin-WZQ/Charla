# Charla
LAN communication software based on Python and PyQt5

### Background - 背景

> 本项目为北京理工大学小学期大作业，基于python和socket的即时通讯软件，面向企业，兼具保密性、实用性与趣味性。这个项目是本年级中唯一一个基于**python**语言和**PyQt5**框架编写的软件，而且功能丰富，广受老师和同学们的好评。

### Introduction

- 用户角度下-使用流程：
![屏幕截图 2021-09-04 123926](https://user-images.githubusercontent.com/60317828/132082606-c231df87-8a09-4742-8b2d-7c754a6efa26.png)
- 系统概要设计
![屏幕截图 2021-09-02 182107](https://user-images.githubusercontent.com/60317828/132082637-1311e787-7104-4284-a188-8e683595add8.png)
- 系统详细设计（只提供通信接口定义）
 参考服务端/数据交换协议.xlsx

### Introduction - 功能简介

- 用户管理
  - 注册、登录、找回密码
  - 人脸识别、IP绑定
  - 好友、群聊、个人信息展示
  - 注销（仅服务端实现）
- 好友管理
  - 展示企业所有人员
  - 添加、删除他人为常用联系人
- 群组管理
  - 添加、删除群组
- 即时通信
  - 聊天实时展示
  - 文件传输
- 界面展示
  - 完成两个界面风格，可设置转换
  - 多个界面可进行跳转
- 特殊功能
  - 漂流瓶
  - 情感识别打卡
  - 表情包传输
  - 内置32个游戏

### presentation - 部分功能界面展示
![1](https://user-images.githubusercontent.com/60317828/132081191-01d653ba-f159-4410-9151-2bab1e6d3a18.png)
![2](https://user-images.githubusercontent.com/60317828/132081201-485436a4-9789-411a-b160-bf6913f96766.png)
![3](https://user-images.githubusercontent.com/60317828/132081202-9ad80cfc-0f0d-4b79-b11a-bb099cc29da1.png)
![4](https://user-images.githubusercontent.com/60317828/132081204-a0bd25fb-2b2e-48f6-a1df-c2837654ae54.png)
![5](https://user-images.githubusercontent.com/60317828/132081205-f096d8dd-a997-4c6d-8f88-19c1d0eff557.png)
![7](https://user-images.githubusercontent.com/60317828/132081207-1f639589-6468-41e7-bca4-0c82e95c96f6.png)


### Installation - 安装

#### Requirements - 必要条件

- Windows10/Ubuntu 20.04
- python3.7 and up
- sqlite3
- PyQt5
- keras and tensorflow

#### Steps - 安装流程

- 安装Ubuntu虚拟机（**可选**，本项目可在Windows下运行）

  参考链接：

  1. [VMware虚拟机安装](https://www.cnblogs.com/fuzongle/p/12760193.html)
  2. [ubuntu安装anaconda](https://blog.csdn.net/qq_15192373/article/details/81091098)
  3. [python3重定向](https://blog.csdn.net/weixin_39715012/article/details/104741637)
  4. [VMware下Ubuntu与Windows实现文件共享的方法](https://www.cnblogs.com/jiangxiaobo/p/7815678.html)
  5. [Ubuntu连接网络](https://www.jb51.net/article/158414.htm)

  安装资源：

  1. Ubuntu20.04镜像文件
  2. VMare工作站下载文件

- 下载当前文件夹

```
mkdir Charla
cd ./Charla
git clone https://github.com/Robin-WZQ/Charla.git
```

- 下载安装sqlite3

  参考菜鸟教程：[SQLite – Python | 菜鸟教程 (runoob.com)](https://www.runoob.com/sqlite/sqlite-python.html)

- 下载安装PyQt5

  参考教程：[pyqt5安装教程](https://blog.csdn.net/ifeng12358/article/details/102943588)

- 下载安装Ternsoflow+keras

  参考教程：[Win10系统 安装Anaconda+TensorFlow+Keras](https://www.cnblogs.com/zeroingToOne/p/8407059.html)
