import ddt
import unittest
import os,sys
import time
from selenium import webdriver
from business.register_business import RegisterBusiness
import unittest
import HTMLTestRunner.HTMLTestRunner

#邮箱，用户名，爱好，验证码，错误信息定位元素，错误显示信心

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
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

    @ddt.data(
        ['12','email_error','请输入正确的邮箱'],
        ['12@qq.com','email_error','请输入正确的邮箱'],
        ['12@qq.com','email_error','请输入正确的邮箱'])
    @ddt.unpack
    def test_register(self, email,assertCode,assertText):
        # 执行操作
        email_error = self.login.register_funtions(email,assertCode,assertText)
        return self.assertFalse(email_error,'case执行了')
if __name__ == '__main__':
    unittest.main()