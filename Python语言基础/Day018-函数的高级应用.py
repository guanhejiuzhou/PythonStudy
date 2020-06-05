import random
import time

""" =========== 装饰器 ========== """
'''装饰器是python中用一个函数装饰另外一个函数或类并为其提供额外功能的语法现象。装饰器本身是一个函数，它的参数是被装饰
的函数或类，它的返回值是一个带有装饰功能的函数。'''

"""
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
upload('Python从入门到放弃.pdf')

# 计算上传文件和下载文件用了多少时间
start = time.time()
download('MySQL从删库到跑路.avi')
end = time.time()
print(f'花费时间：{end - start:.3f}秒')
start = time.time()
upload('python从入门到放弃.pdf')
end = time.time()
print(f'花费时间：{end - start:.3f}秒')


# 将重复的代码封装到一个装饰器中，在有需要的地方直接使用这个装饰器
def record_time(func):
    # 定义装饰器函数，它的参数是被装饰的函数或类

    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # 在python中函数可以嵌套的定义（函数中可以再定义函数）
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间：{end - start:.3f}秒')
        # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
        return result

    # 返回带装饰功能的wrapper函数
    return wrapper


download(record_time(download))
upload(record_time(upload))
download('MySQL从入门到住院.avi')
upload('Java从入门到放弃.pdf')
"""


# 用@装饰器函数 将装饰器函数直接放在被装饰的函数上

def record_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间：{end - start:.3f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成')


@record_time
def upload(filename):
    print(f'开始上传{filename}')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成')


download('python从入门到放弃.avi')
upload('Java从入门到住院.pdf')


