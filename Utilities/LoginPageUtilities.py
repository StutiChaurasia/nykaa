from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.configdata import *
from conftest import driver
from Pages.LoginPageLocators import *

class LoginPageFunctions:

    def perform_login(self, username):
        self.fill_username(username)
        driver.find_element(by=By.XPATH, value=submit_btn).click()

    def fill_username(self, username):
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, phone_number_field)))
        driver.find_element(by=By.XPATH, value=phone_number_field).send_keys(username)

