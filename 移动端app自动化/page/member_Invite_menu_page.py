# 邀请页面
from appium.webdriver.common.mobileby import MobileBy

# from 作业.移动端app自动化.page.contactadd_page import ContactAddPage
from 作业.移动端app自动化.page.base_page import BasePage


class MemberInviteMenuPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def add_member_menual(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        from 作业.移动端app自动化.page.contactadd_page import ContactAddPage  # 局部导入
        return ContactAddPage(self.driver)

    def get_toast(self):
        result = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"成功")]').text
        return result
