from random import randint

"""
分支和循环结构的应用
经典小案例
"""
''' ========== 寻找水仙花数 ========== '''
# 水仙花数被称为超完全数字不变数、自恋数、自幂数、阿姆斯特朗数，它是一个3位数，该数字每个位上数字的立方之和正好等于它本身
# 1³+5³+3³=153
# 这个题目的关键是将一个3位数拆分为个位、十位、百位，这一点利用python中的//(整除)和%(求模)可以实现
for num in range(100, 1000):
    low = num % 10  # 个位数(求模运算 % )
    mid = num // 10 % 10  # 十位数( // 整除运算)
    high = num // 100  # 整除获得百位数
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)

# 正整数的反转
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print('反转后为：', reversed_num)


''' ========== 百钱百鸡问题 ========== '''
# 鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，鸡翁、鸡母、鸡雏各几何？

# 假设公鸡的数量为x,x的取值范围是0到20
for x in range(0, 21):
    # 假设母鸡的数量为y,y的取值范围是0到33
    for y in range(0, 34):
        z = 100 - x -y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(f'公鸡：{x}只，母鸡：{y}只，小鸡：{z}只')


''' ========== CRAPS赌博游戏 ========== '''
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；
# 玩家如果摇出其他点数则玩家继续摇骰子，如果玩家摇出了7点，庄家胜；如果玩家摇出了第一次摇的点数，玩家胜；
# 其他点数玩家继续摇骰子，直到分出胜负
# 我们设定游戏开始时玩家有1000元，游戏结束的条件是玩家破产
'''
money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    go_on = False
    # 下注金额必须大于0小于等于玩家总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 第一次摇色子
    # 用1到6均匀分布的随机数模拟摇色子得到的点数
    first = randint(1, 6) + randint(1, 6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
        money -= debt
    else:
        go_on = True
    # 第一次摇色子没有分出胜负游戏继续
    while go_on:
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜!\n')
            money -= debt
        elif current == first:
            print('玩家胜!\n')
            money += debt
        else:
            go_on = True
print('你破产了, 游戏结束!')
'''
''' ========== 斐波那契数列前20个数 ========== '''
# 前连个数都是1
a, b = 1, 1
print(a, b, end=' ')
# 通过递推公式算出后面的18个数
for _ in range(18):
    a, b = b, a + b
    print(b, end=' ')

''' ========== 打印素数-输出100内的素数 ========== '''
# 素数指只能被1和自身整除的正整数（不包括1）
for num in range(2, 100):
    # 假设num是素数
    is_prime = True
    # 在2到num-1之间找num的因子
    for factor in range(2, num):
        # 如果找到了num的因子，num就不是素数
        if num % factor == 0:
            is_prime = False
            break
    # 如果布尔值为True在num是素数
    if is_prime:
        print(num)

