import time

from base.base import BaseClass

class Home_after(BaseClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    book = "(//a[contains(.,'Books')])[3]" #  xpath
    addcart = "(//input[@class = 'button-2 product-box-add-to-cart-button'])[1]" #xpath
    cartlabel = "cart-label" #classname
    # cartquantity = "itemquantity2661239" #name
    updatecart = "updatecart" #name
    countrydrpdwon = "//select[@id= 'CountryId']"  # xpath
    statedrpdwn = "//select[@id= 'StateProvinceId']"
    estiship = "estimateshipping" #name
    checkbox = "termsofservice"  #name
    checkout = "checkout" #id
    signout = "ico-logout" #class

    # method
    def click_book(self):
        self.click_on_element(self.book, "xpath")

    def click_addcart(self):
        self.click_on_element(self.addcart, "xpath")

    def click_cartlabel(self):
        self.click_on_element(self.cartlabel, "class")

    # def send_cartqnt(self):
    #     self.send_text(2 ,self.cartquantity, "name")

    def click_updatecart(self):
        self.click_on_element(self.updatecart, "name")

    # def selectcountry(self):
    #     self.get_Option_by_Text_Index(41, "xpath")
    #
    # def click_state(self):
    #      self.click_on_element(self.statedrpdwn, "xpath")

    def click_estishipping(self):
         self.click_on_element(self.estiship, "name")

    def click_checkbox(self):
         self.click_on_element(self.checkbox, "name")

    def click_checkout(self):
         self.click_on_element(self.checkout, "id")
    def clik_signout(self):
        self.click_on_element(self.signout, "class")
    #
    #     # def selectcountry(self):
    # #     self.get_Option_by_Text_Index(41, "xpath")