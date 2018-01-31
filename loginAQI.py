# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 15:29:09 2017

@author: 100419
"""

from selenium import webdriver
from time import sleep

url='http://opendata.epa.gov.tw'
#email="wavefly1972@gmail.com"
#password="577en055"
Keyin="AQI"
browser=webdriver.Chrome()
browser.maximize_window()
browser.get(url)

sleep(3)
#chrome_options=webdriver.ChromeOptions()
#prefs={"profile.default_content_setting_values.notifications"}
#chrome_options.add_experimental_option("prefs",prefs)
#browser=webdriver.Chrome(chrome_options=chrome_options)
#browser.maximize_window()
#browser.get(url)


#
#browser.find_element_by_id('gb_70').click()  #按右上角的登入鈕

browser.find_element_by_id('Keyword').send_keys(Keyin) #輸入帳號
sleep(2) #加入等待，避免誤動作

browser.find_element_by_xpath("//a[@href='#']").click()
sleep(2)

browser.find_element_by_link_text("空氣品質指標(AQI)").click()
#browser.find_element_by_xpath("//onclink[@class='RveJvd snByac']").click() #按繼續鍵
sleep(3)

browser.find_element_by_link_text("JSON").click()
#browser.find_element_by_xpath("//input[@type='password']").send_keys(password) #輸入密碼
sleep(3)

#browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click() #按繼續鍵
#sleep(3)
