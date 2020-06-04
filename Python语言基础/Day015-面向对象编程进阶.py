"""
可见性和属性装饰器
在很多面向对象编程语言中，对象的属性通常会被设置为私有(private)或受保护(protected)的成员，就是不允许直接访问这些属性；
对象的方法通常都是公开的(public)，因为公开的方法是对象能够接受的消息，也是对象暴露给外界的调用接口，这就是访问可见性。
在python中可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性，如可以用__name表示一个私有属性，_name表示一个
受保护属性
"""


class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('张三', 20)
stu.study('python程序设计')
print(stu._Student__name, stu._Student__age)

"""
python中可以通过property装饰器为私有属性提供读取和修改的方法，装饰器通常会放在类、函数或方法的声明之前，通过一个@符号
表示将装饰器应用于类、函数或方法。
"""


class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 属性访问器(getter方法)-获取__name属性
    @property
    def name(self):
        return self.__name

    # 属性修改器(setter方法)-修改__name属性
    @name.setter
    def name(self, name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为无名氏，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'

    @property
    def age(self):
        return self.__age


stu = Student('李四', 20)  # 李四 20
print(stu.name, stu.age)
stu.name = ''  # 无名氏
print(stu.name)

''' ========== 动态属性 ========== '''


# 在python中我们可以动态为对象添加属性。对象的方法其实本质上也是对象的属性，如果给对象发送一个无法接收的消息，引发的
# 异常仍然是AttributeError
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王五', 20)
# 为Student对象添加sex属性
stu.sex = '男'
print(stu.name, stu.age, stu.sex)
# 如果不希望在使用对象时动态的为对象添加属性，可以使用__slots__。可以在类中指定__slots__ = ('name', 'age')
# 这样对象只能有name和age属性，如果动态添加其他属性将会引发异常

''' ========== 静态方法和类方法 ========== '''


class Triangle(object):
    """三角形类"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形（静态方法）"""
        return a + b > c and b + c > a and a + c > b

    # @classmethod
    # def is_valid(cls, a, b, c):
    #   """判断三条边长能否构成三角形（类方法）"""
    #   return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


# 上面代码使用staticmethod装饰器声明了is_valid方法是Triangle类的静态方法，如果要声明类方法可以使用classmethod
# 可以直接使用类名.方法名的方式来调用静态方法和类方法，二者区别在于类方法的第一个参数是类对象本身，而静态方法则没有这个参数
# 对象方法、类方法、静态方法都可以通过类名.方法名的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有
# 接收消息的对象。静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定


''' ========== 继承和多态 ========== '''
'''
面向对象的编程语言支持在已有类的基础上创建新类，从而减少重复代码的编写。提供继承信息的类叫做父类（超类、基类），得到继承
信息的类叫做子类（派生类、衍生类）。
'''


class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生类"""

    def __init__(self, name, age):
        # super(Student, self).__init__(name, age)
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师类"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')


stu1 = Student('李元芳', 30)
stu2 = Student('狄仁杰', 50)
teacher = Teacher('武则天', 70, '皇帝')
stu1.eat()
stu2.sleep()
teacher.teach('攻打突厥方略')
stu1.study('兵法')
"""
继承的语法是在定义类的时候在类名后的圆括号中指定当前类的父类。在子类的初始化方法中可以通过super().__init__()来调用
父类初始化方法，super函数是python内置函数中专门为获取当前对象的父类对象而设计的。
"""

