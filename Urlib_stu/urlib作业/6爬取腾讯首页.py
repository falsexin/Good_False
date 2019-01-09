#
# @Time    : 2019/1/7 18:57
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 6爬取腾讯首页.py
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

# 从西刺网查找代理ip，通过代理ip爬取腾讯首页，打印爬取内容
from urllib import request
from urllib import parse
import chardet
import zlib

if __name__ == "__main__":
    url='https://www.qq.com/'
    req = request.Request(url)
    # 这是代理 IP
    proxy = {'http': '119.101.116.245:9999'}

    # 创建 ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    # 创建 Opener
    opener = request.build_opener(proxy_support)
    # 添加 User Angent
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')]
    # 安装 OPener
    request.install_opener(opener)
    # 使用自己安装好的 Opener
    response = request.urlopen(req, timeout=120)
    html = response.read()
    encoding = response.info().get('Content-Encoding')
    print(encoding)
    if encoding == 'gzip':
        html = zlib.decompress(html, 16+zlib.MAX_WBITS)
    elif encoding == 'deflate':
        try:
            html = zlib.decompress(html, -zlib.MAX_WBITS)
        except zlib.error:
            html = zlib.decompress(html)
    charset = chardet.detect(html)["encoding"]
    html = html.decode('gb2312','ignore')
    file_name = r"E:\Good_False\Urlib_stu\urlib作业\腾讯首页"  + ".html"

    with open(file_name, "w", encoding='gb2312') as file:
        file.write(html)
