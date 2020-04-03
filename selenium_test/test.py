# -*- coding:utf-8 -*-
import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class TestActionChain():
    def setup(self):
        # chrome_option = webdriver.ChromeOptions()
        # chrome_option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    def test_case(self):

        # cookies = self.driver.get_cookies()
        # with open("cookie.txt", "w") as f:
        #     json.dump(cookies,f)
        # self.driver.find_element_by_css_selector('[href="/t/topic/1296/5"]').click()
        self.driver.get("https://www.baidu.com/")

        # self.driver.find_element_by_css_selector('#kw').send_keys("测试")
        # self.driver.find_element_by_css_selector('#su').click()
        # #self.driver.execute_script("document.documentElement.scrollTop=1000")
        # time.sleep(3)
        # self.driver.find_element_by_xpath('//*[@id="page"]/a[1]/span[2]').click()

        action = ActionChains(self.driver)
        element = self.driver.find_element_by_css_selector('a[href="http://www.baidu.com/gaoji/preferences.html"][name="tj_settingicon"]')
        action.move_to_element(element).perform()  
        self.driver.find_element_by_css_selector('.pfhover').click()
        # self.driver.find_element_by_css_selector('[href="//www.baidu.com/gaoji/advanced.html"]').click()
        # with open("cookie.txt") as f:
        #     cookies = json.load(f)
        # for cookie in cookies:
        #     if "expiry" in cookie.keys():
        #         cookie.pop("expiry")
        #     self.driver.add_cookie(cookie)
        # def wait(x):
        #     return  len(self.driver.find_element_by_css_selector("https://home.testing-studio.com/latest")) >= 1
        # WebDriverWait(self.driver,10).until(wait)

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test.py"])
