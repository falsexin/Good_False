"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/13'
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
from lxml import etree

html = etree.parse('./data/hello.html')
result = html.xpath('//li[last()-1]/a')
# text 方法可以获取元素内容
print(result[0].text)
result = html.xpath('//li[last()-1]/a/text()')[0]
# text 方法可以获取元素内容
print(result)
result = html.xpath('//h1//span/text()')
print(''.join(result).strip())