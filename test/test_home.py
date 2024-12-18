import unittest
import pytest

from pages.home import Home


@pytest.mark.usefixtures("beforeMethod")
class Survey(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):  # object creation
        self.home_object = Home(self.driver)

    def test_home(self):
        self.home_object.click_register()