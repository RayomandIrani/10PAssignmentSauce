from saucedemo.Locators.locators import Locators
from selenium.webdriver.common.by import By
class LoginPage():

    def __init__(self, driver):
        self.driver=driver

        self.username_textbox_id = Locators.username_textbox_id
        self.password_textbox_id = Locators.password_textbox_id
        self.login_button_id = Locators.login_button_id
        self.error_message_xpath = Locators.error_message_xpath

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID,  self.login_button_id).click()

    def error_message(self, msg):
        text = self.driver.find_element(By.XPATH, self.error_message_xpath).text
        assert text == msg

