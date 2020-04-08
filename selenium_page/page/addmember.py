from selenium.webdriver.common.by import By

from selenium_page.page.basepage import BasePage


class AddMember(BasePage):
    def add_member(self):
        self.find(By.CSS_SELECTOR,'#username').send_keys("王二")
        self.find(By.CSS_SELECTOR,'#memberAdd_acctid').send_keys("cc")
        self.find(By.CSS_SELECTOR,'#memberAdd_phone').send_keys('18818530653')
        self.find(By.CSS_SELECTOR,'.js_member_editor_form :nth-child(3) .js_btn_save').click()

    def get_name(self):
        eles = self.finds(By.CSS_SELECTOR,'[data-type="member"] > :nth-child(2)')
        arg = []
        for ele in eles:
            arg.append(ele.get_attribute("title"))
        return arg