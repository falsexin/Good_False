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
from urllib import request
import re
import chardet

def down(url):
    head = {}
    #写入User Agent信息
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #创建Request对象
    req = request.Request(url, headers=head)
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)
    #print(charset)
    print(charset['encoding'])
    html = html.decode(charset['encoding'])
    return html


if __name__ == "__main__":
    # 获取超链接<a>和</a>之间内容
    url = "https://www.baidu.com/"
    html = down(url)
    pat = re.compile(r'<a .*?><span></span>(.*?)</a>',re.M|re.S)
    texts = pat.findall(html)
    for t in texts:
        print(t)
        #print(unicode(t, 'utf-8'))