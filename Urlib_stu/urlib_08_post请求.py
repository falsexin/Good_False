#
# @Time    : 2019/1/7 16:28
# @Author  : Mat
# @欣      ：Very Cool
# @File    : urlib_08_post请求.py
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

from urllib import request
from urllib import parse
import json
if __name__ == "__main__":
    #对应上图的 Request URL 为避免{"errorCode":50}的错误，去除 url 中的_o
    #Request_URL = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #创建 Form_Data 字典，存储上图的 Form Data
    Form_Data = {}
    Form_Data['i'] = 'Tom'
    Form_Data['from'] = 'AUTO'
    Form_Data['to'] = 'AUTO'
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1526796477689'
    Form_Data['sign'] = 'd0a17aa2a8b0bb831769bd9ce27d28bd'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'
    Form_Data['typoResult'] = 'false'
    #使用 urlencode 方法转换标准格式
    data = parse.urlencode(Form_Data).encode('utf-8')
    head = {}
    # 写入 User Agent 信息
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 创建 Request 对象
    req = request.Request(Request_URL, headers=head)
    # 传递 Request 对象和转换完格式的数据
    response = request.urlopen(req, data=data)
    # 读取信息并解码
    html = response.read().decode('utf-8')
    # 使用 JSON
    translate_results = json.loads(html)
    print(translate_results)
    # 找到翻译结果
    translate_results = translate_results['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是： %s" % translate_results)



