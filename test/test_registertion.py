import unittest
import pytest
from pages.registration import Register
from pages.home import Home


@pytest.mark.usefixtures("beforeMethod")
class Survey(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
        self.home_object = Home(self.driver)
        self.reg_obj = Register(self.driver)

    def test_register(self):
        self.home_object.click_register()
        self.reg_obj.click_gender()
        self.reg_obj.send_first()
        self.reg_obj.send_last()
        self.reg_obj.send_email()
        self.reg_obj.send_pass()
        self.reg_obj.send_confirmpass()
        self.reg_obj.click_reg()
