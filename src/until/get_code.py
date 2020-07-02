from PIL import Image

from src.funtions.find_element import FindElement
from src.funtions.print_image_code import GetCode
from page.register_page import RegisterPage
from src.until.read_ini import ReadIni


class Getcode:
    def __init__(self,driver):
        self.driver = driver

    def get_img(self, img_path_key, img_element_key):
        read_ini = ReadIni()
        img_path = read_ini.get_value(img_path_key)
        self.driver.save_screenshot(img_path)
        im = FindElement(self.driver)
        # img_element = self.driver.find_element_by_css_selector('#mail-form > div:nth-child(7) > div.ipt.ver_code > span > img')
        img_element = im.get_element(img_element_key)
        # print(type(img_element))
        # print(img_element)
        location = img_element.location
        size = img_element.size
        rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']),
                  int(location['y']) + size['height'])  # 写成我们要截取的位置坐标

        i = Image.open(img_path)  # 打开截图
        frame4 = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(img_path)  # 验证码截图
        return img_path

    def get_img_code(self,driver,img_path_key):
        register_p = RegisterPage(driver)
        img_path = register_p.fd.get_path(img_path_key)
        a = GetCode()
        text = a.OCR_lmj(img_path)
        return text