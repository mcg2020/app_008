from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.driver import Driver
import time, os, allure


class Base:

    def __init__(self):
        # 声明driver
        self.driver = Driver.get_app_driver()

    def search_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位单个元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return: 返回定位对象
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*loc))

    def search_eles(self, loc, timeout=5, poll_frequency=1.0):
        """
        定位一组元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return: 返回定位对象列表
        """
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*loc))

    def click_ele(self, loc, timeout=5, poll_frequency=1.0):
        """
        点击元素
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        self.search_ele(loc, timeout, poll_frequency).click()

    def send_ele(self, loc, text, timeout=5, poll_frequency=1.0):
        """
        输入文本内容
        :param loc: 元组 (By.ID,属性值) (By.XPATH,属性值) (By.CLASS_NAME,属性值)
        :param text: 文本内容
        :param timeout: 搜索超时时间
        :param poll_frequency: 搜索间隔
        :return:
        """
        # 定位
        input_text = self.search_ele(loc, timeout, poll_frequency)
        # 清空
        input_text.clear()
        # 输入
        input_text.send_keys(text)

    def swipe_screen(self, tag=1):
        """
        滑动屏幕
        :param tag: 1:向上 2:向下 3:向左 4: 向右
        :return:
        """
        # 分辨率
        size = self.driver.get_window_size()
        # 宽
        width = size.get("width")
        # 高
        height = size.get("height")
        time.sleep(1)
        # 滑动 上下 高80 -高20 宽50   左右 宽80 -宽20 高50
        if tag == 1:
            # 向上滑动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.2, 2000)
        if tag == 2:
            # 向下滑动
            self.driver.swipe(width * 0.5, height * 0.2, width * 0.5, height * 0.8, 2000)
        if tag == 3:
            # 向左滑动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.2, height * 0.5, 2000)
        if tag == 4:
            # 向右滑动
            self.driver.swipe(width * 0.2, height * 0.5, width * 0.8, height * 0.5, 2000)

    def get_toast(self, mess):
        """
        获取taost提示消息
        :param mess: toast的xpath拼接文本
        :return:
        """
        """注意： 当前appium1.17.1版本可以直接获取toast消息，之前版本不可以 需要Uiautomator2参数"""
        toast_xpath = (By.XPATH, "//*[contains(@text,'%s')]" % mess)
        # 定位toast
        return self.search_ele(toast_xpath, timeout=3, poll_frequency=0.3).text

    def screen_image(self, name="截图"):
        """
        截图
        :param name: 报告中图片名字
        :return:
        """
        # 图片名字
        png_name = "./Image" + os.sep + "%d.png" % int(time.time())

        self.driver.get_screenshot_as_file(png_name)

        with open(png_name, "rb") as f:
            allure.attach(f.read(), name, attachment_type=allure.attachment_type.PNG)
