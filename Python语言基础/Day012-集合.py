""" ========== 创建集合 ========== """
# 创建集合的字面量语法{}
set1 = {1, 2, 3, 3, 2}
print(set1)  # {1, 2, 3}
print(len(set1))  # 3
# 创建集合的构造器语法
set2 = set('hello')
print(set2)  # {'e', 'o', 'h', 'l'}
# 将列表转换成集合(可以去掉列表中的重复元素)
set3 = set([1, 2, 3, 3, 2, 1])
print(set3)  # {1, 2, 3}
# 创建集合的生成式语法(将列表生成式的[]换成{})
set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)  # {3, 5, 6, 9, 10, 12, 15, 18}
# 集合元素的循环遍历
for elem in set4:
    print(elem)
'''集合中的类型必须是hashable类型。通常不可变类型都是hashable类型，如整数、浮点数、字符串、元组等。而可变类型都不是
hashable类型，因为可变类型无法确定唯一的ID值，所以也就不能放到集合中，集合本身也是可变类型所以集合不能够作为集合中的元素
'''
''' ========== 集合运算-成员运算 ========== '''
# 通过成员运算in 和 not in 检查元素是否在集合中
set5 = {11, 12, 13, 14, 15}
print(10 in set5)  # False
print(15 in set5)  # True
set6 = {'python', 'java', 'C'}
print('python' in set6)  # True
print('PHP' not in set6)  # True
''' ========== 集合运算-交并差运算 ========== '''
set7 = {1, 2, 3, 4, 5, 6, 7}
set8 = {2, 4, 6, 8, 10}
# 交集
# 方法一：使用 & 运算符
print(set7 & set8)  # {2, 4, 6}
# 方法二：使用intersection方法
print(set7.intersection(set8))  # {2, 4, 6}
# 并集
# 方法一：使用 | 运算符
print(set7 | set8)  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 方法二：使用union方法
print(set7.union(set8))  # {1, 2, 3, 4, 5, 6, 7, 8, 10}
# 差集
# 方法一：使用 - 运算符
print(set7 - set8)  # {1, 3, 5, 7}
# 方法二：使用difference方法
print(set7.difference(set8))  # {1, 3, 5, 7}
# 对称差
# 方法一：使用 ^ 运算符
print(set7 ^ set8)  # {1, 3, 5, 7, 8, 10}
# 方法二：使用symmetric_difference方法
print(set7.symmetric_difference(set8))  # {1, 3, 5, 7, 8, 10}
# 方法三：对称差相当于两个集合的并集减去交集
print((set7 | set8) - (set7 & set8))  # {1, 3, 5, 7, 8, 10}
# 集合的交集、并集、差集运算还可以跟赋值运算一起构成复合运算
set9 = {1, 3, 5, 7}
set10 = {2, 4, 6}
# 将set9和set10求并集，再赋值给set9
set9 |= set10
print(set9)  # {1, 2, 3, 4, 5, 6, 7}
set11 = {3, 6, 9}
# 将set9和set11求交集再赋值给set9
set9 &= set11
print(set9)  # {3, 6}
''' ========== 集合运算-比较运算 ========== '''
set12 = {1, 3, 5}
set13 = {1, 2, 3, 4, 5}
set14 = set13
# < 运算符表示真子集，<= 运算符表示子集
print(set12 < set13, set12 <= set13)  # True True
print(set13 < set14, set13 <= set14)  # False True
# 通过issubset方法进行子集判断
print(set12.issubset(set13))  # True
# 用issuperset或>运算符进行超集判断
print(set13.issuperset(set12))  # True
print(set13 > set12)  # True

''' ========== 集合的方法 ========== '''
# 创建一个空集合
set1 = set()
# 通过add方法添加元素
set1.add(3)
set1.add(55)
set1.update({1, 10, 100, 1000})
print(set1)  # {1, 3, 100, 55, 1000, 10}

# 通过discard方法删除指定元素
set1.discard(100)
set1.discard(99)
print(set1)  # {1, 3, 55, 1000, 10}
# 通过remove方法删除指定元素，先做成员运算再删除，否则元素不在集合中会引发KeyError异常
if 10 in set1:
    set1.remove(10)
print(set1)  # {1, 3, 55, 1000}

# pop方法可以从集合中随机删除一个元素并返回该元素
print(set1.pop())

# clear方法清空整个集合
set1.clear()
print(set1)  # set()

# 如果要判断两个集合有没有相同的元素可以使用isdisjoint方法,如果不包含返回True，否则返回False
a = {'java', 'python', 'C'}
b = {'Kotlin', 'java', 'Dart'}
c = {'HTML', 'CSS', 'php'}
print(a.isdisjoint(b))  # False
print(a.isdisjoint(c))  # True

''' ========== 不可变集合 ========== '''
# python中的一种不可变类型的集合叫frozenset，frozenset不能添加和删除元素
d = frozenset({1, 3, 5, 7})
e = frozenset(range(1, 6))
print(d & e)  # frozenset({1, 3, 5})
print(d | e)  # frozenset({1, 2, 3, 4, 5, 7})
print(d - e)  # frozenset({7})
print(d < e)  # False
