

"""expected_conditions模块visibility_of_element_located类"""
#visibility_of_element_located判断某个locator元素是否可见，宽和高都大于0
#如果定位到就返回WebElement

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

print('开始',time.ctime())
wait = WebDriverWait(driver,10)
try:
    wait.until(ec.visibility_of_element_located((By.ID,'kw')),'失败').send_keys('bbbb')
    wait.until(ec.element_to_be_clickable((By.ID,'su'))).click()
except BaseException as e222:
    print(e222)

driver.quit()