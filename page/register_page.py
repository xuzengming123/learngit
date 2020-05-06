#coding=utf-8
from src.funtions.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd = FindElement(driver)

    def get_email_element(self):
        return self.fd.get_element("user_email")

    def get_name_element(self):
        return self.fd.get_element('user_name')

    def get_like_element(self):
        return self.fd.get_element('user_likes')

    def get_code_element(self):
        return self.fd.get_element('code_text')

    def get_button_element(self):
        return self.fd.get_element('user_regiest')

    def get_code_img(self):
        return self.fd.get_path('img_path_key')

    def get_img_key(self):
        return self.fd.get_element('img_element_key')

    def get_email_error_element(self):
        return self.fd.get_element('email_error')

    def get_name_error_element(self):
        return self.fd.get_element('name_error')

    def get_like_error_element(self):
        return self.fd.get_element('like_error')

    def get_code_error_element(self):
        return self.fd.get_element('code_error')

    def get_register_text(self):
        return self.fd.get_element('register_button_text')

