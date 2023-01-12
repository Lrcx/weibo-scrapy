import random

import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

'''
cmd中以管理员身份运行
chrome.exe --remote-debugging-port=9527 --user-data-dir="C:\Program Files\Google\Chrome\Application"

'''
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome("D:\\chromedriver.exe",options=options)

for i in range(2,3):
    driver.get("https://www.kuaidaili.com/free/inha/{}/".format(i))

    elements = driver.find_elements(By.XPATH, '//*[@id="list"]/table/tbody/tr')

    for element in elements:

        ip = element.find_elements(By.XPATH,"./td")[0].text
        port = element.find_elements(By.XPATH,"./td")[1].text
        proxy = {'http': ip+':'+port}

        try:
            resp = requests.get(url="https://www.baidu.com", proxies=proxy)
        except:
            print("ip:"+ip+":"+port+" 请求超时")
        else:
            print(proxy)

