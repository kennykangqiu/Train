# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 20:46:19 2018

@author: 小康
"""

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://kyfw.12306.cn/otn/login/init')

username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
username.send_keys('&&&')   #填入自己的登录名
password.send_keys('&&&')   #填入自己的密码
print('点击验证码并确认')
while True:
    if browser.current_url != "https://kyfw.12306.cn/otn/index/initMy12306":
        time.sleep(1)
    else:
        break

selectyuding = browser.find_element_by_id('selectYuding')
selectyuding.click()

fromStationText = browser.find_element_by_id('fromStationText')
fromStationText.click()
fromstation = browser.find_elements_by_class_name('ac_even')[8]
fromstation.click()
toStationText = browser.find_element_by_id('toStationText')
toStationText.click()
tostation = browser.find_elements_by_class_name('ac_even')[14]
tostation.click()
datetext = browser.find_element_by_id('train_date')
datetext.click()
date = browser.find_elements_by_class_name('cell')[14]
date.click()  

order = 1
count = 0
if order != 0:
    while browser.current_url == "https://kyfw.12306.cn/otn/leftTicket/init":
        query_ticket = browser.find_element_by_id('query_ticket')
        query_ticket.click()
        count += 1
        print('循环点击查询第{}次'.format(count))
        time.sleep(1)
        try:
            reserve = browser.find_elements_by_class_name('no-br')[order - 1]
            reserve.click()
        except Exception as e:
            print(e)
            print('还没开始预订{}'.format(count))
            continue

print('开始预订')
time.sleep(2)        
passenger = browser.find_element_by_id('normalPassenger_0')  
passenger.click()
confirm = browser.find_element_by_id('dialog_xsertcj_cancel') 
confirm.click()

submitorder = browser.find_element_by_id('submitOrder_id')
submitorder.click()
print('核对车票信息')

  









