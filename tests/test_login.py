

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from datetime import datetime
from pages import HomePages
from pages import login_page
from pages import account_page
from pages.HomePages import Home_Pages
from pages.account_page import Account_page1
from pages.login_page import login_page1
from tests.test_base import Test_base


def get_timestamp():
    time_stam = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return "jagruti" + time_stam + "@gmail.com"



class Test_login(Test_base):

    def test_invalid_email_valid_password(self):
        home = Home_Pages(self.driver)
        login_pages=home.nevigate_login_option()
        login_pages.login_to_application("get_timestamp","shree@123")
        expect_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_pages.diy_warning_sms().__contains__(expect_warning)

    def test_valid_email_invalid_password(self):
        home = Home_Pages (self.driver)
        login_pages=home.nevigate_login_option()
        login_pages.login_to_application("jagrutibmore@mail","shree@12f3")
        expect_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_pages.diy_warning_sms().__contains__(expect_warning)

    def test_no_email_no_password(self):
        home=Home_Pages(self.driver)
        login_pages=home.nevigate_login_option()
        login_pages.login_to_application("","")
        expect_warning = "Warning: No match for E-Mail Address and/or Password."
        assert login_pages.diy_warning_sms().__contains__(expect_warning)

    def test_valid_email_valid_password(self):
        home = Home_Pages(self.driver)
        login_pages=home.nevigate_login_option()
        account_pages=login_pages.login_to_application("gudu12356@gmail.com","shree@123")
        assert account_pages.valid_account_text()
