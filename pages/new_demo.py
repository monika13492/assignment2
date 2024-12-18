from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import datetime
import os
import time


class DemoLoginPage:
    def __init__(self, driver):
        self.driver = driver

    # locator:
    login_btn = "ico-login"  # class
    username = "//input[@id= 'Email']"  # id
    password = "//input[@type ='password']"  # xpath
    rememberme = "RememberMe"  # id
    login = "//input[@class = 'button-1 login-button']"  # xpath

    def click_login_home(self):
        self.driver.find_element(By.CLASS_NAME, self.login_btn).click()

    def send_email(self):
        self.driver.find_element(By.XPATH, self.username).send_keys("r01@getnada.com")

    def send_password(self):
        self.driver.find_element(By.XPATH, self.password).send_keys("123456")

    def click_remember(self):
        self.driver.find_element(By.ID, self.rememberme).click()

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login).click()
        time.sleep(5)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_name = os.path.join("C:\\Users\\monika.trivedi_infob\\Documents\\Monika\\demoproject",f"screenshot_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")
