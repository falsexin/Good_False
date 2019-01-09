#
# @Time    : 2019/1/7 17:33
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 5批量爬取贴吧数据.py
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


# 输入贴吧名称， 起始页码， 结束页码， 爬取贴吧数据， 以‘第x页.html’ 命名， 保存为html 文件

from urllib import request
from urllib import parse
import chardet



tieba_name = input('请输入贴吧名称：')
tieba_start_page = int(input('请输入贴吧起始页码：'))
tieba_end_page = int(input('请输入贴吧结束页码：'))

# url = 'https://tieba.baidu.com/f?kw=lol&ie=utf-8&pn=50'
url = "http://tieba.baidu.com/f"
word = {"kw":tieba_name, 'ie':'utf-8'}
word = parse.urlencode(word) #转换成 url 编码格式（字符串）
print(word)
for i in range(tieba_start_page-1, tieba_end_page):
    pn = (i)*50
    newurl = url + "?" + word + '&' + 'pn=' + str(pn)
    print(newurl)
    headers = {"User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"}
    # req = request.Request(newurl, headers=headers)
    req = request.Request(newurl)
    response = request.urlopen(req)
    html = response.read()
    charset = chardet.detect(html)['encoding']
    print(charset)
    encoding = response.info().get('Content-Encoding')
    print(encoding)
    print(req.get_header("User-agent"))
    html = html.decode('utf-8', 'ignore')
    # print(html)
    file_name = r"E:\Good_False\Urlib_stu\urlib作业\pange" + str(i+1) + ".html"
    print(file_name)
    with open(file_name, "wb") as file:
        file.write(html)







