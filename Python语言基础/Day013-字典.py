# dict函数（构造器）中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
print(person)  # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}

# 通过python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)  # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)  # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)  # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}

# 获取字典中一共有多少对键值对用len函数
print(len(person))  # 4
# 相对字典进行遍历，可以用for循环，for循环只是对字典的键进行了遍历
for key in person:
    print(key)

''' ========== 字典的运算 ========== '''
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
# 检查name和Tel两个键在不在person字典中
print('name' in person, 'tel' in person)  # True False
# 通过age将person字典中对应的值修改
if 'age' in person:
    person['age'] = 25
print(person)  # {'name': '王大锤', 'age': 25, 'weight': 60, 'home': '中同仁路8号'}
# 通过索引操作向字典中存入新的键值对
person['tel'] = '13900000000'
print(person)  # {'name': '王大锤', 'age': 25, 'weight': 60, 'home': '中同仁路8号', 'tel': '13900000000'}
# 对字典的键进行循环并通过索引运算获取键对应的值
for key in person:
    print(f'{key}: {person[key]}')

''' ========== 字典的方法 ========== '''
# 字典中的值又是一个字典（嵌套的字典）
students = {
    1001: {'name': '狄仁杰', 'sex': 'True', 'age': 22, 'place': '山西大同'},
    1002: {'name': '李元芳', 'sex': True, 'age': 23, 'place': '河北保定'},
    1003: {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}
}
# 使用get方法通过键获取对应的值，如果取不到不会引发KeyError异常而是返回None或设定的默认值
print(students.get(1002))  # {'name': '李元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
print(students.get(1005))  # None
print(students.get(1005), {'name': '无名氏'})  # {'name': '无名氏'}

# 获取字典中所有的键
print(students.keys())  # dict_keys([1001, 1002, 1003])
# 获取字典中所有的值
print(students.values())  # dict_values([{'name': '狄仁杰', 'sex': 'True', 'age': 22, 'place': '山西大同'}, {'name': '李元芳', 'sex': True, 'age': 23, 'place': '河北保定'}, {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}])
# 获取字典中所有的键值对
print(students.items())
# 对字典中所有的键值对进行循环遍历
for key, value in students.items():
    print(key, '--->', value)

# 使用pop方法通过键删除对应的键值对并返回该值
stu1 = students.pop(1002)
print(stu1)  # {'name': '李元芳', 'sex': True, 'age': 23, 'place': '河北保定'}
# 使用popitem方法删除字典中最后一组键值对并返回对应的二元组
# 如果字典中没有元素，调用该方法将引发KeyError异常
key, value = students.popitem()
print(key, value)  # 1003 {'name': '武则天', 'sex': False, 'age': 20, 'place': '四川广元'}

# setdefault可以更新字典中的键对应的值或向字典中存入新的键值对
# setdefault方法的第一个参数是键，第二个参数是键对应的值
# 如果这个键在字典中存在，更新这个键之后会返回原来与这个键对应的值
# 如果这个键在字典中不存在，方法将返回第二个参数的值，默认为None
result = students.setdefault(1005, {'name': '闪灵', 'sex': 'True'})
print(result)  # {'name': '闪灵', 'sex': 'True'}
print(students)

# 使用update更新字典元素，相同的键会用新值覆盖掉旧值，不同的键会添加到字典中
others = {
    1005: {'name': '乔峰', 'sex': True, 'age': 32, 'place': '北京大兴'},
    1010: {'name': '王语嫣', 'sex': False, 'age': 19},
    1008: {'name': '钟灵', 'sex': False}
}
students.update(others)
print(students)

# del方法从字典中删除元素，如果指定的键索引不到对应的值引发KeyError错误
person = {'name': '王大锤', 'age': 25, 'sex': True}
del person['age']
print(person)

''' ========== 字典的应用 ========== '''
# 例1：输入一段话统计每个英文字母出现的次数
sentence = input('请输入一段话：')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1
    for key, value in counter.items():
        print(f'字母{key}出现了{value}次.')

# 例2：在一个字典中保存了股票的代码和价格，找出股价大于100的股票并创建一个新的字典
stocks = {
'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用字典生成式语法创建新字典
stocks1 = {key: value for key, value in stocks.items() if value > 100}
print(stocks1)  # {'AAPL': 191.88, 'GOOG': 1186.96, 'IBM': 149.24, 'ACN': 166.89, 'FB': 208.09}