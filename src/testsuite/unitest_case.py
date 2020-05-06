# coding=utf-8
import unittest


class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('所有case执行之前的前置')

    @classmethod
    def tearDownClass(cls):
        print('所有case执行之后的后置')

    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print('这是case的后置条件')

    @unittest.skip('不执行第一条')
    def testfirst01(self):
        print("这是第一个case")

    def testfirst02(self):
        print("这是第二条case")

    def testfirst03(self):
        print("这是第三条case")


if __name__ == '__main__':
    #单独执行某条用例
    suite = unittest.TestSuite()
    suite.addTest(FirstCase01('testfirst02'))
    suite.addTest(FirstCase01('testfirst01'))
    suite.addTest(FirstCase01('testfirst03'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
