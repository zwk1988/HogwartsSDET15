# 编辑联系人页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from 作业.移动端app自动化.page.member_Invite_menu_page import MemberInviteMenuPage
from 作业.移动端app自动化.page.base_page import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def add_contact(self, name, gender, phonenum):
        self.driver.find_element(MobileBy.XPATH,
                                 "// *[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(MobileBy.XPATH,
                                 '// *[contains(@text,"性别")]/..//*[@text="男"]').click()

        if gender == '男':
            WebDriverWait(self.driver, 5).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="女"]'))
            self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()

        else:
            self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()

        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"手机号")]').send_keys(phonenum)
        # self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()

        from 作业.移动端app自动化.page.member_Invite_menu_page import MemberInviteMenuPage  # 局部导入
        return MemberInviteMenuPage(self.driver)
