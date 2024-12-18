import pytest
from utilities.BaseClass import BaseClass
from pages.new_demo import DemoLoginPage
from pages.new_home_after_login import HomeAfter


# @pytest.mark.usefixtures("beforeMethod")
class TestHomeAfterLogin(BaseClass):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
     self.home = HomeAfter(self.driver)

    def test_home(self):
        self.home.click_login_home()
        self.home.send_email()
        self.home.send_password()
        self.home.click_remember()
        self.home.click_login()
        self.home.click_book()
        self.home.click_addcart()
        self.home.click_cartlabel()
        self.home.click_updatecart()
        self.home.click_estishipping()
        self.home.click_checkbox()
        self.home.click_checkout()
        self.home.clik_signout()

