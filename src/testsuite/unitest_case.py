#coding=utf-8
import unittest


class FirstCse01(unittest.TestCase):

    def setUp(self):
        print("这是case的前置条件")

    def tearDown(self):
        print('这是case的后置条件')

    def testfirst01(self):
        print("这是第一个case")
    def testfirst02(self):
        print("这是第二条case")

if __name__ == '__main__':
    unittest.main()