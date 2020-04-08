from selenium import webdriver
from selenium.webdriver.common.by import By


class BasePage:
    driver = ""
    base_url = ""
    def __init__(self,resc=False):

        if resc == True:
            opts = webdriver.ChromeOptions()
            opts.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opts)
        else:
            self.driver = webdriver.Chrome()

        if self.base_url != "":
            self.driver.get(self.base_url)
        self.driver.implicitly_wait(3)

    def find(self,by,location):
        return self.driver.find_element(by,location)

    def finds(self,by,location):
        return self.driver.find_elements(by,location)