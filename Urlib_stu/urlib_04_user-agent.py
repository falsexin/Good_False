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
    #以 CSDN 为例， CSDN 不更改 User Agent 是无法访问的
    url = 'http://www.csdn.net/'
    head = {}
    # 写入 User Agent 信息
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ' \
                         '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    # 创建 Request 对象
    req = request.Request(url, headers=head)
    # 也可以通过调用 Request.add_header() 添加/修改一个特定的 header
    req.add_header("Connection", "keep-alive")
    # req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36")
    # 也可以通过调用 Request.get_header()来查看 header 信息
    print(req.get_header(header_name="Connection"))
    # print(req.get_header(header_name="User-Agent"))
    print(req.get_header("User-agent"))
    # 传入创建好的 Request 对象
    response = request.urlopen(req)
    # 读取响应信息并解码
    html = response.read().decode('utf-8')
    # 打印信息

    print('file.getcode,HTTPResponse类型:', response.getcode)
    print('file.info 返回当前环境相关的信息：', response.info())

    # print(html)