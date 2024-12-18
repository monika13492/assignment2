from base.base import BaseClass

# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
# driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Radha")
# driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Trivedi")
# driver.find_element(By.ID, "Email").send_keys("r01@getnada.com")
# driver.find_element(By.ID, "Password").send_keys("123456")
# driver.find_element(By.ID, "ConfirmPassword").send_keys("123456")
# driver.find_element(By.NAME, "register-button").click()

class Register(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    gender = "//input[@id='gender-female']"
    firstname = "//input[@id='FirstName']"
    lastname = "//input[@id='LastName']"
    email = "Email"
    password = "Password"
    confirm_password = "ConfirmPassword"
    register_btn = "register-button"

    # method
    def click_gender(self):
        self.click_on_element(self.gender, "xpath")

    def send_first(self):
        self.send_text("Radha", self.firstname, "xpath")

    def send_last(self):
        self.send_text("Trivedi", self.lastname, "xpath")

    def send_email(self):
        self.send_text("r00@getnada.com", self.email, "id")

    def send_pass(self):
        self.send_text("123456", self.password, "id")

    def send_confirmpass(self):
        self.send_text("123456", self.confirm_password, "id")

    def click_reg(self):
        self.click_on_element(self.register_btn, "name")
