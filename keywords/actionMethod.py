#codeing=uft-8
from selenium import webdriver
from src.funtions.find_element import FindElement
class ActionMethod:
    def __init__(self):
        pass
    def open_browser(self,browser):
        '''
        打开浏览器
        :param browser:浏览器
        :return:
        '''
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    def get_url(self,url):
        '''
        输入地址
        :url:
        :return:
        '''
        self.driver.get(url)

    def get_element(self,key):
        '''
        定位元素
        :key:
        :return:
        '''
        find_element = FindElement(self.driver)
        element = find_element.get_element(key)
        return element

    def element_send_keys(self,key,value):
        '''
        输入元素
        :return:
        '''
        element = self.get_element(key)
        element.send_keys(value)

    def click_element(self,key):
        '''
        点击元素
        :return:
        '''
        self.get_element(key).click()

    def sleep_time(self,time):
        time.sleep(time)

    def close_browser(self):
        self.driver.close()