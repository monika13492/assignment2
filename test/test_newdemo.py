import pytest
from utilities.BaseClass import BaseClass
from pages.new_demo import DemoLoginPage


# @pytest.mark.usefixtures("beforeMethod")
class TestLogin(BaseClass):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
        self.demo = DemoLoginPage(self.driver)


    def test_log_in(self):
        self.demo.click_login_home()
        self.demo.send_email()
        self.demo.send_password()
        self.demo.click_remember()
        self.demo.click_login()
