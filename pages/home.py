# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get("https://demowebshop.tricentis.com/")
# time.sleep(2)
# time.sleep(2)
# driver.find_element(By.CLASS_NAME, "ico-register").click()

from base.base import BaseClass

class Home(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    btn_register = "ico-register"

    # method
    def click_register(self):
        self.click_on_element(self.btn_register,"class")