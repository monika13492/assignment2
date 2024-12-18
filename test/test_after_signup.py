import time
import unittest
import pytest
from pages.homeaftsignup import Home_after
from pages.signin import Sign_in
import allure

@pytest.mark.usefixtures("beforeMethod")
class After_sign(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
        self.sign_in = Sign_in(self.driver)
        self.after_object = Home_after(self.driver)

    def test_home_after(self):
        self.sign_in.click_login_home()
        self.sign_in.send_email()
        self.sign_in.send_password()
        self.sign_in.click_remember()
        self.sign_in.click_login()
        self.after_object.click_book()
        self.after_object.click_addcart()
        self.after_object.click_cartlabel()
        # self.after_object.click_cartqnt()
        self.after_object.click_updatecart()
        # self.after_object.selectcountry()
        # self.after_object.click_state()
        self.after_object.click_estishipping()
        self.after_object.click_checkbox()
        self.after_object.click_checkout()
        self.after_object.clik_signout()
