#
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

from urllib import request
from urllib import parse
import chardet
url = "http://www.baidu.com/s"
word = {"wd":"长城"}
word = parse.urlencode(word) #转换成 url 编码格式（字符串）
newurl = url + "?" + word # url 首个分隔符就是 ?

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

req = request.Request(newurl, headers=headers)
response = request.urlopen(req)
html = response.read()
charset = chardet.detect(html)['encoding']
print(charset)
print(html.decode(charset))
print(req.get_header("User-agent"))
