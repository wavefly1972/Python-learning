# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:29:09 2017

@author: 100419
"""

from selenium import webdriver
from time import sleep

url='http://www.google.com'
email="wavefly1972@gmail.com"
password="577en055"

browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)

#chrome_options=webdriver.ChromeOptions()
#prefs={"profile.default_content_setting_values.notifications"}
#chrome_options.add_experimental_option("prefs",prefs)
#browser=webdriver.Chrome(chrome_options=chrome_options)
#browser.maximize_window()
#browser.get(url)


#
browser.find_element_by_id('gb_70').click()  #按右上角的登入鈕

browser.find_element_by_id('identifierId').send_keys(email) #輸入帳號
sleep(2) #加入等待，避免誤動作

browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click() #按繼續鍵
sleep(2)

browser.find_element_by_xpath("//input[@type='password']").send_keys(password) #輸入密碼
sleep(2)

browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click() #按繼續鍵
sleep(3)
