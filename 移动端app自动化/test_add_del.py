# 企业微信添加/删除 联系人
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAdd():
    def setup(self):
        desired_caps = {
            "platformName": "android",
            # "deviceName": "127.0.0.1:62001",
            "deviceName": "CLB7N18515003769",
            # "platformVersion": "5.1.1",
            "platformVersion": "10",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": True,
            # "dontStopAppOnReset":"true",#不重启app进行操作
            "skipDeviceInitialization": "true",
            "skipServerInstallation": True,
            "unicodeKeyBoard": "true",
            "resetKeyBoard": "true"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_AddContact(self):

        name = "hogwarts001"
        gender = '男'
        phonenum = '18903307481'
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().\
                                                        scrollable(true).instance(0)).\
                                                        scrollIntoView(new UiSelector().\
                                                        text("添加成员").instance(0));').click()
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'添加成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
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
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()

        result = self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"成功")]').text
        assert "添加成功" == result

    def test_DelContact(self):
        name = "hogwarts001"
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator(f'new UiScrollable(new UiSelector().\
                                                        scrollable(true).instance(0)).\
                                                        scrollIntoView(new UiSelector().\
                                                        text("{name}").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="个人信息"]/../../../../..'
                                                 '/android.widget.LinearLayout[2]'
                                                 '//*[@class="android.widget.TextView"]').click()

        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()

        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(MobileBy.XPATH, '//*[@text="取消"]'))
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()

        search_locator = (MobileBy.XPATH, f'//*[@text={name}]')
        result = WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element_located(search_locator))

        assert result is True
