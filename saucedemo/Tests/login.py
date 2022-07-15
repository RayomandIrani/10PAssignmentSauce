from selenium import webdriver
from saucedemo.Pages.loginPage import LoginPage
import time
import unittest


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("E:/PyCharmProject/10PearlAssignment/saucedemo/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

# Standard User

    def test_01_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login.enter_username("standard_user")
        login.enter_password("secret_sauce")
        login.click_login()

# Improper Credentials

    def test_02_login_invalid(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login.enter_username("standard_user")
        login.enter_password("abc")
        login.click_login()
        login.error_message("Epic sadface: Username and password do not match any user in this service")

# No Credentials

    def test_03_login_invalid(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login.click_login()
        login.error_message("Epic sadface: Username is required")

# Locked Out User

    def test_04_login_valid(self):
        driver = self.driver
        login = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")
        login.enter_username("locked_out_user")
        login.enter_password("secret_sauce")
        login.click_login()
        login.error_message("Epic sadface: Sorry, this user has been locked out.")

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__=='__main__':
    unittest.main()