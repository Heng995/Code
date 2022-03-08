from lib2to3.pgen2 import driver
from os import R_OK
from time import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/heng/Desktop/Code/chromedriver')
driver.get("https://m.momoshop.com.tw/goods.momo?i_code=9249262&mdiv=searchEngine&oid=1_20&kw=ps5")


buynow = driver.find_element_by_css_selector('.buyNowBtn')
buynow.click()
time.sleep(1)
buyclick = driver.find_element_by_css_selector('.enter').click()

for pw in range(10):
    phone = driver.find_element_by_id("memId")
    phone.send_keys("0932103648")
    time.sleep(0.5)
    pws = driver.find_element_by_id("passwd")
    pws.send_keys("esxl0110")
    driver.refresh()
time.sleep(10)