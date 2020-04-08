from selenium.webdriver.common.by import By
from selenium_page.page.addmember import AddMember
from selenium_page.page.basepage import BasePage


class IndxePage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_addmember(self):
        self.find(By.CSS_SELECTOR,'.index_service_cnt_itemWrap').click()
        return AddMember(resc = True)