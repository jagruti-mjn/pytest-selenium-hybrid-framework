from selenium.webdriver.common.by import By

from pages.account_page import Account_page1
from pages.base_page import BasePages


class login_page1(BasePages):
    def __init__(self, driver):
        super().__init__(driver)

    email_xpath = "//input[@id='input-email']"
    pass_word_xpath = "//input[@id='input-password']"
    click_on_login_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_the_valid_email(self, email_ad_text):
        self.type_into_element(email_ad_text,"email_xpath",self.email_xpath)

    def enter_the_valid_password(self, password_ad_text):
        self.type_into_element(password_ad_text,"pass_word_xpath",self.pass_word_xpath)

    def click_on_login_btn(self):
        self.clicks_element("click_on_login_xpath",self.click_on_login_xpath)
        return Account_page1(self.driver)

    def login_to_application(self,email_ad_text,password_ad_text):
        self. enter_the_valid_email(email_ad_text)
        self.enter_the_valid_password(password_ad_text)
        return self.click_on_login_btn()

    def diy_warning_sms(self):
        return self.text_presence("warning_message_xpath",self.warning_message_xpath)


