import time
import pytest
from config.configdata import *
from Pages.LoginPageLocators import *
from Utilities.CommonUtilities import CommonUtil
from Pages.HomePageLocators import *
from Pages.OrderLocators import *
from Utilities.SearchUtilities import seacrh_and_order_product
from Utilities.LoginPageUtilities import LoginPageFunctions

class TestLoginPages:
    @pytest.mark.usefixtures("initiate_driver")
    def test_login_with_correct_email_and_correct_password(self, initiate_driver):
        ca = CommonUtil()
        ca.click_element(account)
        ca.click_element(sign_up_btn)
        LoginPageFunctions().perform_login(username=username)
        time.sleep(20)
        ca.click_element(search_icon)
        seacrh_and_order_product().search_product()
        seacrh_and_order_product().add_wishlist()
        wishlist_success = ca.get_element_text(wishlist_verify)
        assert "My wishlist" == wishlist_success.text
