from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
PATH  = "/Users/heng/Desktop/Code/chromedriver"

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com.tw/?hl=zh_TW")
print(driver.title)
time.sleep(1)
serch = driver.find_element_by_name("q")
serch.send_keys("Youtube")
serch.send_keys(Keys.COMMAND + 'r')
time.sleep(2)



links = driver.find_element_by_link_text("老高YouTube觀看次數破10億！3年驚人收入被揭網看傻：真的厲害｜ 蘋果新聞網｜ 蘋果日報")
links.click()

time.sleep(5)
driver.quit()