# 存放app相关的操作，比如启动，重启，停止，进入首页等
from appium import webdriver

from 作业.移动端app自动化.page.base_page import BasePage

from 作业.移动端app自动化.page.main_page import MainPage


class App(BasePage):

    def start(self):
        if self.driver == None:
            desired_caps = {
                "platformName": "android",
                "deviceName": "CLB7N18515003769",
                "platformVersion": "10",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true",
                # "dontStopAppOnReset":"true"#不重启app进行操作
                "skipDeviceInitialization": "true",
                "skipServerInstallation": True
            }

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self.driver.implicitly_wait(5)
            return self
        else:
            self.driver.launch_app()

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self) -> MainPage:
        # 进到首页
        return MainPage(self.driver)

    # def contact_detail(self):
    #
    #     return ContactDetailBriefInfoProfile(self.driver)
