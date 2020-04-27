# coding=utf-8
import time

from selenium import webdriver
from business.register_business import RegisterBusiness
import unittest


class FisrstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://login.sina.com.cn/signup/signup?entry=homepage')
        self.driver.find_element_by_css_selector('.main_tab >a:nth-child(2)').click()
        self.login = RegisterBusiness(self.driver)
        print('===============\n这是case的前置条件')

    def tearDown(self):
        self.driver.quit()
        time.sleep(1)
        print('这是case的后置条件\n===============\n')

    # def test_login_email_error(self):
    #     email_error = self.login.login_email_error('11')
    #     if email_error:
    #         print('此条case执行失败')
    #     else:
    #         print('此条case执行成功')
    #     # 通过assert判断是否为error
    #
    # def test_login_username_error(self):
    #     name_error = self.login.login_name_error('22')
    #     if name_error:
    #         print('此条case执行失败')
    #     else:
    #         print('此条case执行成功')
    #     # 通过assert判断是否为error
    #
    # def test_login_like_error(self):
    #     like_error = self.login.login_like_error()
    #     if like_error:
    #         print('此条case执行失败')
    #     else:
    #         print('此条case执行成功')
    #     # 通过assert判断是否为error
    #
    # def test_login_code_error(self):
    #     code_error = self.login.login_code_error()
    #     if code_error == True:
    #         print('此条case执行失败')
    #     else:
    #         print('此条case执行成功')
    # # 通过assert判断是否为error
    #

    def test_login_succes(self):
        success = self.login.user_base('12125@168.com', '87877878', 'asdas','IT','体育','新闻','财经','娱乐')
        time.sleep(2)
        if self.login.register_succes() == True:
            print("注册成功")
        else:
            print('注册失败')


'''
def main():

    first = FisrstCase()
    first.test_login_email_error()
    # first.test_login_username_error()
    # first.test_login_like_error()
    # first.test_login_code_error()
    # first.test_login_succes()
'''
if __name__ == '__main__':
    unittest.main()
