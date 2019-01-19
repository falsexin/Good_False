#
# @Time    : 2019/1/14 17:35
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 豆瓣模拟登陆.py
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

# 导入 webdriver
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time

email = input('请输入用户名：')
pd = input('请输入密码：')
driver = webdriver.Chrome()
driver.get("https://www.douban.com/")

input_email = driver.find_elements_by_xpath('//input[@id="form_email"]')
print(len(input_email))

input_pd = driver.find_elements_by_xpath('//input[@id="form_password"]')
print(len(input_pd))
print(email, pd)
input_email[0].send_keys(email)
input_pd[0].send_keys(pd)

input_sumbit = driver.find_element_by_xpath('//input[@class="bn-submit"]')
input_sumbit.click()




