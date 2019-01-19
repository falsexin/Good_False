import requests
import json
import re

def crawl(index):
    base_url = 'http://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)'}
    keywords = {
        'page': '1',
        'num': '40',
        'sort': 'symbol',
        'asc': '1',
        'node': 'sh_a',
        'symbol': '',
        '_s_r_a': 'init'
    }
    response = requests.get(base_url, params=keywords, headers=headers)
    if response.status_code == 200:
        # print(response.text)
        data = response.text
        # print(data)
        # print(data.replace(':', '":').replace(',', ',"').replace('{', '{"'))
        a = data.replace(',', '","').replace('{', '{"').replace('}', '"}')
        b = re.sub('(:)', '":"', a)
        b = b.replace('[{"sy', '{"data": [{"sy').replace('"}]', '"}]}')
        # b = re.findall('(:)\d', a)
        # print(a)
        b = b.replace('""', '"').replace('}","{"symbol"', '},{"symbol"')
        b = re.sub('"ticktime"(.)*?,', '', b)
        # print(b)
        b = json.loads(b)
        # print(b['data'])
        data = b['data']
        for i in data:
            print('代码:', i['symbol'])
            print('名称:', i['name'])
            print('最新价:', i['trade'])
            print('涨跌额:', i['pricechange'])
            print('涨跌幅:', i['changepercent'])
            print('买入:', i['buy'])
            print('卖出:', i['sell'])
            print('昨收:', i['low'])
            print('今开:', i['open'])
            print('最高:', i['high'])
            print('最低:', i['low'])
            print('成交量/手:', i['volume'])
            print('成交额/万:', i['amount'])
            print('----'*30)

        # {symbol: "sh600000",
        #  name: "浦发银行",
        #  trade: "10.130",
        #  pricechange: "0.020",
        #  changepercent: "0.198",
        #  buy: "10.120",
        #  sell: "10.130",
        #  settlement: "10.110",
        #  open: "10.100",
        #  high: "10.150",
        #  low: "10.070",
        #  volume: 12988340,
        #  amount: 131354721,


if __name__ == '__main__':
    for i in range(3):
        crawl(i)