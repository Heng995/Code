from selenium import webdriver
driver = webdriver.Chrome('E:\chromedriver_win32\chromedriver.exe')

driver.get('https://www.momoshop.com.tw/goods/GoodsDetail.jsp?i_code=8334580&Area=search&mdiv=403&oid=1_1&cid=index&kw=g%20pro%20x')

driver.find_elements_by_css_selector('.buynow').click