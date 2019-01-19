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

import re


if __name__ == "__main__":
    content = '''
    <html>
<head><title>表格</title></head>
<body>
    <table  border=1>
        <tr><th>学号</th><th>姓名</th></tr>
        <tr><td>1001</td><td>李白</td></tr>
        <tr><td>1002</td><td>杜甫</td></tr>
    </table>
</body>
</html>
    '''
    # 获取<tr></tr>间内容
    res = r'<tr>(.*?)</tr>'
    texts = re.findall(res, content, re.S | re.M)
    print('len:',len(texts))
    for m in texts:
        print(m)

    # 获取<th></th>间内容
    for m in texts:
        res_th = r'<th>(.*?)</th>'
        m_th = re.findall(res_th, m, re.S | re.M)
        for t in m_th:
            print(t)

    # 直接获取<td></td>间内容
    res = r'<td>(.*?)</td>'
    texts = re.findall(res, content, re.S | re.M)
    for m in texts:
        print(m)



