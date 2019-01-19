"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/30'
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

str1 = '神州10号发射成功'
re_str = '神州\d+号发射成功'

ret = re.match(re_str,str1)
print(ret.group())

ls = ['神州1号发射成功','神州2号发射成功','神州3号发射成功','神州4号发射成功']
pat1 = re.compile(re_str)
pat2 = re.compile('神州(\d+)号发射成功')
print(type(pat1))
for item in ls:
    # print(pat1.match(item).group())
    print(pat2.match(item).group())

mat = pat2.match(str1)
print(type(mat))
print(mat)
print(mat.group())
print(mat.start())
print(mat.end())
print(mat.span())

print(mat.group(1))
print(mat.start(1))
print(mat.end(1))
print(mat.span(1))

#忽略大小写
s = 'hello World!'
regex = re.compile("hello world!", re.I)
print(regex.match(s).group())
#匹配换行
s = '''first line
second line
third line'''
#
regex = re.compile(".+")
print(regex)
print(regex.search(s).group())
print(regex.findall(s))
# re.S
regex_dotall = re.compile(".+", re.S)
print(regex_dotall.findall(s))

