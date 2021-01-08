import configparser
import os
from time import sleep

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# config = configparser.ConfigParser()
# #print(os.path.join(os.path.expandvars('$HOMEPATH'), 'selenium.txt'))
# #config.read('C:/selenium.txt')
# p = "C:"+ os.path.join(os.environ['HOMEPATH'], 'selenium.txt')
# print(p)
# config.read(p)
# print(config.get('driver', 'chrome_driver'))

@allure.feature('Test Baidu Search')
class TestSelenium():
    # 读入配置文件
    def get_config(self):
        config = configparser.ConfigParser()
        config_path = "C:" + os.path.join(os.environ['HOMEPATH'], '../pytest_relearn/selenium.ini')
        config.read(config_path)
        return config

    def teardown(self):
        self.driver.quit()

    def setup(self):
        config = self.get_config()
        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ['using_headless']
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       options=chrome_options)
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('key_word', [('python'), ('java')])
    @allure.story('Test key word')
    def test_baidu(self, key_word):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys(key_word)
        sleep(3)
