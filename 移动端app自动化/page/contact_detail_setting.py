# 点击右上角按钮后，进入成员个人信息第二个页面
from appium.webdriver.common.mobileby import MobileBy

from 作业.移动端app自动化.page.base_page import BasePage
from 作业.移动端app自动化.page.contact_edit import ContactEdit


class ContactDetailSetting(BasePage):
    def contactds(self):
        self.find(MobileBy.XPATH, '//*[@text="编辑成员"]').click()

        return ContactEdit(self.driver)
