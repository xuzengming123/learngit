# -*- coding: utf-8 -*-
# __author__:29276
# 2019/9/20
from appium import webdriver


desired_caps = {
    "platformName":"Android",
    "platformVersion":"9",
    "deviceName":"test",
    #'app':r'd:\apk\toutiao.apk',
    #发现appPackage\appActivity 或者 adb shell dumpsys activity recents |find " intent={"
    "appPackage":"com.ibox.calculators",
    "appActivity":".SplashActivity",
    # 'unicodeKeyboard':'Ture',
    # 'resetKeyboard':'Ture',
    "noReset":True,
    "newCommandTimeout":6000,
    # 'automationName':'uiautomator2'   #不需要每个都配置
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)


print(driver.get_window_size())
from cfg import Slide
peoper = Slide(driver)
peoper.swipeLeft()

def opera(di):
# night = driver.find_element_by_id('digit9')
    driver.find_element_by_xpath(f'//*[@resource-id="com.ibox.calculators:id/{id}"]')
# mul = driver.find_element_by_id('mul')
# two = driver.find_element_by_id('digit2')
# plus = driver.find_element_by_id('plus')
# third = driver.find_element_by_id('digit3')
# add_item = driver.find_element_by_id('equal')


night.click()
mul.click()
two.click()
plus.click()
third.click()
add_item.click()

# 先查找父节点，
# 再根据父节点元素 调用 find element 就是在父节点的范围内 查找
did = driver.find_element_by_id('cv')
son = did.find_elements_by_class_name('android.widget.TextView')
sontext = son[1].text
print(sontext)


res = driver.find_element_by_xpath('//*[@resource-id="com.ibox.calculators:id/cv"]/android.widget.TextView[2]').text

if res == '21':
    print('pass')
else:
    print('fail')

driver.quit()