#
# @Time    : 2019/1/15 11:05
# @Author  : Mat
# @欣      ：Very Cool
# @File    : 万豪酒店客房信息.py
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

driver = webdriver.Chrome()
driver.get("https://www.marriott.com/")
# print(driver.page_source)

input = driver.find_element_by_xpath('//div[@class="l-display-flex"]//input').send_keys('上海世茂皇家艾美酒店')
# print(len(input))
time.sleep(2)

sub = driver.find_element_by_xpath('//*[@id="find-a-hotel-homePage-form"]/div[2]/div[4]/button').click()
for i in range(5):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)
list = driver.find_elements_by_xpath('//div[contains(@id,"property-record-map-")]')
print(len(list))
for j in range(len(list)):
    info = list[j]
    jiudian_name = info.find_element_by_xpath('.//span[@class="l-property-name"]').text.strip()
    print('酒店名字：', jiudian_name)
    address = info.find_element_by_xpath('.//div[contains(@class, "l-s-col-4 l-m-col-8 l-l-col-12 l-m-col-last l-s-col-last t-font-s t-line-height-m m-hotel-address t-color-extradarkgrey")]').text.strip()
    print('地址：', address)
    try:
        link_1 = info.find_element_by_xpath('.//div[contains(@class, "js-button-text-wrapper l-float-right")]//a[1]').get_attribute('href')
        print('url:' , link_1)
        print(len())
        driver.execute_script('window.open()')
        driver.switch_to_window(driver.window_handles[1])
        driver.get(link_1)
        time.sleep(3)
        for i in range(5):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
        temp = driver.find_elements_by_xpath('//div[contains(@class, "l-row l-margin-bottom-ers t-bg-white l-padding-room-card")]')
        print(len(temp))
        for i in temp:
            fangjian_name = i.find_element_by_xpath('.//div[contains(@class, "l-l-col-8 l-xl-col-8")]/h3').text.strip()
            if ''.join(fangjian_name).strip() != '':
                print('房间名：', fangjian_name)
            try:
                huiyuan_price = i.find_elements_by_xpath('.//div[contains(@class, "without-widget-flow t-price l-display-flex ")]')[0].text.strip()
                if ''.join(huiyuan_price).strip() != '':
                    print('会员价:', huiyuan_price)
                putong_price = i.find_elements_by_xpath('.//div[contains(@class, "without-widget-flow t-price l-display-flex ")]')[1].text.strip()
                if ''.join(putong_price).strip() != '':
                    print('普通价:',putong_price)

            except:
                pass
            print('---'*50)
        driver.close()
        driver.switch_to_window(driver.window_handles[0])
        # driver.refresh()
        time.sleep(3)

    except Exception as e:
        print('房间已满')
        print(e)
    print("#"*50)











