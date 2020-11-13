# 成员个人信息第一个页面
from appium.webdriver.common.mobileby import MobileBy

from 作业.移动端app自动化.page.base_page import BasePage

from 作业.移动端app自动化.page.contact_detail_setting import ContactDetailSetting


class ContactDetailBriefInfoProfile(BasePage):
    def contactdetailbip(self):
        self.find(MobileBy.XPATH, '//*[@text="个人信息"]/../../../../..'
                                  '/android.widget.LinearLayout[2]'
                                  '//*[@class="android.widget.TextView"]').click()
        return ContactDetailSetting(self.driver)
