from selenium_page.page.index import IndxePage
import pytest


class Test_Page:
    def setup(self):
        self.index_p = IndxePage(resc=True)

    def test_addmember(self):
        add_member = self.index_p.goto_addmember()
        add_member.add_member()
        assert "王二" in add_member.get_name()


