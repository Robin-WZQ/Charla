## 服务端

#### 运行

```python
pip install -r Requirements.txt
python3 server.py
```

#### 文件代码树

│  client(just for test).py    服务端本地测试接口用的临时客户端文件
│  README.md   说明文本
│  Requirements.txt   需要的第三方库
│  sen_advertisement.txt   敏感词识别文本，可自定义添加
│  server.db   数据库文件，用sqlite打开
│  server.py   服务器端主函数
│  数据交换协议.xlsx  包含客户端与服务端的交换接口定义
└─all_files   客户端传过来的文件保存在此处（需要修改路径，==不要包含中文==）
        0.png
        R.jpg

