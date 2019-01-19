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
str = 'abbbc'
# 贪婪模式
pattern = re.compile(r'ab*') # * 决定了尽可能多匹配 b,结果是abbb
result = pattern.match(str)
print(result.group())

# 非贪婪模式
pattern = re.compile(r'ab*?') # *? 决定了尽可能少匹配 b，结果是a
result = pattern.match(str)
print(result.group())

pattern = re.compile(r'ab+?') # *? 决定了尽可能少匹配 b，结果是ab
result = pattern.match(str)
print(result.group())

# 贪婪模式
str = "aa<div>test1</div>bb<div>test2</div>cc"
pattern = re.compile(r'<div>.*</div>') #* 决定了尽可能多匹配 b,结果是<div>test1</div>bb<div>test2</div>
result = pattern.search(str)
print(result.group())

# 非贪婪模式
str = "aa<div>test1</div>bb<div>test2</div>cc"
pattern = re.compile(r'<div>.*?</div>') # *? 决定了尽可能少匹配 b，结果是<div>test1</div>
result = pattern.search(str)
print(result.group())