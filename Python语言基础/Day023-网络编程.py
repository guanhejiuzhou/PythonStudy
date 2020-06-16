import requests
from time import time
from threading import Thread
from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from base64 import b64encode
from json import dumps




# 继承Thread类创建自定义的线程类
class DownloadHanlder(Thread):
    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('D:/小东西/PythonStudy/picture/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests模块的get函数获取网络资源
    # 使用天行数据接口提供的网络API
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=fb7f9bffcac68c7b67e58c25dfc3939a&num=20'
    )
    # 将服务器返回的json格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['newslist']:
        url = mm_dict['picUrl']
        # 通过多线程的方式实现图片下载
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()

''' ========== 基于传输层协议的套接字编程 ========== '''
''' ========== TCP套接字 ========== '''

'''
# TCP套接字就是使用TCP协议提供的传输服务来实现网络通信的编程接口
# 在python中可以通过创建socket对象并指定type属性为SOCK_STREAM来使用TCP套接字

# 实现一个提供时间日期的服务器
def main():
    # 1.创建套接字对象并指定使用哪种传输服务
    """
    family=AF_INET --- IPV4地址
    family=AF_INET6 --- IPV6地址
    type=SOCK_STREAM --- TCP套接字
    type=SOCK_DGRAM --- UDP套接字
    type=SOCK_RAW --- 原始套接字
    """
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定IP地址和端口（端口用于区分不同的服务）
    # 同一时间同一个端口上只能绑定一个服务否则报错
    server.bind(('192.168.0.103', 6789))
    # 3.开启监听-监听客户端连接到服务器
    # 参数512可以理解为连接队列的大小
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        # 4.通过循环接收客户端的连接并做出相应的处理（提供服务）
        # accept方法是一个阻塞方法，如果没有客户端连接到服务器，代码不会向下执行
        # accept方法返回一个元组，其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址（由IP和端口两部分构成）
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        # 5.发送数据
        client.send(str(datetime.now()).encode('utf-8'))
        # 6.断开连接
        client.close()


if __name__ == '__main__':
    main()


# 实现TCP客户端
def main():
    # 1.创建套接字对象默认使用IPV4和TCP协议
    client = socket()
    # 2.连接到服务器（需要指定IP地址和端口）
    client.connect(('192.168.0.103', 6789))
    # 3.从服务器接收数据
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
'''
'''
# 最简单的服务器代码
s = socket.socket()

# 获取当前机器的主机名
host = socket.gethostname()
print(host)
prot = 1234
s.bind((host, prot))

s.listen(5)
while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    c.send('Thank you for connecting')
    c.close()
'''


# 服务器端代码
def server_main():
    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient

        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # json是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = data
            # 通过dumps函数将字典处理成json字符串
            json_str = dumps(my_dict)
            # 发送json字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口（区分不同的服务）
    server.bind(('192.168.0.103', 5566))
    # 3.开启监听-监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('70_1104.jpg', 'rb') as f:
        # 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()


if __name__ == '__main__':
    server_main()
