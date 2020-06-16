from socket import socket
from json import loads
from base64 import b64decode


# 客户端代码
def client_main():
    client = socket()
    client.connect(('192.168.0.103', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据多大，每次接收102字节
    data = client.recv(1024)
    while True:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成json字符串并转换成字典
    # loads函数的作用就是将json字符串转换成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    with open('D:/小东西/PythonStudy/picture/' + filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
    print('图片已保存')


if __name__ == '__main__':
    client_main()
