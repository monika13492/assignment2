from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import datetime
import os
import time


class HomeAfter(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    # locator signin:
    login_btn = "ico-login"  # class
    username = "//input[@id= 'Email']"  # xpath
    password = "//input[@type ='password']"  # xpath
    rememberme = "RememberMe"  # id
    login = "//input[@class = 'button-1 login-button']"  # xpath

    # locators
    book = "(//a[contains(.,'Books')])[3]"  # xpath
    addcart = "(//input[@class = 'button-2 product-box-add-to-cart-button'])[1]"  # xpath
    cartlabel = "//span[@class ='cart-qty']"  # classname
    # cartquantity = "itemquantity2661239" #name
    updatecart = "updatecart"  # name
    countrydrpdwon = "//select[@id= 'CountryId']"  # xpath
    statedrpdwn = "//select[@id= 'StateProvinceId']"
    estiship = "estimateshipping"  # name
    checkbox = "termsofservice"  # name
    checkout = "checkout"  # id
    signout = "ico-logout"  # class

    # method
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
        screenshot_name = os.path.join("C:\\Users\\monika.trivedi_infob\\Documents\\Monika\\demoproject",
                                       f"screenshot_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")

    def click_book(self):
        self.driver.find_element(By.XPATH, self.book).click()

    def click_addcart(self):
        self.driver.find_element(By.XPATH, self.addcart).click()

    def click_cartlabel(self):
        self.driver.find_element(By.XPATH, self.cartlabel).click()

    # def send_cartqnt(self):
    #     self.send_text(2 ,self.cartquantity, "name")

    def click_updatecart(self):
        self.driver.find_element(By.NAME, self.updatecart).click()

    # def selectcountry(self):
    #     self.get_Option_by_Text_Index(41, "xpath")
    #
    # def click_state(self):
    #      self.click_on_element(self.statedrpdwn, "xpath")

    def click_estishipping(self):
        self.driver.find_element(By.NAME, self.estiship).click()

    def click_checkbox(self):
        self.driver.find_element(By.NAME, self.checkbox).click()

    def click_checkout(self):
        self.driver.find_element(By.ID, self.checkbox).click()

    def clik_signout(self):
        self.driver.find_element(By.CLASS_NAME, self.signout).click()
    #
    #     # def selectcountry(self):
    # #     self.get_Option_by_Text_Index(41, "xpath")
