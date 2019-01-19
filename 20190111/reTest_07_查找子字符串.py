"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/7/12'
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
content = '''<div><a href="#">锚点</a></div>'''
start = content.find(r'<a href="#">') + len(r'<a href="#">') #起点位置
end = content.find(r'</a>')              #重点点位置
infobox = content[start:end]
print(infobox)




