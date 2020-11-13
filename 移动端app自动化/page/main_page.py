# 消息页（首页）封装
from appium.webdriver.common.mobileby import MobileBy

from 作业.移动端app自动化.page.addresslist_Page import AddressListPage
from 作业.移动端app自动化.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def goto_message(self):
        """
        进入消息页
        :return:
        """
        pass

    def goto_address(self):
        # 进入到通讯录页
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return AddressListPage(self.driver)
