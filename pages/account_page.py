from selenium.webdriver.common.by import By

from pages.base_page import BasePages


class Account_page1(BasePages):
    def __init__(self, driver):
        super().__init__(driver)

    account_page_text = "Edit your account information"

    def valid_account_text(self):
        return self.display("account_page_text",self.account_page_text)
