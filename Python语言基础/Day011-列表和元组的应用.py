from random import randint, sample

""" ========== 成绩表和平均分统计 ========== """
'''
# 录入5个学生3门课程的考试成绩，计算每个学生的平均分和每个课程的平均分
names = ['云长', '翼德', '子龙', '汉升', '孟起']
courses = ['语文', '数学', '英语']
# 用生成式创建嵌套的列表保存5个人3门课程的成绩
scores = [[0] * len(courses) for _ in range(len(names))]
# 录入数据
for i, name in enumerate(names):
    print(f'请输入{name}的成绩 ===>')
    for j, course in enumerate(courses):
        scores[i][j] = float(input(f'{course}: '))
print()
print('-' * 5, '学生平均成绩', '-' * 5)
# 计算每个人的平均成绩
for index, name in enumerate(names):
    avg_score = sum(scores[index]) / len(courses)
    print(f'{name}的平均成绩为: {avg_score:.1f}分')
print()
print('-' * 5, '课程平均成绩', '-' * 5)
# 计算每门课的平均成绩
for index, course in enumerate(courses):
    # 用生成式从scores中取出指定的列创建新列表
    curr_course_scores = [score[index] for score in scores]
    avg_score = sum(curr_course_scores) / len(names)
    print(f'{course}的平均成绩为：{avg_score:.1f}分')
'''
# 上面对列表遍历的时候使用了enumerate函数
# 循环遍历列表的两种方法，一种是通过索引循环遍历，一种是直接遍历列表元素
# 通过enumerate处理后的列表在循环遍历时会取到一个二元组，解包之后第一个值是索引，第二个值是元素
items = ['python', 'java', 'Go']
for index in range(len(items)):
    print(f'{index}: {items[index]}')

for index, item in enumerate(items):
    print(f'{index}: {item}')

''' ========== 设计一个函数返回指定日期是这一年的第几天 ========== '''


def is_leap_year(year):
    # 判断指定的年份是不是闰年，平年返回False，闰年返回True
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    '''
    计算传入的日期是这一年的第几天
    :param year: 年
    :param month: 月
    :param date: 日
    :return:
    '''
    # 用嵌套的列表保存平年和闰年每个月的天数
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ]
    # 布尔值False和True可以转换成整数0和1，因此，平年会选中嵌套列表中的第一个列表(2月是28天)
    # 闰年会选中嵌套列表中的第二个列表
    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date


print(which_day(2018, 1, 5))

''' ========== 实现双色球随机选号 ========== '''


# 用一个列表保存红色球的号码，然后通过random模块的sample函数实现无放回抽样，这样就可以抽中6个不重复的红色球号码
# 红色球需要排序，可以使用列表的sort方法，显示时1位数前面需要做补0的操作，可以用字符串格式化的方式来处理
def display(balls):
    # 输出列表中的双色球号码
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end='')
        print(f'{ball:0>2d}', end=' ')
    print()


def random_select():
    # 随机选择一组号码
    # 用生成式生成1到33号的红色球
    red_balls = [x for x in range(1, 34)]
    # 通过无放回随机抽样的方式选中6个红色球
    selected_balls = sample(red_balls, 6)
    # 对红色球进行排序
    selected_balls.sort()
    # 用1到16的随机数表示选中的蓝色球并追加到列表中
    selected_balls.append(randint(1, 16))
    return selected_balls


n = int(input('机选几注：'))
for _ in range(n):
    display(random_select())
