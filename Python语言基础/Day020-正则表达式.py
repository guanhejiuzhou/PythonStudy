import re

"""
正则表达式是一种工具，它定义了字符串的匹配模式，如何检查一个字符串是否有跟某种模式匹配的部分或者从一个字符串中将与模式匹配的
部分提取出来或者替换掉。
正则表达式中的一些基本符号
符号      |解释               |示例                  |说明
.        |匹配任意字符         |b.t                  |可以匹配到bat/but/b#t/b1t等
\w       |匹配字母、数组、下划线 |b\wt                 |可以匹配到bat/b1t/b_t等，但不能匹配b#t
"""
"""
python对正则表达式的支持
python提供了re模块来支持正则表达式相关操作，re模块的核心函数如下
|函数                                       |说明
|compile(pattern, flags=0)                 |编译正则表达式返回正则表达式对象
|match(pattern, string, flags=0)           |用正则表达式匹配字符串成功返回匹配对象，否则返回None
|search(pattern, string, flags=0)          |搜索字符串中第一次出现正则表达式的模式，成功返回匹配对象，否则返回None
|split(pattern,string,maxsplit=0,flags=0)  |用正则表达式指定的模式分隔符拆分字符串，返回列表
|sub(pattern,repl,string,count=0,flags=0)  |用指定的字符串替换原字符串中与正则表达式匹配的模式，可以用count指定替换的次数
|fullmatch(pattern,string,flags=0)         |match函数的完全匹配，从字符串开头到结尾
|findall(pattern,string,flags=0)           |查找字符串所有与正则表达式匹配的模式，返回字符串的列表
|finditer(pattern,string,flags=0)          |查找字符串所有与正则表达式匹配的模式，返回一个迭代器
|purge()                                   |清除隐式编译的正则表达式的缓存
|re.I / re.IGNORECASE                      |忽略大小写匹配标记
|re.M / re.MULTILINE                       |多行匹配标记
"""

''' 验证输入用户名和QQ号是否有效并给出对应的提示信息'''


# 用户名必须由字母、数字或下划线构成且长度在6-20个字符之间，QQ号是5-12的数字且首位不能为0
def main():
    username = input('请输入用户名：')
    qq = input('请输入QQ号：')
    # match函数的第一个参数是正则表达式字符串或正在表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6-20}$', username)
    if not m1:
        print('请输入有效的用户名.')
    m2 = re.match(r'^[1-9]\d{5,12}$', qq)
    if not m2:
        print('请输入有效的QQ号.')
    if m1 and m2:
        print('输入的信息有效!')


if __name__ == '__main__':
    main()
