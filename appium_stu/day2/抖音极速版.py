# -*- coding: utf-8 -*-
# __author__:29276
# 2019/9/25
import time

from appium import webdriver

desired_caps = {
    "platformName":"Android",
    "platformVersion":"9",
    "deviceName":"test",
    #'app':r'd:\apk\toutiao.apk',
    #发现appPackage\appActivity 或者 adb shell dumpsys activity recents |find " intent={"
    "appPackage":"com.kuaishou.nebula",
    "appActivity":"com.yxcorp.gifshow.HomeActivity",
    # 'unicodeKeyboard':'Ture',
    # 'resetKeyboard':'Ture',
    "noReset":True,
    "newCommandTimeout":6000,
    # 'automationName':'uiautomator2'   #不需要每个都配置
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
time.sleep(2)

from cfg import Slide
peoper = Slide(driver)
while True:
    peoper.swipeUp()
    time.sleep(10)

a = 'cmp=com.yanhui.qktx/.dv.SwitchEnvironmentActivity}'