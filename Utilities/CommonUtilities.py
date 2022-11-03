from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from selenium.webdriver.support import expected_conditions as EC


class CommonUtil:

    def get_element_text(self, element):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, element)))
        text = driver.find_element(by=By.XPATH, value=element)
        return text

    def click_element(self, element):
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element)))
        driver.find_element(by=By.XPATH, value=element).click()
