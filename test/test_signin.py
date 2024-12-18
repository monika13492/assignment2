import unittest
import pytest

from pages.home import Home
from pages.signin import Sign_in

@pytest.mark.usefixtures("beforeMethod")
class Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
        self.sign_in = Sign_in(self.driver)


    def test_log_in(self):
        self.sign_in.click_login_home()
        self.sign_in.send_email()
        self.sign_in.send_password()
        self.sign_in.click_remember()
        self.sign_in.click_login()


