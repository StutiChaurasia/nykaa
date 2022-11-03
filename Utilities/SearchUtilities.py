import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.CommonUtilities import CommonUtil
from config.configdata import *
from conftest import driver
from Pages.OrderLocators import *
from Pages.HomePageLocators import *

class seacrh_and_order_product:
    def search_product(self):
        ca = CommonUtil()
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, search_icon)))
        search_item = driver.find_element(by=By.XPATH, value=search_icon)
        search_item.send_keys(product)
        search_item.send_keys(Keys.ENTER)
        ca.click_element(toys)
        time.sleep(10)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[1])
        ca.click_element(add_to_bag)
        ca.click_element(view_bag)
        time.sleep(5)
        driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
        time.sleep(3)

    def add_address(self):
        ca = CommonUtil()
        ca.click_element(proceed_to_buy)
        time.sleep(5)
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, postal_code)))
        add_pin = driver.find_element(by=By.XPATH, value=postal_code)
        add_pin.send_keys(pincode)
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, address_line_1)))
        add_add = driver.find_element(by=By.XPATH, value=address_line_1)
        add_add.send_keys(address)
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, name)))
        add_add = driver.find_element(by=By.XPATH, value=name)
        add_add.send_keys(full_name)
        WebDriverWait(driver, explicit_wait_time).until(
            EC.visibility_of_element_located((By.XPATH, phone_number)))
        add_add = driver.find_element(by=By.XPATH, value=phone_number)
        add_add.send_keys(num)

    def add_wishlist(self):
        ca = CommonUtil()
        ca.click_element(move_to_wishlist)
        ca.click_element(back_shopping)
        time.sleep(2)
        ca.click_element(wishlist)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[2])







