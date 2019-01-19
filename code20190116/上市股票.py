#
# @Time    : 2019/1/16 9:21
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 豆瓣.py
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

import requests
import json
import pymysql
conn = pymysql.connect(host='localhost', port=3306, db='gupiao', user='root', passwd='123456')
cur = conn.cursor(cursor=pymysql.cursors.DictCursor)

def crawl(type, page):
    base_url = 'http://query.sse.com.cn/security/stock/getStockListData2.do'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,\
    like Gecko) Chrome/51.0.2704.103 Safari/537.36",
        "Cookie": "yfx_c_g_u_id_10000042=_ck19011609462714324252417931089; VISITED_MENU=%5B%228451%22%2C%228528%22%5D; yfx_f_l_v_t_10000042=f_t_1547603187417__r_t_1547603187417__v_t_1547603726697__r_c_0",
        "Referer": "http://www.sse.com.cn/assortment/stock/list/share/"
    }
    for i in range(1,page+1):
        print('第'+ str(i)+'页数据:')
        keywords = {
            'jsonCallBack': 'jsonpCallback20624',
            'isPagination': 'true',
            'stockCode':'',
            'csrcCode':'',
            'areaName':'',
            'stockType': str(type),
            'pageHelp.cacheSize': '1',
            'pageHelp.beginPage': str(i),
            'pageHelp.pageSize': '25',
            'pageHelp.pageNo': str(i),
            'pageHelp.endPage': str(i)+'1',
            '_' : '1547603727095'
        }

        response = requests.get(base_url, params=keywords, headers=headers )
        print(response.text)
        return 0
        a = '{"data":' + response.text[18:].replace('(', '[').replace(')', ']}')
        if response.status_code == 200:

            data = json.loads(a)['data']
            # print(data[0]['pageHelp']['data'])
            data = data[0]['pageHelp']['data']
            for item in data:
                print('公司代码:', item['COMPANY_CODE'])
                print('公司简称:', item['COMPANY_ABBR'])
                if type == 1:
                    print('A股代码:', item['SECURITY_ABBR_A'])
                    print('A股简称:', item['SECURITY_CODE_A'])
                    print('A股总资本:', item['totalShares'])
                    print('A股流通资本:', item['totalFlowShares'])
                    cur.executemany('insert into A_gu values(%s,%s,%s,%s,%s,%s)', [(item['COMPANY_CODE'],
                                                                                    item['COMPANY_ABBR'],
                                                                                    item['SECURITY_ABBR_A'],
                                                                                    item['SECURITY_CODE_A'],
                                                                                    item['totalShares'],
                                                                                    item['totalFlowShares']
                                                                                    )])
                elif type == 2:
                    print('B股代码:', item['SECURITY_ABBR_B'])
                    print('B股简称:', item['SECURITY_CODE_B'])
                    print('B股总资本:', item['totalShares'])
                    print('B股流通资本:', item['totalFlowShares'])
                    cur.executemany('insert into A_gu values(%s,%s,%s,%s,%s,%s)', [(item['COMPANY_CODE'],
                                                                                    item['COMPANY_ABBR'],
                                                                                    item['SECURITY_ABBR_B'],
                                                                                    item['SECURITY_CODE_B'],
                                                                                    item['totalShares'],
                                                                                    item['totalFlowShares']
                                                                                    )])

                conn.commit()
                print('--'*40)
if __name__ == '__main__':
    print('a股 1 ， b 股 2')
    type = int(input('请输入你要获取的股票类型:'))
    page = int(input('请输入你要获取几页数据:'))
    crawl(type, page)
cur.close()
conn.close()