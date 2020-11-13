# 进入最终删除联系人页面
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

# from 作业.移动端app自动化.page.addresslist_Page import AddressListPage

from 作业.移动端app自动化.page.base_page import BasePage


class ContactEdit(BasePage):
    # 点击删除按钮
    def contact_del(self):
        self.find_by_scroll("删除成员").click()
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="取消"]'))
        self.find(MobileBy.XPATH, '//*[@text="确定"]').click()

        from 作业.移动端app自动化.page.addresslist_Page import AddressListPage
        return AddressListPage(self.driver)
