""" ============== 分支结构-if语句使用 ================= """
# ============ 用户身份验证 ==============
username = input("请输入用户名：")
password = input("请输入密码：")
# 用户名是admin并且密码是123456则身份验证成功，否则身份验证失败
if username == "admin" and password == "123456":
    print("身份验证成功！")
else:
    print("身份验证失败！")

# ============ 分段函数求值 =============
# 推荐使用第一种扁平化的代码格式，能使用扁平化结构时就不要使用嵌套结构
x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
elif x >= -1:
    y = x + 2
else:
    y = 5 * x + 3
print(f'f({x}) = {y}')

# 嵌套的分支结构
x = float(input("x = "))
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(f"f({x}) = {y}")


'''
例子：输入三条边长，如果能构成三角形就计算周长和面积
'''
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a + b > c and a + c > b and b + c > a:
    peri = a + b + c
    print(f"周长：{peri}")
    half = peri / 2
    area = (half * (half - a) * (half - b) * (half - c)) ** 0.5
    print(f"面积：{area}")
else:
    print("不能构成三角形")

