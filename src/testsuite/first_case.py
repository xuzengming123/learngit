# coding=utf-8
import os,sys
import time

from selenium import webdriver
from business.register_business import RegisterBusiness
import unittest
import HTMLTestRunner.HTMLTestRunner



class FisrstCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://login.sina.com.cn/signup/signup?entry=homepage')
        self.driver.find_element_by_css_selector('.main_tab >a:nth-child(2)').click()
        self.login = RegisterBusiness(self.driver)
        print('===============\n这是case的前置条件')

    def tearDown(self):
        # for method_name,error in self._outcome.errors:
        #     if error:
        #         case_name = self._testMethodName
        #         file_path = os.path.join(os.path.abspath('../..') + "\\report\\" + case_name + '.png')
        #         self.driver.save_screenshot(file_path)
        time.sleep(1)
        self.driver.quit()
        print('这是case的后置条件\n===============\n')

    def test_login_email_error(self):
        email_error = self.login.login_email_error('11')
        self.assertFalse(email_error,'case执行了')
        # if email_error:
        #     print('此条case执行失败')
        # else:
        #     print('此条case执行成功')
        # 通过assert判断是否为error

    def test_login_username_error(self):
        name_error = self.login.login_name_error('22')
        self.assertFalse(name_error)
        # if name_error:
        #     print('此条case执行失败')
        # else:
        #     print('此条case执行成功')
        # 通过assert判断是否为error

    def test_login_like_error(self):
        like_error = self.login.login_like_error()
        self.assertFalse(like_error)
        # if like_error:
        #     print('此条case执行失败')
        # else:
        #     print('此条case执行成功')
        # 通过assert判断是否为error

    def test_login_code_error(self):
        code_error = self.login.login_code_error()
        self.assertFalse(code_error)
        # if code_error:
        #     print('此条case执行失败')
        # else:
        #     print('此条case执行成功')
    # 通过assert判断是否为error

    def test_login_succes(self):
        success = self.login.user_base('12125@168.com', '87877878','IT','体育','新闻','财经','娱乐')
        time.sleep(2)
        self.assertFalse(success)
        # if self.login.register_succes():
        #     print("注册成功")
        # else:
        #     print('注册失败')


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
    file_path = os.path.join(os.path.abspath('../..')+"\\report\\"+"first_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestSuite()
    suite.addTest(FisrstCase('test_login_succes'))
    # unittest.TextTestRunner().run(suite)
    runner = HTMLTestRunner.HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report',description="这个是我们第一次测试报告",verbosity=2)
    runner.run(suite)