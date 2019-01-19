#
# @Time    : 2019/1/16 15:22
# @Author  : Mat
# @欣      ：Very Cool
# @File    : TEST.py
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

# import re
# a = 'style="background-image: url("https://static.geetest.com/pictures/gt/5745c5f90/bg/4d35502cd.webp"); background-position: -1px 0px;"'
# # bg_url = re.findall('url\(\"(.*?)\"\); (.*?)und', a.replace('webp', 'jpg'))
# #
# # print(bg_url)
#
# fullbg_location_list = []
# location = {}
# location['x'] = re.findall('background-position: (.*)px (.*)px;', a)[0][1]
# location['y'] = re.findall('background-position: (.*)px (.*)px;', a)[0][1]
# fullbg_location_list.append(location)
# print(fullbg_location_list)

# print(4/2)
# import re
# a = 'sadf:sfas, "safa":123, "sasa"'
# b = re.search(r'("[a-z]*"):.*?', a)
# b = re.search(r'(sa)\1', a)
# print(b)
# a = re.sub('')
# a = [1,2,3]
# b = [4,5,6]
# d = [4,5,6, 7]
# c = zip(a, b, d)
# print(c)
# for i, j, k in c:
#     print(i, j, k)

l1=[[1,2,3],[4,5,6],[7,8,9,8]]
print(  [[j[i] for j in l1] for i in range(len(l1[1]))])





