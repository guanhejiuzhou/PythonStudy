import random
import string
from os.path import splitext
import os
import time

""" ========== 经典小案例-设计一个生成指定长度验证码的函数 ========== """
# 验证码由数字和英文大小写字母构成

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def generate_code(code_len=4):
    """
    生成指定长度的验证码
    :param code_len:验证码的长度（默认4个字符）
    :return:由大小写英文字母和数字构成的随机验证码字符串
    """

    code = ''
    for _ in range(code_len):
        # 产生0到字符串长度减1范围的随机数作为索引
        index = random.randrange(0, len(ALL_CHARS))
        # 利用索引运算从字符串中取出字符并进行拼接
        code += ALL_CHARS[index]
    return code


# 生成10组随机验证码
for _ in range(10):
    print(generate_code())

''' ========== 生成指定长度验证码函数的简单写法 ========== '''
# 直接利用random模块的随机抽样函数从字符串中取出指定数量的字符，然后利用字符串的join方法将选中的字符拼接起来
# 然后利用python标准库中的string模块来获得数字和英文字母的字面常量
ALL_CHARS1 = string.digits + string.ascii_letters


def generate_code1(code_len=6):
    """
    生成指定长度的验证码
    :param code_len:验证码长度（默认6个字符）
    :return:由大小写英文字母和数字构成的随机验证码字符串
    """
    # random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，抽样取出的字符是不重复的
    # choices实现有放回抽样，可能会重复选中某些字符。这两个函数的第一个参数代表抽样的总体，参数k代表抽样的数量
    return ''.join(random.choices(ALL_CHARS1, k=code_len))


# 生成5组随机验证码
for _ in range(5):
    print(generate_code1())

''' ========== 设计一个函数返回给定文件名的后缀名 ========= '''


def get_suffix(filename):
    """
    获取文件名的后缀名
    :param filename:文件名
    :return:文件的后缀名
    """
    # 从字符串中逆向查找.出现的位置
    pos = filename.rfind('.')
    # 通过切片操作从文件名中取出后缀名
    return filename[pos + 1:] if pos > 0 else ''


print(get_suffix('readme.txt'))  # txt
print(get_suffix('readme.txt.md'))  # md
print(get_suffix('.readme'))  #
print(get_suffix('readme.'))  #

''' ========== 设计一个函数返回给定文件名的后缀名-简单写法 ========== '''


# 直接使用os.path模块的splitext函数，这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组
# 二元组中第二个元素就是文件的后缀名（包含.），如果要去掉.，需要做一个字符串的切片操作
def get_suffix1(filename):
    return splitext(filename[1][1:])


''' ========== 在终端显示滚动文字 ========== '''

content = '北 京 欢 迎 你 为 你 开 天 辟 地           '
while True:
    # Windows清除屏幕上的输出
    # os.system('cls')
    # macOS清除屏幕上的输出
    os.system('clear')
    print(content)
    # 休眠0.2秒（200毫秒）
    time.sleep(0.2)
    content = content[1:] + content[0]
