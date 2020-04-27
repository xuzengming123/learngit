# -*- coding: utf-8 -*-
# __author__:29276
# 2019/9/22

class Slide:
    '''
    模拟手机滑动
    '''

    def __init__(self, driver):
        self.driver = driver

    def get_screen_size(self):
        x = self.driver.get_window_size()['width']  # 获取屏幕宽度
        y = self.driver.get_window_size()['height']  # 获取屏幕高度
        return (x, y)

    def swipeLeft(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.75)  #起点x轴
        y1 = int(l[1] * 0.5)   #起点y轴
        x2 = int(l[0] * 0.25)  #终点x轴
        self.driver.swipe(x1, y1, x2, y1)
        print('向左滑动')

    def swipeRight(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1,500)
        print('向右滑动')

    def swipeUp(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.75)
        y2 = int(l[1] * 0.25)
        self.driver.swipe(x1, y1, x1, y2,500)
        print('向上滑动')

    def swipeDown(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.25)
        y2 = int(l[1] * 0.75)
        self.driver.swipe(x1, y1, x1, y2,500)
        print('向下滑动')

class move(Slide):
    def swipeLeft(self):
        l = self.get_screen_size()
        x1 = int(l[0] * 0.75)  # 起点x轴
        y1 = int(l[1] * 0.25)  # 起点y轴 ---从上往下数的
        x2 = int(l[0] * 0.25)  # 终点x轴
        self.driver.swipe(x1, y1, x2, y1,500)
        print('向左滑动')

