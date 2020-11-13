# 企业微信自动打卡
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestClockIn:
    def setup(self):
        des_caps = {
            'platformName': "android",
            'platformVersion': '5.1.1',
            'deviceName': '172.0.0.1:62001',
            'noReset': True,
            'skipDeviceInitialization': 'true',
            'automationName': 'uiautomator2',
            'appPackage': 'com.tencent.wework',
            'appActivity': '.launch.LaunchSplashActivity',
            'settings[waitForIdleTimeout]': 0,  # 在动态页面获取元素时需要加上，否则用例会很慢
            # 'dontStopAppOnReset':True
        }

        self.driver = webdriver.Remote("127.0.0.1:4723/wd/hub", des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_clockIn(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector()\
                                                        .scrollable(true).instance(0))\
                                                        .scrollIntoView(new UiSelector()\
                                                        .text("打卡").instance(0));').click()

        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/hiy').click()

        # idy也可定位到打卡按钮
        # self.driver.find_element(MobileBy.ID,'com.tencent.wework:id/atz').click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()

        # 显示等待
        locator = (MobileBy.XPATH, "//*[contains(@text,'打卡成功')]")
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        ele = self.driver.find_element(*locator)

        clockIn_success = str(ele.text)
        print(clockIn_success)
        assert clockIn_success in "外出打卡成功"

    # def testDemo(self):
    #     locator = (MobileBy.XPATH, "//*[contains(@text,'打卡成功')]")
    #     WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
    #     ele = self.driver.find_element(*locator)
    #
    #     clockIn_success = str(ele.text)
    #     assert clockIn_success  in "外出打卡成功"
