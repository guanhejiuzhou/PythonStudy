import random
from collections import Counter
import time


# 利用def关键字创建函数，简单来说函数就是将具有独立功能的代码块组织成一个模块，需要的时候调用
def hello_world():
    # 输入函数，input(),若input中有字符串，可以输出
    yourname = input('你好，请输入你的名字：')
    # 输出函数，print()，如果有多个对象输入，利用逗号分隔
    print('欢迎你来到python的世界,', yourname)
    print('让我们开始学习吧')


def hello_twice():
    # 利用global关键字定义全局变量，使之在整个程序运行周期能够被调用
    global yourname, yourheight, yourweight
    yourname = input('请输入你的名字：')
    yourheight = input('请输入你的身高：')
    yourweight = input('请输入你的体重：')


''' python中字符串的部分操作 '''


def deviding_line():
    # 字符串的创建利用单引号或者双引号进行创建
    word1 = 'i am line'
    # 字符串的函数，利用运算符进行调用，upper（）可以将字符串装换为全大写字母
    word2 = word1.upper()
    # lower()函数将字符串装换为全小写
    word3 = word1.lower()
    # title()函数，可以将字符串标题化
    word4 = word1.title()
    # []可以创建一个列表，列表可以存放很多对象
    words = [word1, word2, word3, word4]
    print(words)
    # 利用*运算符创建串，这里就是有40个-符号
    line = '-' * 40
    print(line)
    # 字符串可以利用+号直接相连
    endReturn = line + words[random.randint(0, 3)] + line
    print(endReturn)
    # 函数返回值，可以在被调用时将这个值返回
    return endReturn


''' python中的数字模型 '''


def study_number():
    num1 = input('请输入一个数字：')
    # 输出函数格式控制
    # type函数返回该值的类型
    print('你输入的是数字 %s' % num1, '它的类型为：', type(num1))
    # 利用int()函数进行数值类型转换，将数字转换为int整型
    num2 = int(input('再输入一个数字：'))
    print('你输入的是数字%s' % num2, '它的类型为:', type(num2))
    # float函数可以转换为浮点数类型
    num3 = float(input('再输入一个数字：'))
    print('你输入的是数字%s' % num3, '它的类型为：', type(num3))
    # 数字加法
    # format()函数格式化输出，在字符串中的{}符号将被替换为format的参数
    print('num1+num2={}'.format(int(num1) + num2))
    # 数字减法
    print('num1 - num2 = {}'.format(int(num1) - num2))
    # 数字乘法
    print('num1*num2={}'.format(int(num1) * num2))
    # 数字除法,{:.3f}表示输出格式小数点后面保留3位
    print('num2/num3={:.3f}'.format(num2 / num3))
    # 数字整除
    print('num2//num3={:.3f}'.format(num2 // num3))
    # 求余数
    print('num2%num3={:.3f}'.format(num2 % num3))
    # 求余数，输出格式为百分比格式
    print('num2%num3={:.3%}'.format(num2 % num3))
    # 幂运算
    print('num1**num2={}'.format(int(num1) ** num2))
    # format多参数，标记位置对应输出
    print('This is the {a}, and {b}'.format(a='numbers', b='some operations'))
    # bool值
    one, two, three = True, True, False
    print(one, two, three)
    # and运算，当两个值同时为真时才为真
    print('and运算符：', one and two, one and three)
    # or运算，当两个值同假时为假
    print('or运算：', one or two, one or three)
    # not运算，得到相反的值
    print('not运算：', not one, not two, not three)


''' python中的列表模型 '''


def study_list(length):  # 带有参数的函数
    # 创建列表，利用符号[]
    l1 = [1, 2, 3, 4, 5, 9.0]
    # 创建列表，也可以用list()函数
    # range函数，可以创建一个整数列表，格式为range(start,end,step)
    # start为开始位置，end为结束位置，前闭后开，step为步长
    l2 = list(range(10, 10 + length))
    print('l1的类型为：', type(l1))
    print('l2的类型为：', type(l2), l2)
    # 访问列表值，直接用list[num]的方式进行访问
    print(l1[1], l2[2])
    # 将l2赋给l3
    l3 = l2
    print(l3)
    # id()函数获取对象的内存地址
    print(id(l1), id(l2), id(l3))
    # 更新列表值
    l3[0] = 99
    print(l3)
    print('l2等于l3么？', l2 == l3)
    # 赋值列表，copy()函数创建一个一模一样的列表
    l4 = l2.copy()
    print(l4)
    # 更新l4列表值
    l4[0] = 999
    print('l4等于l2么?', l4 == l2)  # false
    # del进行删除列表值，python中del可以删除所有变量
    del l4[0]
    print('删除后', l4)
    # 给列表添加值
    l4.append(30)
    print(l4)
    # 给列表追加一个序列多个值
    l4.extend(l1)
    print('添加l1后l4的值为：', l4)  # [11, 12, 30, 1, 2, 3, 4, 5, 9.0]
    # 列表反转
    l4.reverse()
    print('反转后l4:', l4)  # [9.0, 5, 4, 3, 2, 1, 30, 12, 11]
    # sort函数，将列表进行排序
    l4.sort()
    print('排序后：', l4)  # [1, 2, 3, 4, 5, 9.0, 11, 12, 30]


''' python中的元组模型 '''


def study_tuple(length: int) -> bool:  # 解释参数类型的函数创建，->为返回值类型
    # 创建元组，利用()，元组不可改变
    tuple1 = (1, 2, 3, 4)
    # 利用tuple创建函数
    tuple2 = tuple(range(10, 10 + length))
    print(tuple1, tuple2)
    # count()输出某个值的数量
    print(tuple1.count(1))
    # index()按照索引得到值
    print(tuple1.index(1))
    # python中的异常处理，try:语句内部如果出现错误则会转入到except中
    try:
        tuple1[0] = 9  # 元组不可变，该句会出错
    except TypeError:
        print('元组更新失败')
    finally:
        print('不管更新成功与否我都会执行')

    try:
        print(id(tuple1), id(tuple2))  # 获取对象的内存地址
    except:
        return False
    else:
        tuple3 = tuple1 + tuple2  # 元组虽然不可改变，但是可以通过+号进行合并为另一个元组
        print(tuple3, id(tuple3))
    return True


''' python中的字典模型 '''


def study_dict():
    # 创建字典
    dict1 = {1: '一', 2: '二', 3: '三', 4: '四'}
    dict2 = dict(one=1, two=2, three=3)
    dict3 = dict(zip([6, 7, 8, 9], ['six', 'seven', 'eight', 'nine']))
    dict4 = dict([('one', 1), ('two', 2), ('three', 3)])
    dict5 = dict({1: '一', 2: '二', 3: '三', 4: '四'})
    print(dict1, dict2, dict3, dict4, dict5)
    # dict1和dict5是等价的
    print(type(dict1), dict1 == dict5)
    # 通过字典的键访问
    print(dict1[1], dict2['one'], dict3[6], dict4['one'], dict5[3])
    # 通过get函数访问内容
    print(dict1.get(4))
    # 修改字典内容
    dict1[1] = '壹'
    # 添加字典
    dict1[5] = '五'
    print(dict1)
    # in和not in关键字，判断值是否在序列中
    print(1 in dict1, 2 in dict2, 3 not in dict3)
    # 字典复制
    dict6 = dict1.copy()
    print(dict6)
    dict6[1] = 'one'
    print(dict1, '<dict1-----------------dict6>', dict6)
    # 清空字典
    dict1.clear()
    print(dict1)
    # 删除字典，也可以用del dict[key]的方式删除某个键
    del dict1, dict2
    del dict3[6]
    print(dict3)


''' 集合 集合中不存在相等的值 '''


def study_set():
    # 利用set函数创建集合
    set1 = set(['You', 'Are', 'Not', 'Beautiful'])
    print(set1)
    # 利用{}创建集合，创建空集合的时候不能用{},因为{}表示字典
    set2 = {'You', 'Are', 'so', 'Beautiful'}
    print(set2)
    # 集合复制
    set3 = set2.copy()
    print(set3)
    # 集合或运算符，得到两个集合中所有元素
    print(set1 | set2)
    # 集合与运算，得到两个几个的共同元素
    print(set1 & set2)
    # 不同时包含于set1和set2的元素
    print(set1 ^ set2)
    # 集合差运算，得到set1有，set2没有的元素
    print(set1 - set2)
    # <=符号，判断是否为子集，<符号，判断是否为真子集
    print(set1 <= set2, set3 <= set2, set3 < set2)
    # 集合添加元素
    set1.add('Me too')
    print(set1)
    # is和is not语句，is语句用于判断对象是否一样，==判断值是否一样
    print('is语句用法:', set3 == set2, set3 is set2, set1 is not set2)
    # 清空集合，集合变为空
    set3.clear()
    print(set3)
    # 删除集合
    del set3
    print(set3)


''' python中的一些函数 '''


def study_Some_functions():
    list1 = [1, 2, 3, 4, 5, 6]
    tuple1 = (11, 12, 13, 14, 15, 16)
    set1 = set(list1)
    dict1 = dict(zip([1, 2, 3, 4, 5], ['one', 'tow', 'three', 'four', 'five']))
    print(list1, tuple1, set1, dict1)
    # max()函数，得到序列中最大值
    print(max(list1), max(tuple1), max(set1), max(dict1))
    # min()函数，得到序列中最小值
    print(min(list1), min(tuple1), min(set1), min(dict1))
    # sun()函数，得到序列的和
    print(sum(list1), sum(tuple1), sum(set1), sum(dict1))
    # len()函数，得到序列长度
    print(len(list1), len(tuple1), len(set1), len(dict1))
    # divmod()函数，计算两个数的商和余数，结果两个格式为（商，余数）
    print(divmod(list1[0], tuple1[0]))
    # enumerate()函数，给元组添加一个索引
    print(list(enumerate(tuple1)))
    # 利用list将元组、集合、字典转换为列表
    list2 = list(tuple1)
    list3 = list(set1)
    list4 = list(dict1)
    print(list2, list3, list4)
    # 利用tuple()将列表、字典、集合转换为元组
    tuple2 = tuple(list1)
    tuple3 = tuple(set1)
    tuple4 = tuple(dict1)
    print(tuple2, tuple3, tuple4)

    # for循环语句
    for i in range(len(list1)):
        # print的属性end，可以使输出格式为end的内容，而不是默认换行
        print(list1[i], end=' ')
    print()
    # for循环遍历
    for i in dict1:
        print(i, dict1[i], end=' ')

    # reversed()函数，可以反转序列
    list5 = list(reversed(list1))
    print('\n', list5)  # \n 换行符

    testStr = '天地不仁，以万物为刍狗'
    # split()函数，以split（）内参数分割字符串，返回一个列表
    words = testStr.split(' ')
    print(words)
    # sort()函数，进行排序，参数key=len时，以字符串长度为标准排序
    words.sort(key=len)
    print('以长度排序：', words)
    # reverse参数，结果反转
    words.sort(key=len, reverse=True)
    print('以长度排序并且反转：', words)
    # 以字典序进行排序
    print('以字典序排序：', words)

    # collections模块中的Counter，可以得到字符串中每个数字出现次数
    ct = Counter(testStr)
    print(ct)
    # 更新
    ct.update('eeeexxxx11111')
    print(ct)
    # 得到字符数最多的前5位
    print(ct.most_common(5))


''' python的切片操作，得到序列的部分内容 '''


def study_Slice():
    str1 = '天下大势，分久必合，合久必分'
    list1 = list(range(10))
    tuple1 = tuple(list1)
    print(list1, tuple1)
    # 切片格式为str[start:end:step],前闭后开，step可为正负，默认步长为1
    print(str1[:])
    # 当步长为负数的时候反转
    print(str1[::-1])
    # 只有end时，截取最开始到end
    print(str1[:7])
    # 只有start时截取从start到末尾的所有字符
    print(str1[4:])
    # 步长为2
    print(str1[::2])
    print(str1[1::2])
    # 切片操作对于列表是和字符串操作同样的
    print(list1[:])

    # 切片赋值，右边必须为一个可以遍历的序列
    list1[1:5] = [10]
    print(list1)


''' python中的循环和选择语句 '''


def study_loop_select():
    list1 = [1, 2, 3, 4, 5]
    num = int(input('while循环，输入你想要循环的次数：'))
    i = 1
    # while expression:当expression为真的时候进行循环
    while i <= num:
        if i < 5:
            print('我打印了', i, '次')
        elif i < 10:
            print('打印了', i, '次', '真累')
        elif i < 15:
            print('打印太多了')
        elif i < 20:
            print('continue...')
            i += 1
            # continue语句，用在循环中，continue后的所有语句都不允许，直接进入下次循环
            continue
            print('我想我可能输出不了了')
        else:
            print('累死我了，都', i, '次了。。。')
            # break语句，直接退出循环
            break
        i += 1
        time.sleep(0.5)
    else:
        print('while结束了')

    # for循环
    for i in list1:
        print(i, end=' ')
    print()
    for i in range(5):
        print(i)


''' python表达式推导 '''


def study_expression_deduction():
    # 推导出列表
    list1 = [i for i in range(10)]
    # 语句中增加if，满足if后表达式的才会是列表
    list2 = [x for x in range(20) if x % 2 == 0]
    print(list1, '<list1----------list2>', list2)
    # 函数可以在任何地方被调用，如果是自己调用自己就可以称为递归调用
    print(deviding_line())

    list3 = [['_'] * 3 for i in range(3)]
    print(list3)

    fruits = ['Apple', 'Banana', 'Pear']
    colors = ['Red', 'Yellow', 'Green']
    # 两个列表合并
    suitcolor = [(colors, fruits) for colors, fruits in zip(colors, fruits)]
    print(suitcolor)
    # 两个列表的笛卡尔积
    cartesian = [(color, fruit) for color in colors for fruit in fruits]
    print(cartesian)
    # 字典的推导，只要是带有键值对的任何序列，都可以推导出字典
    dict1 = {fruit: color for fruit, color in suitcolor}
    print(dict1)


''' python文件读写 '''


def study_files():
    filepath = input('请输入你的文件路径（输入quit退出）：')
    if filepath == 'quit':
        return True
    try:
        # 打开文件,w为写格式打开
        file = open(filepath, 'w')
        file.write('现在开始写文件')
        # 关闭文件
        file.close()
        # r 读格式打开
        file = open(filepath, 'r')
        # read函数可以得到文件内容
        print('从文件中读出的内容：\n', file.read())
    except FileNotFoundError:
        print('文件不存在')
        # 递归调用
        study_files()
    except:
        print('出现错误，请重新输入路径')
        study_files()


''' 面向对象编程，python中创建类class，类包含有属性与方法，包括有私有变量，共有变量等等 '''


class User:
    # 类的构造方法，创建实例时自动调用
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
        self.yanzhi = 100

    # 类方法
    def display(self):
        print('大家好，我是{},身高{},体重{},颜值超高{}'.format(self.name, self.height, self.weight, self.yanzhi))


if __name__ == '__main__':
    # hello_world()
    hello_twice()
    # deviding_line()
    # study_number()
    # study_list(3)
    # study_tuple(5)
    # study_dict()
    # study_set()
    # study_Some_functions()
    # study_Slice()
    # study_loop_select()
    # study_expression_deduction()
    # study_files()
    # 在hello_twice()函数中定义了global语句，所以该函数的变量在以下程序中都可以使用
    # 实例化对象，创建Users类的实例
    user = User(yourname, yourheight, yourweight)  # yourname等变量是hello_twice()函数中定义的
    # 对象调用方法
    user.display()

    chooseinformation = '''输入您想要运行的函数的数量(quit是退出):
    1.study_number  2.study_list
    3.study_tuple   4.study_dict
    5.study_set     6.study_Some_functions
    7.study_Slice   8.study_loop_select
    9.study_expression_deduction
    10.study_files
    '''
    deviding_line()
    # while循环进行运行程序，只有当输入quit时才会退出循环
    while True:
        # 为了让输出不那么快，等待按键后才输出以下内容
        input('按键继续')
        print(chooseinformation)
        num = input('输入序号：')
        # 在以下if语句选择中，我们来选择运行不同的函数
        if num == 'quit':
            break
        elif num == '1':
            study_number()
        elif num == '2':
            study_list(3)
        elif num == '3':
            study_tuple()
        elif num == '4':
            study_dict()
        elif num == '5':
            study_set()
        elif num == '6':
            study_Some_functions()
        elif num == '7':
            study_Slice()
        elif num == '8':
            study_loop_select()
        elif num == '9':
            study_expression_deduction()
        elif num == '10':
            study_files()
        deviding_line()
    print('哈哈，恭喜你，这个程序结束了~')
