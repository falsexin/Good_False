"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/14'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import re
pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
m = pattern.match('Hello World Wide Web')

print(m)     # 匹配成功，返回一个 Match 对象
print(m.group(0))  # 返回匹配成功的整个子串
print(m.span(0))   # 返回匹配成功的整个子串的索引
print(m.group(1))  # 返回第一个分组匹配成功的子串
print(m.span(1))   # 返回第一个分组匹配成功的子串的索引
print(m.group(2))  # 返回第二个分组匹配成功的子串
print(m.span(2))   # 返回第二个分组匹配成功的子串
print(m.groups())  # 等价于 (m.group(1), m.group(2), ...)
#print(m.group(3))   # 不存在第三个分组 IndexError: no such group
