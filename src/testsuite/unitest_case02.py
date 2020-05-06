# coding=utf-8
import unittest


class FirstCase02(unittest.TestCase):

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
    def testfirst001(self):
        print("这是第001个case")

    def testfirst002(self):
        print("这是第002条case")

    def testfirst003(self):
        print("这是第003条case")


if __name__ == '__main__':
    #单独执行某条用例
    suite = unittest.TestSuite()
    suite.addTest(FirstCase02('testfirst002'))
    suite.addTest(FirstCase02('testfirst001'))
    suite.addTest(FirstCase02('testfirst003'))
    runner = unittest.TextTestRunner()
    runner.run(suite)
