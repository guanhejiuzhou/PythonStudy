# 以3个单引号或双引号开头的字符串可以拆行
s3 = '''
hello,
world!
'''
print(s3, end='')  # print函数中的end=''表示输出后不换行，即将磨人的结束符\n(换行符)更换为''(空字符)

''' ========== 转义字符和原始字符串 ========== '''
# 可以在字符串中使用反斜杠\来表示转义，也就是说\后的字符不再是它原来的意义，例如：\n表示换行，\t表示制表符
# 如果字符串本身又包含了'、"、\这些特殊字符，必须要通过\进行转义处理
# 输出一个带单引号或反斜杠的字符串
s1 = '\'hello,world!\''
print(s1)
s2 = '\\hello,world!\\'
print(s2)
# python中的字符串可以以r或R开头，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义
# 在字符串中'hello\n'中，\n表示换行，而在r'hello\n'中，\n就是反斜杠和字符n
# 字符串s1中\t是制表符，\n是换行符
s1 = '\time up \now'
print(s1)
# 字符串s2中没有转义字符，每个字符都是原始含义
s2 = r'\time up \now'
print(s2)

''' ========== 字符串的运算 ========== '''
# 字符串的拼接和重复
s1 = 'hello' + ' ' + 'world'
print(s1)  # hello world
s2 = '!' * 3
print(s2)  # !!!
s1 += s2
print(s1)  # s1 = s1+s2
s1 *= 2
print(s1)  # s1=s1*2
# 比较运算 （字符串的大小比较的是每个字符对应的编码大小）
a = 'a whole new world'
b = 'hello world'
print(ord('a'), ord('h'))
print(a == b, a < b)
c = '龙战'
print(ord('龙'), ord('战'))
d = '龙骑'
print(ord('骑'))
print(c > d, c < d)

# is运算符（身份运算符），比较的是两个变量是否对应内存中的同一个字符串
e = 'hello world'
f = 'hello world'
g = f
# 比较字符串的内容
print(e == f, f == g)  # True True
# 比较字符串的内存地址
print(e is f, f is g)  # False True

# 成员运算 用in和not in判断一个字符串中是否存在另外一个字符或字符串
j = 'hello,world'
print('wo' in j)  # True
k = 'goodbye'
print(k in j)  # False

# 获取字符长度
k = 'hello,world'
print(len(k))  # 11
print(len('goodbye, world'))  # 14

# 索引和切片
h = 'abc123456'
H = len(h)
print(len(h))
# 获取第一个字符
print(h[0], h[-H])  # a,a
# 获取最后一个字符
print(h[H - 1], h[-1])  # 6,6
# 获取索引为2或-7的字符
print(h[2], h[-7])  # c,c

# 对字符串进行切片
# i=2,j=5,k=1的正向切片操作
print(h[2:5])  # c12
# i=-7,j=-4,k=1的正向切片操作
print(h[-7:-4])  # c12
# i=2,j=9,k=1的正向切片操作
print(h[2:])  # c123456
# i=2,j=9,k=2的正向切片操作
print(h[2::2])  # c246
# i=7,j=1,k=-1的负向切片操作
print(h[7:1:-1])  # 54321c
# i=-1,j=-10,k=-2的负向切片
print(h[::-2])  # 642ca

''' ========== 循环遍历 ========== '''
# 从字符串中取出每个字符，使用for循环对字符串进行遍历，有两种方式
p = 'hello'
for index in range(len(p)):
    print(p[index])

for i in p:
    print(i)

""" ========== 字符串的方法-大小写相关操作 ========== """
a1 = 'hello, world!'
# 使用capitalize方法获得字符串首字母大写后的字符串
print(a1.capitalize())  # Hello, world!
# 使用title方法获得字符串每个单词首字母大写后的字符串
print(a1.title())  # Hello,World!
# 使用upper方法获得字符串大写后的字符串
print(a1.upper())  # HELLO,WORLD!
a2 = 'GOODBYE'
# 使用lower方法获得字符串小写后的字符串
print(a2.lower())  # goodbye

''' =========== 字符串方法-查找操作 ========== '''
# 如果想在一个字符串中从前向后查找有没有另外一个字符串，可以使用字符串的find和index方法
a3 = 'hello,world!'
# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(a3.find('or'))  # 7
# 找不到返回-1
print(a3.find('good'))  # -1

# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(a3.index('or'))  # 7
# 找不到引发异常
# print(a3.index('good'))  # ValueError: substring not found

# 从前向后查找字符l出现的位置（相当于第一次出现）
print(a3.find('l'))  # 2
# 从索引为5的位置开始查找字符l出现的位置
print(a3.find('l', 5))  # 9
# 从后向前查找字符l出现的位置（相当于最后一次出现）
print(a3.rfind('l'))  # 9

''' ========== 字符串方法-性质判断 ========== '''
a4 = 'hello,world'
# startwith方法检查字符串是否以指定的字符串开头，返回布尔值
print(a4.startswith('He'))  # False
print(a4.startswith('hell'))  # True
# endswith方法检查字符串是否以指定的字符串结尾，返回布尔值
print(a4.endswith('d'))  # True
# isdigit方法检查字符串是否由数字构成，返回布尔值
print(a4.isdigit())  # False
# isalpha方法检查字符串是否以字母构成，返回布尔值
print(a4.isalpha())  # False
# isalnum方法检查字符串是否以数字和字母构成，返回布尔值
print(a4.isalnum())  # False

''' ========== 字符串方法-格式化字符串 ========== '''
a5 = 'hello,world'
# center方法以宽度20将字符串居中并在两侧填充*
print(a5.center(20, "*"))  # ****hello,world*****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(a5.rjust(20))
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(a5.ljust(20, '~'))

m = 123
n = 321
print('%d * %d = %d' % (m, n, m * n))
print('{0} * {1} = {2}'.format(m, n, m * n))
# python3.6开始格式化字符串在字符串前面加f，在以f打头的字符串中，{变量名}是一个占位符，会被变量对应的值将其替换调
print(f'{m} * {n} = {m * n}')

''' ========== 字符串方法-修剪操作 ========== '''
z = '    hello,world  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print(z.split())
print(z.lstrip())
print(z.rstrip())
