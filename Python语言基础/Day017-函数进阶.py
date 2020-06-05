""" ========== 关键字参数 ========== """


# 在调用函数传入参数时，可以指定参数名，也可以不指定参数名
def can_form_triangle(a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


# 调用函数传入参数不指定参数名按位置对号入座
print(can_form_triangle(1, 2, 3))
# 调用函数通过“参数名=参数值” 的形式按顺序传入参数
print(can_form_triangle(a=1, b=2, c=3))
# 调用函数通过“参数名=参数值”的形式不按顺序传入参数
print(can_form_triangle(c=3, a=1, b=2))


# 调用函数时如果希望调用者必须以 参数名=参数值 的方式传参，可以用命名关键字参数取代位置参数。
# 命名关键字参数，是在函数的参数列表中，写在 * 之后的参数
def can_form_triangle(*, a, b, c):  # * 是一个分隔符，*前面的参数都是位置参数，*后面的参数就是命名关键字参数
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and a + c > b and b + c > a


# print(can_form_triangle(3, 4, 5))  # TypeError: can_form_triangle() takes 0 positional arguments but 3 were given
# 传参时必须使用 参数名=参数值 的方式，位置不重要
print(can_form_triangle(c=5, b=4, a=3))


# 函数的参数列表中可以使用可变参数*args来接收任意数量的参数，但是不能处理带参数名的参数
# 在设计函数时，如果既不知道调用者会传入的参数个数，也不知道调用者会不会指定参数名，那么同时使用可变参数和关键字参数
# 关键字参数会将传入的带参数名的参数组装成一个字典，参数名就是字典中键值对的键，而参数值就是字典中键值对的值
def calc(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result


print(calc())  # 0
print(calc(1, 2, 3))  # 6
print(calc(a=1, b=2, c=3))  # 6
print(calc(1, 2, c=3, d=4))  # 10
# 不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前

''' ========== 高阶函数用法 ========== '''


# 函数本身也可以作为函数的参数或返回值，这就是所谓的高阶函数
def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        result = op(result, arg)
    for value in kwargs.values():
        result = op(result, value)
    return result


# init_value代表运算的初始值，op代表二元运算函数
def add(x, y):
    return x + y


def mul(x, y):
    return x * y


print(calc(1, 2, 3, init_value=0, op=add, x=4, y=5))  # 15
print(calc(1, 2, x=3, y=4, z=5, init_value=1, op=mul))  # 120

'''去掉一个整数列表中的奇数，并对所有的偶数求平方得到一个新的列表，可以使用filter和map函数，filter可以实现对序列中
元素的过滤，map可以实现对序列中元素的映射'''


def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)  # [144, 64, 3600, 2704]

# 可以使用列表生成式
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers2)  # [144, 64, 3600, 2704]
