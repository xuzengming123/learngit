#coding=utf-8
from src.funtions.print_image_code import GetCode
from src.until.read_ini import ReadIni
from selenium import webdriver
from src.funtions.find_element import FindElement

import time,random
from PIL import Image

class RegisterFunction():
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    def get_driver(self,url,i):
        '''
        获取driver并且打开URL
        :param url:
        :return: driver对象
        '''
        if i == 0:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Edge()
        else:
            driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver

    def send_user_info(self,key,data):
        '''
        输入用户信息
        :param key:
        :param data:
        :return:
        '''
        self.get_user_element(key).send_keys(data)

    def click_user_info(self,key):
        '''
        点击
        :param key:
        :param data:
        :return:
        '''
        self.get_user_element(key).click()

    def get_user_element(self,key):
        '''
        定位用户信息，获取element
        :param key:
        :return:
        '''
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_user(self):
        user_info = ''.join(random.sample('123456zxcvbn',8))
        return user_info


    def get_img(self,img_path_key,img_element_key):
        read_ini = ReadIni()
        img_path = read_ini.get_value(img_path_key)
        self.driver.save_screenshot(img_path)
        im = FindElement(self.driver)
        # img_element = self.driver.find_element_by_css_selector('#mail-form > div:nth-child(7) > div.ipt.ver_code > span > img')
        img_element = im.get_element(img_element_key)
        # print(type(img_element))
        # print(img_element)
        location = img_element.location
        size = img_element.size
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y']) + size['height'])  # 写成我们要截取的位置坐标

        i = Image.open(img_path)  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(img_path)  # 验证码截图
        return img_path

    def get_img_code(self):
        read_ini = ReadIni()
        img_path = read_ini.get_value('img_path_key')
        getcode = GetCode()
        text = getcode.OCR_lmj(img_path)
        return text


    def main(self):
        user_name_info = self.get_range_user()
        user_emial = user_name_info + '@168.com'
        user_name = user_name_info

        self.click_user_info('user_email_click')
        time.sleep(1)
        self.send_user_info('user_email',user_emial)
        time.sleep(1)
        self.send_user_info('user_name',user_name)
        time.sleep(1)
        self.click_user_info('user_like')
        time.sleep(1)

        self.get_img('img_path_key','img_element_key')
        code_text = self.get_img_code()
        self.send_user_info('code_text',code_text)

        self.click_user_info('user_regiest')
        code_error = self.get_user_element('code_error')
        if code_error == None:
            print('注册成功')
        else:

            a = int(round(time.time() * 1000))
            self.driver.save_screenshot("E:/imooc/error"+str(a)+".png")
        time.sleep(1)

if __name__ =='__main__':
    for i in range(3):
        register = RegisterFunction('https://login.sina.com.cn/signup/signup?entry=homepage',i)
        register.main()
        register.driver.quit()



