# 基类模块，主要用于初始化driver，定义find等 常用的基本方法
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 封装find方法
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    # 封装滚动查找
    def find_by_scroll(self, text):
        return self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector()\
                                                                .scrollable(true).instance(0))\
                                                                .scrollIntoView(new UiSelector()\
                                                                .text("{text}").instance(0));')
