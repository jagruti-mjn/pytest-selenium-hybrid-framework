from selenium.webdriver.common.by import By

from pages.base_page import BasePages
from pages.login_page import login_page1
from pages.register_page import Register_Page
from pages.search_Page import SearchPages


class Home_Pages(BasePages):
    def __init__(self, driver):
        super().__init__(driver)

    search_box_filed_xpath = "//input[@class='form-control input-lg']"
    click_on_search_btn_xpath= "//button[@class='btn btn-default btn-lg']"
    click_on_drop_down_menu_xpath = "//span[@class='caret']"
    click_on_login_text = "Login"
    click_on_my_account_xpath = "//a[@title='My Account']"
    select_register_option_text = "Register"

    def test_search_the_valid_product_pages(self, product_name):
        self.type_into_element(product_name,"search_box_filed_xpath",self.search_box_filed_xpath)

    def click_on_search_btn_pages(self):
        self.clicks_element("click_on_search_btn_xpath",self.click_on_search_btn_xpath)
        return SearchPages(self.driver)

    def click_drop_down_menu(self):
        self.clicks_element("click_on_drop_down_menu_xpath",self.click_on_drop_down_menu_xpath)

    def select_login_option(self):
        self.clicks_element("click_on_login_text",self.click_on_login_text)
        return login_page1(self.driver)

    def nevigate_login_option(self):
        self.click_drop_down_menu()
        return self.select_login_option()

    def click_on_my_account_option(self):
        self.clicks_element("click_on_my_account_xpath",self.click_on_my_account_xpath)

    def click_on_register_option(self):
        self.clicks_element("select_register_option_text",self.select_register_option_text)
        return Register_Page(self.driver)
    
    def nevigates_on_register_option(self):
        self.click_on_my_account_option()
        return self.click_on_register_option()
   
    def search_product_filed(self,product_name):
        self.test_search_the_valid_product_pages(product_name)
        self.click_on_search_btn_pages()
        return SearchPages(self.driver)