#
# @Time    : 2019/1/7 19:32
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 8云起书院.py
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

# 爬取云起书院http://yunqi.qq.com/bk,要求设置UA，爬取前5页，
# 把内容保存在.\data\yunqi_*.txt文件中(爬取5页）

from urllib import request
from urllib import parse
import chardet


url = 'http://yunqi.qq.com/bk'
req = request.Request(url)
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)

url = 'http://yunqi.qq.com/bk/so2/n10p'
for i in range(1,6):
    newurl = url  + str(i)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
        like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    req = request.Request(newurl, headers=headers)
    response = request.urlopen(req)
    html = response.read()
    # encoding = response.info().get('Content-Encoding')
    # print(encoding)

    html = html.decode(charset, 'ignore')
    file_name = r"E:\Good_False\Urlib_stu\urlib作业\云起书院_page" + str(i) + ".html"
    print(file_name)
    with open(file_name, "w", encoding=charset) as file:
        file.write(html)

