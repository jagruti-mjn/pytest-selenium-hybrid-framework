import pytest
import self
from selenium.webdriver.common.by import By
from pages import register_page

from pages import HomePages
from pages.HomePages import Home_Pages
from pages.register_page import Register_Page
from tests.test_base import Test_base


class Test_common(Test_base):
    def test_register_valid(self):
        home = Home_Pages(self.driver)
        register_pages=home.nevigates_on_register_option()
        register_pages.open_register_page("jagu","jagu","jagu@gmail.com","12345","jagu","jagu")
        expected = "Warning: E-Mail Address is already registered!"
        assert register_pages.display_error_sms().__contains__(expected)
