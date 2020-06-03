import time

"""
面向对象编程：把一组数据和处理数据的方法组成对象，把行为相同的对象归纳为类，通过封装隐藏对象的内部细节，通过继承实现类的特
化和泛化，通过多态实现基于对象类型的动态分派。
类(class)和对象(object)：类是一个抽象的概念，对象是一个具体的概念。把同一类对象的共同特征抽取出来就是一个类。例如人类，
这是一个抽象概念，而我们每个人就是人类的这个抽象概念下的具体的实实在在的存在，也就是一个对象。简而言之，类是对象的蓝图和模板，
对象是类的实例。
面向对象编程中，一切皆为对象，对象都有属性和行为，每个对象都是独一无二的，而且对象一定属于某个类。
"""


# 定义类
# 在类的代码块中我们需要一些函数，这些函数就是我们对一类对象共同的动态特征的提取
# 写在类里面的函数我们称之为方法，方法就是对象的行为，也就是对象可以接收的消息。方法的第一个参数通常都是self，代表了接收这个消息的对象本身
class Student:
    # 定义方法
    def study(self, course_name):
        print(f'学生正在学习{course_name}.')

    # 定义方法
    def play(self):
        print(f'学生正在玩游戏')


# 创建和使用对象
# 定义好一个类之后，可以使用构造器语法来创建对象
stu1 = Student()
stu2 = Student()
print(stu1)
print(stu2)
print(hex(id(stu1)), hex(id(stu2)))
# 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')  # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu2.study('python程序设计')  # 学生正在学习python程序设计.
Student.play(stu1)  # 学生正在玩游戏
stu2.play()  # 学生正在玩游戏

''' ========== 初始化方法 ========== '''


# 通过给类添加__init__方法的方式为对象指定属性，同时完成对属性赋初始值的操作
# __init__方法通常也被称为初始化方法
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')


# 由于初始化方法除了self之外还有两个参数
# 调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student('张三', 30)
stu2 = Student('李四', 23)
stu1.study('python程序设计')  # 张三正在学习python程序设计.
stu2.play()  # 李四正在玩游戏.

''' ========== 打印对象 ========== '''


# 在打印对象的时候不希望看到对象的地址而是看到我们自定义的信息可以通过在类中放置__repr__
class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

    def __repr__(self):
        return f'{self.name}:{self.age}'


stu1 = Student('王五', 29)
print(stu1)  # 王五:29
students = [stu1, Student('张三', 14), Student('李四', 15)]
print(students)  # [王五:29, 张三:14, 李四:15]

''' ========== 例子1：定义一个类描述平面上的点，要求提供计算到另一个点距离的方法 ========== '''


class Point(object):
    """屏幕上的点"""

    def __init__(self, x=0, y=0):
        """
        初始化方法
        :param x:横坐标
        :param y:纵坐标
        """
        self.x, self.y = x, y

    def distance_to(self, other):
        """
        计算与另一个点的距离
        :param other:另一个点
        :return:
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Point(3, 5)
p2 = Point(6, 9)
print(p1, p2)
print(p1.distance_to(p2))

''' ========== 例子2：定义一个类描述数字时钟 ========== '''


class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法
        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        """走字"""
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'


# 创建时钟对象
clock = Clock(23, 59, 58)
while True:
    # 给时钟对象发消息读取时间
    print(clock.show())
    # 休眠1秒钟
    time.sleep(1)
    # 给时钟对象发消息使其走字
    clock.run()
