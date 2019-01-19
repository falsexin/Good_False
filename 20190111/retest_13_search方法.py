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
pattern = re.compile('(\d)\d')
m = pattern.search('one12twothree34four')  # 这里如果使用 match 方法则不匹配
print(m.group())
m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
print(m.group())
print(m.span())
