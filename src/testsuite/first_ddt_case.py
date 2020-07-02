import ddt
import unittest
import os,sys
import time
from selenium import webdriver
from business.register_business import RegisterBusiness
from src.until.excel_until import ExcelUntil
import unittest
import HTMLTestRunner.HTMLTestRunner
#邮箱，用户名，爱好，验证码，错误信息定位元素，错误显示信息

ex = ExcelUntil()
#读取data数据
data = ex.get_data()

@ddt.ddt
class FirstDdtCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://login.sina.com.cn/signup/signup?entry=homepage')
        self.driver.find_element_by_css_selector('.main_tab >a:nth-child(2)').click()
        self.login = RegisterBusiness(self.driver)
        print('===============\n这是case的前置条件')

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        print('这是case的后置条件\n===============\n')
    '''
    @ddt.data(
        ['12','125','email_error','请输入正确的邮箱','IT'],
        ['@qq.com','125','email_error','请输入正确的邮箱','娱乐'],
        ['dashab332@qq.com','125','email_error','请输入正确的邮箱','体育'])
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register(self, data):
        email, name, assertCode, assertText, *like = data
        # 执行操作
        email_error = self.login.register_funtions(email,name,assertCode,assertText,*like)
        return self.assertFalse(email_error,'case执行了')

if __name__ == '__main__':
    file_path = os.path.join(os.path.abspath('../..')+"\\report\\"+"first_ddt_case.html")
    f = open(file_path,'wb')
    suite = unittest.TestLoader().loadTestsFromTestCase(FirstDdtCase)
    runner = HTMLTestRunner.HTMLTestRunner.HTMLTestRunner(stream=f,title='This is first report1',description="这个是我们第一次测试报告1",verbosity=2)
    runner.run(suite)