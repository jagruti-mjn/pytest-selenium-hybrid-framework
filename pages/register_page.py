from selenium.webdriver.common.by import By

from pages.base_page import BasePages


class Register_Page(BasePages):
    def __init__(self,driver):
        super().__init__(driver)

    register_id = "input-firstname"
    last_name_id = "input-lastname"
    input_email_id = "input-email"
    input_telephone_id = "input-telephone"
    input_password_id = "input-password"
    input_confirm_id = "input-confirm"
    click_agree_name = "agree"
    continue_btn_xpath = "//input[@value='Continue']"
    error_sms_xpath = "//div[@id='account-register']/div[1]"

    def register_name(self, name_text):
        self.type_into_element(name_text,"register_id",self.register_id)

    def register_last_name(self, last_name):
        self.type_into_element(last_name,"last_name_id",self.last_name_id)

    def register_input_email(self, email):
        self.type_into_element(email,"input_email_id",self.input_email_id)

    def register_input_password(self, password):
        self.type_into_element(password,"input_password_id",self.input_password_id)

    def register_input_telephone(self, telephone):
        self.type_into_element(telephone,"input_telephone_id",self.input_telephone_id)

    def register_input_confirm_password(self, confirm_password):
        self.type_into_element(confirm_password,"input_confirm_id",self.input_confirm_id)

    def click_on_agree_btn(self):
        self.clicks_element("click_agree_name",self.click_agree_name)

    def click_on_continue(self):
        self.clicks_element("continue_btn_xpath",self.continue_btn_xpath)

    def display_error_sms(self):
        return self.text_presence("error_sms_xpath",self.error_sms_xpath)

    def open_register_page (self,name_text, last_name, email, telephone, password, confirm_password):
        self.register_name(name_text)
        self.register_last_name(last_name)
        self.register_input_email(email)
        self.register_input_telephone(telephone)
        self.register_input_password(password)
        self.register_input_confirm_password(confirm_password)
        self.click_on_agree_btn()
        self.click_on_continue()

  #  def open_click_registerpage(self):
    #    self.click_on_agree_btn()
     #   self.click_on_continue()