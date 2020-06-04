from enum import Enum
import random
from abc import ABCMeta, abstractmethod

""" ========== 案例1：扑克游戏 ========== """


# 扑克有52张牌，将52张牌发到4个玩家手上，每个玩家手上有13张牌，按照黑桃、红心、草花、方块的顺序和点数从小到大排列

class Suite(Enum):
    """花色（枚举）"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


# 定义枚举类型其实就是定义符号常量，如SPADE/HEART等，每个符号常量都有与之对应的值，这样表示黑桃就可以不用数字0
# 而是用Suite.SPADE.
# python的枚举类型是可迭代类型，就是可以将枚举类型放到for-in循环中，依次取出每个符号常量及其对应的值

for suite in Suite:
    print(f'{suite}: {suite.value}')


class Card:
    """定义牌类"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suite = '♠♥♣♦'
        face = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # 根据牌的花色和点数取到对应的字符
        return f'{suite[self.suite.value]}{face[self.face]}'

    def __lt__(self, other):
        """花色相同比较点数的大小"""
        if self.suite == other.suite:
            return self.face < other.face
        """花色不同比较花色对应的值"""
        return self.suite.value < other.suite.value


# 通过下面代码测试下card类
card1 = Card(Suite.SPADE, 5)
card2 = Card(Suite.HEART, 13)
print(card1, card2)  # ♠5 ♥K


class Poker(object):
    """定义扑克类"""

    def __init__(self):
        # 通过列表的生成式语法创建一个装52张牌的列表
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        # current属性表示发牌的位置
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        # 通过random模块的shuffle函数实现列表的随机排序
        random.shuffle(self.cards)

    def deal(self):
        """发牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """还有没有牌可以发"""
        return self.current < len(self.cards)


# 通过下面代码测试Poker类
poker = Poker()
poker.shuffle()
print(poker.cards)


class Player(object):
    """定义玩家类"""

    def __init__(self, name):
        self.name = name
        self.cards = []

    def get_one(self, card):
        """摸牌"""
        self.cards.append(card)

    def arrange(self):
        self.cards.sort()


# 创建4个玩家，并将牌发到玩家手上
poker = Poker()
poker.shuffle()
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)

''' ========== 案例2：工资结算系统 ========== '''
"""
某公司有三种类型的员工，分别是部门经理、程序员、销售员。需要设计一个工资结算系统，根据提供的员工信息来计算员工的月薪
其中部门经理月薪固定15000，程序员按工作时间支付月薪，每小时200元，销售员的月薪由1800元底薪加上销售额5%的提成构成
"""
'''
通过对上述需求的分析，可以看出部门经理、程序员、销售员都是员工，有相同的属性和行为。那么可以先设计一个名为Employee
的父类，在通过继承的方式从这个父类派生出部门经理、程序员和销售员三个子类。很显然，后续的代码不会创建Employee类的对象，
因为我们需要的是具体的员工对象，所以这个类可以设计成专门用于继承的抽象类。python中没有定义抽象类的关键字，但是可以通过abc
模块中名为ABCMeta的元素来定义抽象类
'''


class Employee(metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """结算月薪"""
        pass


# 在员工类中，get_salary方法用于结算月薪，但是由于还没有确定是哪一类员工，所以结算月薪虽然是员工的公共行为但这里却没有
# 办法实现。对于暂时无法实现的方法我们可以使用abstractmethod装饰器将其声明为抽象方法。
# 所谓抽象方法就是只有声明没有实现的方法，声明这个方法是为了让子类去重写这个方法

class Manager(Employee):
    """定义部门经理类"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """定义程序员类"""

    def __init__(self, name, working_hour=0):
        super().__init__(name)
        self.working_hour = working_hour

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Employee):
    """定义销售员类"""

    def __init__(self, name, sales=0):
        super().__init__(name)
        self.sales = sales

    def get_salary(self):
        return 1800 + self.sales * 0.05


# 上面的Manage、Programma、Salesman三个类都继承自Employee，三个类都分别重写了get_salary方法。
# 重写就是子类对父类已有的方法重新作出实现。
# 三个子类中的get_salary各不相同，运行时会产生多态行为--调用相同的方法，不同的子类对象做不同的事情

emps = [
    Manager('刘备'), Programmer('诸葛亮'), Salesman('关云长'),
    Manager('曹操'), Programmer('郭嘉'), Programmer('曹仁')
]
for emp in emps:
    if isinstance(emp, Programmer):
        emp.working_hour = int(input(f'请输入{emp.name}本月工作时间：'))
    elif isinstance(emp, Salesman):
        emp.sales = float(input(f'请输入{emp.name}本月销售额：'))
    print(f'{emp.name}本月工资为：￥{emp.get_salary():.2f}元')
