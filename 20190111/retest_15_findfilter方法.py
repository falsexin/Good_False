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
pattern = re.compile(r'\d+')

result_iter1 = pattern.finditer('hello 123456 789')
result_iter2 = pattern.finditer('one1two2three3four4', 0, 10)

print(type(result_iter1))
print(type(result_iter2))

print('result1...')
for m1 in result_iter1: # m1 是 Match 对象
    print(type(m1))
    print('matching string: {}, position: {}'.format(m1.group(), m1.span()))

print('result2...')
for m2 in result_iter2:
    print(type(m2))
    print('matching string: {}, position: {}'.format(m2.group(), m2.span()))

