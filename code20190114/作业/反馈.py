#
# @Time    : 2019/1/17 18:53
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 反馈.py
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
from selenium import webdriver
# 要想调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys
import time
# WebDriverWait 库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait


def run(pwd, phone):
    driver = webdriver.Chrome()
    driver.get("https://www.wenjuan.in/s/viyYJ3O/")
    driver.find_element_by_id('password').send_keys(pwd)
    driver.find_element_by_id('submit_btn').click()
    time.sleep(2)
    print(driver.current_url)
    driver.get("https://www.wenjuan.in/s/viyYJ3O/")
    driver.find_element_by_id('lmPhoneNum').send_keys(phone)
    time.sleep(2)
    driver.find_element_by_id('lm_next_button').click()
    driver.implicitly_wait(10)  # seconds
    list_wenti = driver.find_elements_by_xpath('//div[contains(@class, "wjques maxtop question jqtransformdone")]')
    print(len(list_wenti))
    # list_wenti.pop()
    a = driver.find_elements_by_class_name('jqTransformRadioWrapper')
    b = driver.find_elements_by_class_name('jqTransformCheckboxWrapper')
    # c = driver.find_elements_by_class_name('jqTransformCheckboxWrapper')
    for info in range(len(list_wenti)):
        if info in range(21):
            a = list_wenti[info].find_elements_by_xpath('.//span[contains(@class, "jqTransformRadioWrapper")]/a')
            # print(len(a))
            a[0].click()
            if info == 20:
                a[1].click()

        if info in range(21, 22):
            a = list_wenti[info].find_elements_by_xpath('.//span[contains(@class, "jqTransformCheckboxWrapper")]/a')
            a[0].click()
            a[1].click()
            a[2].click()
            a[3].click()
            a[4].click()
            a[5].click()
        if info in range(22, 29):
            a = list_wenti[info].find_elements_by_xpath('.//span[contains(@class, "jqTransformRadioWrapper")]/a')
            # print(len(a))
            a[0].click()
            if info == 25:
                a[2].click()

        if info in range(29, 30):
            a = list_wenti[info].find_element_by_xpath('.//textarea').send_keys('very good')
            # print(len(a))
            # a[0].click()
    driver.find_element_by_id('next_button').click()

    # driver.implicitly_wait(10)  # seconds
    time.sleep(5)
    driver.save_screenshot("./"+str(time.time())+"_反馈.png")

if __name__ == '__main__':
    pwd = input('请输入密码:')
    phone = input('请输入手机号:')
    # pwd = '0117'
    # phone = '17630728035'
    run(pwd, phone)





