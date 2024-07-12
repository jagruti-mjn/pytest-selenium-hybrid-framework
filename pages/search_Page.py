from selenium.webdriver.common.by import By

from pages.base_page import BasePages


class SearchPages(BasePages):
    def __init__(self, driver):
        super().__init__(driver)

    hp_link_text = "HP LP3065"
    invalid_product_honda_xpath = "//input[@id='button-search']/following-sibling::p"

    def valid_hp_product_link_text(self):
        return self.display("hp_link_text",self.hp_link_text)

    def invalid_product_text(self):
        return self.text_presence("invalid_product_honda_xpath",self.invalid_product_honda_xpath)
