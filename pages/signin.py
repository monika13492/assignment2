from base.base import BaseClass

class Sign_in(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#locator:
    login_btn = "ico-login" #class
    email = "Email" #id
    password = "//input[@type ='password']" #xpath
    rememberme = "RememberMe" #id
    login = "//input[@class = 'button-1 login-button']" #xpath

    # method
    def click_login_home(self):
        self.click_on_element(self.login_btn, "class")

    def send_email(self):
        self.send_text("r01@getnada.com", self.email, "id")

    def send_password(self):
        self.send_text("123456", self.password, "xpath")

    def click_remember(self):
        self.click_on_element(self.rememberme, "id")

    def click_login(self):
        self.click_on_element(self.login, "xpath")

