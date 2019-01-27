import time
from selenium import webdriver
from bs4 import BeautifulSoup

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
time.sleep(3)
driver.get('https://tw.yahoo.com')

for i in range(10):  
    driver.execute_script('window.scrollTo(i, document.body.scrollHeight);')  # 重複往下捲動
    time.sleep(1)                     

driver.close()  # 關閉瀏覽器
