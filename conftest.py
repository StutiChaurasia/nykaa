import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver=webdriver.Chrome(ChromeDriverManager().install())
@pytest.fixture()
def initiate_driver():

    driver.get("https://www.nykaafashion.com/")
    driver.maximize_window()
    yield driver
    driver.quit()