import random


""" ================== for-in循环 ======================"""
# 如果明确知道循环执行的次数，推荐使用for-in循环
# =================== for循环实现1-100求和 =====================
total = 0
for i in range(1, 101):
    total += i
print(total)
'''
range(101):可以用来产生0到100范围的整数，取不到101
range(0,101)：可以用来产生1到100范围的整数，前闭后开
range(1,101,2):可以用来产生1到100的奇数
range(100,0,-2):可以用来产生100到1的偶数
'''

# =============== 1-100偶数求和 ==================
total1 = 0
for i in range(0, 101, 2):
    total1 += i
print(total1)

""" ======================== while循环 ======================="""
# 如果要构造不知道具体循环次数的循环结构，推荐使用while循环。while循环通过一个能够产生或转换出bool值的表达式来
# 控制循环，表达式的值为True则继续循环，表达式值为False则结束循环


# 产生一个1到100范围的随机数
answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('请输入:'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print("小一点")
    else:
        print('恭喜你，猜对了!')
        break
# 当退出while循环的时候显示用户一共猜了多少次
print(f'你一共猜了{counter}次')
'''
关键字break：终止所在的那个循环
关键字continue：用来放弃本次循环后续的代码直接让循环进入下一轮
'''

""" ========== 嵌套的循环结构 ========== """
# 打印乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}*{j}={i*j}', end='\t')
    print()


""" ========== 例子：输入一个正整数判断是否为素数 ========== """
# 素数指的是只能被1和自身整数的大于1的整数
num = int(input("请输入一个正整数："))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
    if is_prime and num != 1:
        print(f'{num}是素数')
    else:
        print(f'{num}不是素数')


""" ========== 例子：输入两个正整数，计算它们的最大公约数和最小公倍数 =========="""
# 两个数的最大公约数是两个数的公共因子中最大的那个数
# 两个数的最小公倍数是能够同时被两个数整除的最小的那个数
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x  # python中可以用这样的方式来交换两个变量的值
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break

