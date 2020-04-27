#coding:utf-8
import time

__author__ = 'xzm'
'''
selenium元素定位封装
'''
from time import sleep
from selenium import webdriver

class BasePage():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")

    def elements(self,element,elementvalues):
        '''
        封装selenium定位方式
        :param element:
        :param elementvalues:
        :return:
        '''
        if element == 'id':
            f = self.driver.find_element_by_id(elementvalues)
            return f
        elif element == 'name':
            f = self.driver.find_element_by_name(elementvalues)
            return f
        elif element == 'classname':
            f = self.driver.find_elements_by_class_name(elementvalues)
            return f
        elif element == 'css':
            f = self.driver.find_elements_by_css_selector(elementvalues)
            return f
        elif element == 'xpath':
            f = self.driver.find_element_by_xpath(elementvalues)
            return f
    def search(self):
        inputText = '特斯拉'
        inputby = 'id'
        inputElement = 'kw'
        buttonby = 'id'
        buttonElement = 'su'
        # 定位方法的调用
        self.elements(inputby,inputElement).send_keys(inputText)
        self.elements(buttonby,buttonElement).click()
        time.sleep(3)
        self.driver.quit()
#
# my = BasePage()
# my.search()




from selenium import webdriver
from time import sleep

STYLE = "background: green; border: 2px solid red;"  # 高亮的样式

def find(driver, by, expr):
    element = driver.find_element(by, expr)
    driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, STYLE)
    return element

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')

find(driver, 'id', 'kw').send_keys("博客园 韩志超")
find(driver, 'id', 'su').click()

sleep(3)
driver.quit()



'abc=bc=1'.split('=', 1)

