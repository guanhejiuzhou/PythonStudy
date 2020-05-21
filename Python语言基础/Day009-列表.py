import random

# 将一个色子掷6000次，统计每个点数出现的次数
# 可以用1到6均匀分布的随机数来掷色子，然后用6个变量分别记录每个点数出现的次数

f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0
f6 = 0
for _ in range(6000):
    face = random.randint(1, 6)
    if face == 1:
        f1 += 1
    elif face == 2:
        f2 += 1
    elif face == 3:
        f3 += 1
    elif face == 4:
        f4 += 1
    elif face == 5:
        f5 += 1
    else:
        f6 += 1
print(f'1点出现了{f1}次')
print(f'2点出现了{f2}次')
print(f'3点出现了{f3}次')
print(f'4点出现了{f4}次')
print(f'5点出现了{f5}次')
print(f'6点出现了{f6}次')

'''
列表是由一系列元素按特定顺序构成的数据序列，这就意味着定义一个列表类型的变量，可以保存多个数据，而且允许数据重复
列表也是一种结构化的、非标量类型，操作一个列表类型的变量，除了可以使用运算符还可以使用它的方法
python中用[]定义列表，列表中的多个元素用逗号进行分隔
'''
items1 = [21, 12, 15, 22, 90]
items2 = ["python", "java", "c", "Go"]
# 除此以外还可以通过python内置的list函数将其他序列变成列表
items3 = list(range(1, 10))
print(items3)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
items4 = list("hello")
print(items4)  # ['h', 'e', 'l', 'l', 'o']
'''
需要说明的是，列表是一种可变数据类型，也就是说列表可以添加元素、删除、更新元素，和字符串有明显差别，字符串是一种
不可变数据类型，对字符串做拼接、重复、转化大小写、修剪空格等操作的时候会产生新的字符串，原来的字符串并没有发生任何改变
'''

""" ========== 列表的运算符 ========== """
items5 = [35, 12, 42, 26, 13]
items6 = [21, 78, 81]
# 列表的拼接
items7 = items5 + items6
print(items7)  # [35, 12, 42, 26, 13, 21, 78, 81]
# 列表的重复
items8 = ['hello'] * 3
print(items8)  # ['hello', 'hello', 'hello']
# 列表的成员运算
print(100 in items7)  # False
print('hello' in items8)  # True
# 获取列表长度(元素个数)
size = len(items7)
print(size)  # 8
# 列表的索引
print(items7[0], items7[-size])  # 35 35
items7[-1] = 100
print(items7)
print(items7[size - 1], items7[-1])  # 100 100
# 列表切片
items9 = [1, 23, 33, 45, 63, 15, 10, 90, 21]
print(items9[:5])  # [1, 23, 33, 45, 63]
print(items9[4:])  # [63, 15, 10, 90, 21]
print(items9[-5:-7:-1])  # [63, 45]
print(items9[::-2])  # [21, 10, 63, 33, 1]
# 列表的比较运算
items10 = [1, 2, 3, 4]
items11 = list(range(1, 5))
print(items10)
print(items11)
print(items10 == items11)  # True
items12 = [3, 2, 1]
print(items10 <= items12)  # True
'''
两个列表比较相等性比的是对应索引位置上的元素是否相等
两个列表比较大小比的是对应索引位置上的元素的大小
对于有N个元素的列表，正向索引的范围是0到N-1，负向索引的范围是-1到-N
'''

''' ========== 列表元素的遍历 ========== '''
# 如果想逐个取出列表中的元素，可以使用for循环，有以下两种做法
# 方法一
list1 = ['python', 'java', 'Go', 'C']
for index in range(len(list1)):
    print(list1[index])
# 方法二
list2 = ['python', 'java', 'C++']
for i in list2:
    print(i)
# 重构掷色子的代码
# 用counters列表中的六个元素分别表示1到6的点数出现的次数，最开始的时候六个元素的值都是0，接下来用随机数模拟掷色子，
# 如果摇出1点counters[0]的值加1，如果摇出2点counters[1]的值加1，以此类推
counters = [0] * 6
print(counters)
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')

''' ========== 列表的方法 ========== '''
list3 = ['python', 'java', 'Go', 'C++']
# 使用append方法在列表尾部添加元素

