"""
元组是多个元素按照一定的顺序构成的序列。
元组和列表的不同之处在于元组是不可变类型，元组类型的变量一旦定义，其中的元素不能添加或删除，元素的值也不鞥进行修改
定义元组使用()字面量语法
"""
# 定义一个三元组
t1 = (30, 10, 55)
# 定义一个四元组
t2 = ('哈哈', 40, True, 'python')
# 查看变量的类型
print(type(t1), type(t2))  # <class 'tuple'> <class 'tuple'>
# 查看元组中元素的数量
print(len(t1), len(t2))  # 3 4
# 通过索引运算获取元组中的元素
print(t1[0], t2[-3])  # 30 40
# 循环遍历元组中的元素
for number in t2:
    print(number)
# 成员运算
print(100 in t1)  # False
print('python' in t2)  # True
# 拼接
t3 = t1 + t2
print(t3)  # (30, 10, 55, '哈哈', 40, True, 'python')
# 切片
print(t3[::3])  # (30, '哈哈', 'python')
# 比较运算
print(t1 == t3)  # False
print(t1 >= t3)  # False
print(t1 < (30, 11, 55))  # True

''' ========== 元组的应用场景 ========== '''
# 当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型
# 当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
# 打包
a = 1, 10, 100
print(type(a), a)  # <class 'tuple'> (1, 10, 100)
# 解包
i, j, k = a
print(i, j, k)  # 1 10 100
# 在解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异常
a = 1, 10, 100, 1000
# i, j, k = a  # ValueError: too many values to unpack (expected 3)
# i, j, k, l, m, n = a  # ValueError: not enough values to unpack (expected 6, got 4)
# 有一种解决变量个数少于元素个数的方法，就是使用星号表达式，有了星号表达式，就可以让一个变量接收多个值
# 用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素。在解包语法中，星号表达式只能出现一次
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)  # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)  # 1 [10, 100] 1000
*i, j = a
print(i, j)  # [1, 10, 100] 1000
i, j, k, l, *m = a
print(i, j, k, l, m)  # 1 10 100 1000 []
# 解包语法对所有序列都成立，包括字符串、列表、range函数
a, b, *c = range(1, 10)
print(a, b, c)  # 1 2 [3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 10, 100]
print(a, b, c)  # 1 10 100
a, *b, c = 'hello'
print(a, b, c)  # h ['e', 'l', 'l'] o

''' 可变参数-其实就是将多个参数打包成了一个元组 '''


def add(*args):
    print(type(args), args)
    total = 0
    for val in args:
        total += val
    return total


add(1, 10, 20)  # <class 'tuple'> (1, 10, 20)
add(1, 2, 3, 4, 5)  # <class 'tuple'> (1, 2, 3, 4, 5)

''' ========== 交换两个变量的值 ========== '''
a = 1
b = 2
a, b = b, a
print(a, b)  # 2 1
d = 3
e = 4
f = 5
d, e, f = e, f, d
print(d, e, f)  # 4 5 3

''' ========== 让函数返回多个值 ========== '''


# 找出列表中最大值和最小值
def find_max_and_min(items):
    '''
    找出列表中最大和最小的元素
    :param items: 列表
    :return: 最大和最小元素构成的二元组
    '''

    max_one, min_one = items[0], items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one, min_one


''' 元组和列表的比较 '''
# 1.元组是不可变类型，不可变类型更适合多线程环境，它降低了并发访问量的同步化开销
# 2.元组是不可变类型，通常不可变类型在创建时间和占用空间上都优于对应的可变类型
# 3.python总元组和列表是可以相互转换的
# 将元组转换成列表
info = ('python', 10, True)
print(list(info))  # ['python', 10, True]
# 将列表转换成元组
fruits = ['apple', 'banana', 'orange']
print(tuple(fruits))  # ('apple', 'banana', 'orange')
