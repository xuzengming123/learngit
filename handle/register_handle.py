#coding=utf-8
from page.register_page import RegisterPage

class RegisterHandle():
    def __init__(self,driver):
        self.register_p = RegisterPage(driver)

    def send_user_email(self,email):
        # 输入邮箱
        self.register_p.get_email_element().send_keys(email)

    def send_user_name(self,name):
        # 输入用户名
        self.register_p.get_name_element().send_keys(name)

    def send_user_like(self,*like):
        # 输入爱好
        eles = self.register_p.get_like_element()
        for ele in eles:
            likes = ele.get_attribute('textContent')
            if likes in like:
                ele.click()

    def send_user_code(self,code):
        # 输入验证码
        self.register_p.get_code_element().send_keys(code)

    def click_register_button(self):
        #点击
        self.register_p.get_button_element().click()

    def get_user_text(self,info):
        if info == 'email_error':
            text = self.register_p.get_email_error_element().get_attribute('textContent')
        elif info == 'user_error':
            text = self.register_p.get_name_error_element().get_attribute('textContent')
        elif info == 'like_error':
            text = self.register_p.get_like_error_element().get_attribute('textContent')
        else:
            text = self.register_p.get_code_error_element().get_attribute('textContent')
        return text

    def get_register_text(self):
        return self.register_p.get_button_element()

