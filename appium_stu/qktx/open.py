from appium import webdriver
import time
from cfg import Slide
desired_caps = {
    "platformName":"Android",
    "platformVersion":"8.0.0",
    "deviceName":"test",
    #'app':r'd:\apk\toutiao.apk',
    #发现appPackage\appActivity 或者 adb shell dumpsys activity recents |find " intent={"
    "appPackage":"com.yanhui.qktx",
    "appActivity":".dv.SwitchEnvironmentActivity",
    # 'unicodeKeyboard':'Ture',
    # 'resetKeyboard':'Ture',
    "noReset":True,
    "newCommandTimeout":6000,
    # 'automationName':'uiautomator2'   #不需要每个都配置
}

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(10)
time.sleep(2)

driver.find_element_by_id('com.yanhui.qktx:id/btn_start').click()

time.sleep(8)

peoper = Slide(driver)
while True:
    peoper.swipeUp()
    time.sleep(10)



