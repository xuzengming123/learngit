#coding=utf-8
from page.register_page import RegisterPage
from src.until.get_code import Getcode

class RegisterHandle():
    def __init__(self,driver):
        self.driver = driver
        self.register_p = RegisterPage(self.driver)

    def send_user_email(self,email):
        # 输入邮箱
        self.register_p.get_email_element().send_keys(email)

    def send_user_name(self,name):
        # 输入用户名
        self.register_p.get_name_element().send_keys(name)

    def send_user_like(self,*like):
        # 输入爱好7
        eles = self.register_p.get_like_element()
        for ele in eles:
            likes = ele.get_attribute('textContent')
            if likes in like:
                ele.click()

    def send_user_code(self):
        # 输入验证码
        print('1234')
        #定位验证码图片元素，截图保存到盘
        gg = Getcode(self.driver)
        gg.get_img('img_path_key','img_element_key')
        #读取盘中验证码，输入
        code_text = gg.get_img_code(self.driver,'img_path_key')
        self.register_p.get_code_element().send_keys(code_text)

    def click_register_button(self):
        #点击
        self.register_p.get_button_element().click()

    def get_user_text(self,info,user_info):
        try:
            if info == 'email_error':
                text = self.register_p.get_email_error_element().get_attribute('textContent')
            elif info == 'user_error':
                text = self.register_p.get_name_error_element().get_attribute('textContent')
            elif info == 'like_error':
                text = self.register_p.get_like_error_element().get_attribute('textContent')
            else:
                text = self.register_p.get_code_error_element().get_attribute('textContent')
        except:
            text = None
        return text

    def get_register_text(self):
        return self.register_p.get_button_element()

