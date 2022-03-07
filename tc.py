from lib2to3.pgen2 import driver
from selenium import webdriver
import time


browser = webdriver.Chrome("E:/chromedriver_win32/chromedriver.exe")
browser.get('https://m.momoshop.com.tw/mymomo/login.momo')
time.sleep(1)



browser.find_element_by_id('memId').send_keys('0932103648')
time.sleep(1)
browser.find_element_by_id('passwd').send_keys('esxl0110')
browser.find_element_by_css_selector('.loginBtn').click()
time.sleep(1)
browser.find_element_by_css_selector('.topSearch').click()
time.sleep(1)
browser.find_element_by_id('searchKeyword').send_keys('ps5')
browser.find_element_by_link_text('【SONY 索尼】PlayStation5 光碟版主機(CFI-1118A01)').click()
