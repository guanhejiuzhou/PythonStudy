import time
from math import sqrt
import json
import requests

"""
在Pyhton中实现文件的读写操作使用内置的open函数

操作模式   具体含义
'r'       读取（默认）
'w'       写入（会先截断之前的内容）
'x'       写入，如果文件已经存在会产生异常
'a'       追加，将内容写入到已有文件的末尾
'b'       二进制模式
't'       文本模式（默认）
'+'       更新（既可以读又可以写）
"""

''' ========== 读取文本文件 ========== '''


# 读取文本文件时，需要在使用open函数时指定好带路径的文件名（可以使用相对路径或绝对路径）并将文件模式设置为'r'（如果不指定，
# 默认也是'r'），然后通过encoding参数指定编码（如果不指定默认是None，那么在读取文件时使用的是操作系统默认的编码），如果
# 不能保证保存文件时使用的编码方式与encoding参数指定的编码方式是一致的，那么就可能无法解码字符而导致读取失败

# 读取一个纯文本文件
def main():
    f = None
    try:  # 将可能出现异常状况的代码块放在try代码块中
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally:  # finally代码块来关闭打开的文件，释放掉程序中获取的外部资源
        if f:
            f.close()


if __name__ == "__main__":
    main()


# 如果不愿意在finally代码块中关闭文件对象资源，可以使用上下文语法，通过with关键字
def main():
    try:
        with open('D:\个人资料\网址.txt', 'r', encoding='utf-8') as f:
            print('文件内容：' + f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了未知的编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')


if __name__ == "__main__":
    main()

# 除了使用文件帝乡的read方法读取文件外，还可以使用for-in循环逐行读取或者用readlines将文件按行读取到一个列表容器中
""" ========== 一次性读取整个文件内容 ========== """


def main1():
    with open('D:\个人资料\网址.txt', 'r', encoding='utf-8') as f:
        print(f.read())


if __name__ == '__main__':
    main1()

''' ========== 通过for-in循环逐行读取 ========== '''


def main2():
    with open('D:\个人资料\网址.txt', mode='r') as f:
        for line in f:
            print(line, end='')
            time.sleep(0.5)
    print()


if __name__ == '__main__':
    main2()

''' ========== 读取文件按行读取到列表中 ========== '''


def main3():
    with open('D:\个人资料\网址.txt') as f:
        lines = f.readlines()
    print(lines)


if __name__ == '__main__':
    main3()

''' ========== 写入 ========== '''


# 将文本信息写入文件，在使用open函数时指定好文件名并将文件模式设置为'w'。
# 如果需要对文件内容进行追加式写入，将模式设置为'a'

# 将1-9999之间的素数分别写入三个文件中，1-99之间的素数保存在a.txt，100-999之间的素数保存在b.txt，其他的保存在c.txt
def is_prime(n):
    """判断素数的函数"""
    assert n > 0
    for factor in range(2, int(sqrt(n)) + 1):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误!')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成!')


if __name__ == '__main__':
    main()

''' ========== 读写二进制文件 ========== '''


def main():
    try:
        with open('D:\个人资料\wangpan\myResousce\images\1234.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('D:\个人资料\wangpan\myResousce\images\timg.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定的文件无法打开')
    except IOError as e:
        print('读写文件时出现错误')
    print('程序执行结束')


if __name__ == '__main__':
    main()

''' ========== 读取json文件 ========== '''


def main():
    mydict = {
        'name': '云长',
        'age': 58,
        'brother': ['玄德', '翼德'],
        'cars': [
            {'brand': '赤兔', 'max_speed': 1000},
            {'brand': '的卢', 'max_speed': 700},
            {'brand': '乌骓', 'max_speed': 800}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs, ensure_ascii=False)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
'''
json模块主要有4个比较重要的函数
dump--将python对象按照json格式序列化到文件中
dumps--将python对象处理成json格式的字符串
load--将文件中的json数据反序列化成对象
loads--将字符串的内容反序列化成python对象
'''


def main():
    resp = requests.get('https://v1.jinrishici.com/all.json')
    data_model = json.loads(resp.text)
    print(data_model)
    for news in data_model:
        print(news)


if __name__ == '__main__':
    main()
