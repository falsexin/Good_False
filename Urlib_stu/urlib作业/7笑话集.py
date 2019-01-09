#
# @Time    : 2019/1/7 19:21
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 7笑话集.py
# @Software: PyCharm
#  ......................我佛慈悲......................
#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -卍-|||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
#
# ..................佛祖开光 ,永无BUG...................
# ..................佛祖保佑，永不加班...................
# 爬取http://www.jokeji.cn/hot.htm笑话集，获取页面编码，保存html文件(爬取5页）

from urllib import request
from urllib import parse
import chardet


url = 'http://www.jokeji.cn/hot.htm'
req = request.Request(url)
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)

url = 'http://www.jokeji.cn/hot.asp'
for i in range(1,6):
    newurl = url + '?' + 'me_page=' + str(i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
        like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    req = request.Request(newurl, headers=headers)
    response = request.urlopen(req)
    html = response.read()
    html = html.decode(charset, 'ignore')
    file_name = r"E:\Good_False\Urlib_stu\urlib作业\笑话集_page" + str(i) + ".html"
    print(file_name)
    with open(file_name, "w", encoding=charset) as file:
        file.write(html)