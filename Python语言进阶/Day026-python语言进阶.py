import heapq
import itertools
from collections import *

""" ================== 重要知识点 ================== """

""" ========== 生成式（推导式）的用法 ========== """
# 生成式可以用来生成列表、集合和字典
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.98,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ANC': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: value for key, value in prices.items() if value > 100}
print(prices2)


""" ========== 嵌套的列表 ========== """
'''
names = ['关云长', '张翼德', '赵子龙', '马孟起', '黄汉升']
courses = ['春秋', '汉书', '战国策']
# 录入5个人三门课程的成绩
scores = [[None] * len(courses) for _ in range(len(names))]
for row, name in enumerate(names):
    for col, course in enumerate(courses):
        scores[row][col] = float(input(f'请输入{name}的{course}成绩：'))
        print(scores)
'''

""" ========== heapq 模块（堆排序） ========== """
# 从列表中找出最大的或最小的N个元素。堆结构（大根堆/小根堆）
list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {"name": 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# list1中最大的三个元素
print(heapq.nlargest(3, list1))  # [99, 92, 88]
# list1中最小的三个元素
print(heapq.nsmallest(3, list1))  # [12, 25, 34]
# list2中price元素最大的2组
print(heapq.nlargest(2, list2, key=lambda x: x['price']))
# list2中shares元素最大的2组
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))


''' ========== 迭代工具模块 iteratools 模块 ========== '''
# 产生ABCD的全排列
itertools.permutations('ABCD')
# 产生ABCDE的五选三组合
itertools.combinations('ABCDE', 3)
# 产生ABCE和123的笛卡尔积
itertools.product('ABCD', '123')
# 产生ABC的无限循环序列
itertools.cycle(('A', 'B', 'C'))


""" ========== collections 模块 ========== """
'''
常用的工具类：
namedtuple：命令元组，它是一个工厂类，接受类型的名称和属性列表来创建一个类
deque：双端队列，是列表的替代实现。python中的列表底层是基于数组来实现的，而deque底层是双向链表，因此当你需要在头尾添加和
删除元素时，deque会表现出更好的性能
Counter：dict的子类，键是元素，值是元素的计数，它的most_common()方法可以帮助我们获取出现频率最高的元素
OrderedDict：dict的子类，它记录了键值对插入的顺序，看起来既有字典的行为，也有链表的行为
defaultdict：类似于字典的类型，但是可以通过默认的工厂函数来获得键对应的默认值，相比字典中的setdefault()方法，这种做法
更加高效
'''
# 找出序列中出现次数最多的元素
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print(counter.most_common(3))