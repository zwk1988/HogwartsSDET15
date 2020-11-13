# 通讯录页面封装
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from 作业.移动端app自动化.page.base_page import BasePage
from 作业.移动端app自动化.page.contact_detail_page import ContactDetailBriefInfoProfile
from 作业.移动端app自动化.page.member_Invite_menu_page import MemberInviteMenuPage


class AddressListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    def click_addmember(self):
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().\
        #                                                         scrollable(true).instance(0)).\
        #                                                         scrollIntoView(new UiSelector().\
        #                                                         text("添加成员").instance(0));').click()
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def search_del_contact(self):
        name = "hogwarts001"
        search_locator = (MobileBy.XPATH, f'//*[@text={name}]')
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(search_locator))
        return result

    def click_contact(self):
        # 点击某个联系人
        name = "hogwarts001"
        self.find_by_scroll(name).click()
        return ContactDetailBriefInfoProfile(self.driver)
