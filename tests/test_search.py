import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

from pages import HomePages
from pages import search_Page
from pages.HomePages import Home_Pages
from pages.search_Page import SearchPages
from tests.test_base import Test_base


class Test_search(Test_base):



    def test_search_the_valid_product(self):
        home = Home_Pages(self.driver)
        search_pages=home.search_product_filed("hp")
        assert search_pages.valid_hp_product_link_text()

    def test_search_the_invalid_product(self):
        home = Home_Pages(self.driver)
        search_pages=home.search_product_filed("honda")
        expected_text = "There is no product that matches the search criteria."
        assert search_pages.invalid_product_text().__eq__(expected_text)

    def test_search_the_none_product(self):
        home = Home_Pages(self.driver)
        search_pages=home.search_product_filed("")
        expected_text = "There is no product that matches the search criteria."
        assert search_pages.invalid_product_text().__eq__(expected_text)
