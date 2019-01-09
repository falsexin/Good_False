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
if __name__ == "__main__":


    #访问网址
    # url = 'http://www.baidu.com/'
    url='http://ip.27399.com/'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 创建 Request 对象
    req = request.Request(url, headers=head)
    #这是代理 IP
    proxy = {'http':'119.101.116.245:9999'}
    #创建 ProxyHandler
    proxy_support = request.ProxyHandler(proxy)
    #创建 Opener
    opener = request.build_opener(proxy_support)
    #添加 User Angent
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')]
    # 安装 OPener
    request.install_opener(opener)
    # 使用自己安装好的 Opener
    response = request.urlopen(req)
    # 读取相应信息并解码
    html = response.read().decode("utf-8")
    print('file.getcode,HTTPResponse类型:', response.getcode)
    print('file.info 返回当前环境相关的信息：', response.info(),type(response.info()))
    a = response.info().get('Content-Type')
    print(a)
    print(req.get_header("User-agent"))
    # 打印信息
    # print(html)