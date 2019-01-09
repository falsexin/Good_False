"""
__title__ = ''
__author__ = 'Thompson'
__mtime__ = '2018/9/26'
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
from urllib import request

url = 'http://imgsrc.baidu.com/forum/w%3D580/sign=781a1507c595d143da76e42b43f18296/6213bba1cd11728b7dad7526c5fcc3cec2fd2cc1.jpg'
headers = {'User-Agent': 'Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)'}
req = request.Request(url,headers=headers)
repsonse = request.urlopen(req)
with open('./images/img.jpg','wb') as file:
    file.write(repsonse.read())
