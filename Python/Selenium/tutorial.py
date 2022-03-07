from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "E:\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://24h.pchome.com.tw/")

search = driver.find_element_by_id("keyword")
search.send_keys("PS5")
search.send_keys(Keys.RETURN)
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CLASS_NAME, "Sort"))
    
)

titles = driver.find_elements_by_class_name("prod_name")
for title in titles:
    print(title.text)
    
link = driver.find_element_by_link_text("PS5《艾爾登法環》中文一般版")
link.click()
driver.back()

time.sleep(5)
driver.quit()