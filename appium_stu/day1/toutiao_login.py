# -*- coding: utf-8 -*-
# __author__:29276
# 2019/9/17
import time
from appium import webdriver


desired_caps = {
    'platformName':'Android',
    'platformVersion':'9',
    'deviceName':'test',
    #'app':r'd:\apk\toutiao.apk',
    #发现appPackage\appActivity 或者 adb shell dumpsys activity recents |find " intent={"
    'appPackage':'io.manong.developerdaily',
    # 'appPackage':'com.yanhui.qktx',
    'appActivity':'io.toutiao.android.ui.activity.LaunchActivity',
    # 'appActivity':'.dv.SwitchEnvironmentActivity',
    # 'unicodeKeyboard':'Ture',
    # 'resetKeyboard':'Ture',
    'noReset':True,
    'newCommandTimeout':6000,
    # 'automationName':'uiautomator2'   #不需要每个都配置
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)

try:
    # eles = driver.find_elements_by_id('tv_tab_title')
    # print(len(eles))
    eles = driver.find_elements_by_class_name('android.widget.TextView')
    print(len(eles))
    for ele in eles:
        if '我的' in ele.text:
            ele.click()
            break

    #根据id找到元素，并点击，id和html元素的id不同

except Exception as e:
    print(e.args)



