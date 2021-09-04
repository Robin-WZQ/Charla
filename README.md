# Charla
LAN communication software based on Python and PyQt5

## Background - 背景

> 本项目为北京理工大学小学期大作业，基于python和socket的即时通讯软件，面向企业，兼具保密性、实用性与趣味性。这个项目是本年级中唯一一个基于**python**语言和**PyQt5**框架编写的软件，而且功能丰富，广受老师和同学们的好评。

## Introduction - 项目简介

- 用户角度下-使用流程：
![屏幕截图 2021-09-04 123926](https://user-images.githubusercontent.com/60317828/132082606-c231df87-8a09-4742-8b2d-7c754a6efa26.png)
- 系统概要设计
![屏幕截图 2021-09-02 182107](https://user-images.githubusercontent.com/60317828/132082637-1311e787-7104-4284-a188-8e683595add8.png)
- 系统详细设计（只提供通信接口定义）
 
 参考服务端/数据交换协议.xlsx

## Features - 功能介绍

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
  - 敏感词侦测

## presentation - 部分功能界面展示
![3](https://user-images.githubusercontent.com/60317828/132081202-9ad80cfc-0f0d-4b79-b11a-bb099cc29da1.png)
![5](https://user-images.githubusercontent.com/60317828/132081205-f096d8dd-a997-4c6d-8f88-19c1d0eff557.png)


## Installation - 安装

### Requirements - 必要条件

- Windows10/Ubuntu 20.04
- python3.7 and up
- sqlite3
- PyQt5
- keras and tensorflow

### Steps - 安装流程

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
  
## Usage - 使用方法

1. 首先启动服务端

```
cd ./Charla/服务端/
python server.py
```

*注*：

- 修改本地IP地址，通过ipconfig语句在cmd中查看
- 修改all_files的文件夹地址

   2.其次启动客户端

```
python logist.py
```

*注*：

- 客户端与服务端须在两个窗口打开（若是在同一个电脑上）
- 首先开启人脸识别，按q退出
- 情感识别部分如果报错，可以注释掉，或者安装tensorflow等相关依赖
- 很多路径需要修改，请自行解决。
- 若是仍显示不出来图片，可以调式模式实时（运行也建议调式模式）

## Contributing

小学期我们6个人，用了5天时间，最后一天还刷了个夜，最后做成这个样子。但由于时间紧、任务重，以及能力有限，有些bug并没有即时解决的，主要出现在客户端多线程的问题，和整体框架设计、PyQt使用的问题。

欢迎各位开发者完善此项目！

### Contributors

感谢这些开发者对本项目的贡献：

@Tang Feiyao

@Zhao Yingying

@Li Tong

@Wang Jianan

@Liu yunhao

@Wang Zhongqi (myself)

## License
MIT License
