#coding=utf-8
from src.until.read_ini import ReadIni





class FindElement():
    def __init__(self,driver):
        self.driver = driver

    def get_element(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by = data.split('=>')[0]
        value = data.split('=>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'css':
                return self.driver.find_element_by_css_selector(value)

            elif by == 'ids':
                return self.driver.find_elements_by_id(value)
            elif by == 'names':
                return self.driver.find_elements_by_name(value)
            elif by == 'xpaths':
                return self.driver.find_elements_by_xpath(value)
            elif by == 'classNames':
                return self.driver.find_elements_by_class_name(value)
            elif by == 'names':
                return self.driver.find_elements_by_name(value)
            elif by == 'csses':
                return self.driver.find_elements_by_css_selector(value)

        except Exception as e:
            print(e)
        return None

    def get_path(self,key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        return data
