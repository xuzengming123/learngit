# coding=utf-8
from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, name, code,*like):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_code(code)
        self.register_h.send_user_like(*like)
        self.register_h.click_register_button()

    def register_succes(self):
        if self.register_h.get_register_text() is None:
            return True
        else:
            return False

    def login_email_error(self, email):
        # 执行操作
        self.register_h.send_user_email(email)
        self.register_h.click_register_button()
        if self.register_h.get_user_text('email_error') is None:
            print('输入非法数字：%s，没有出现提示'%email)
            return True
        else:
            print('输入非法数字：%s,出现错误提示'%email)
            return False

    def login_name_error(self, name):
        self.register_h.send_user_name(name)
        self.register_h.click_register_button()
        if self.register_h.get_user_text('user_error') is None:
            print('输入非法数字：%s，没有出现提示' % name)
            return True
        else:
            print('输入非法数字：%s,出现错误提示' % name)
            return False

    def login_like_error(self):
        self.register_h.click_register_button()
        if self.register_h.get_user_text('like_error') is None:
            print('爱好为空，没有出现错误提示')
            return True
        else:
            print('爱好不为空，出现错误提示')
            return False

    def login_code_error(self):
        # 执行操作
        self.register_h.click_register_button()
        if self.register_h.get_user_text('code_error') is None:
            print('验证码为空，没有出现错误提示')
            return True
        else:
            print('验证码不为空，没有错误提示')
            return False