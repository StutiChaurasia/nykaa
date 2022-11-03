import time
import pytest
from config.configdata import *
from Pages.LoginPageLocators import *
from Utilities.CommonUtilities import CommonUtil
from Utilities.LoginPageUtilities import LoginPageFunctions

class TestLoginPages:
    @pytest.mark.usefixtures("initiate_driver")
    def test_login_with_correct_email_and_correct_password(self, initiate_driver):
        ca = CommonUtil()
        ca.click_element(account)
        ca.click_element(sign_up_btn)
        LoginPageFunctions().perform_login(username=username)
        time.sleep(20)
        ca.click_element(account)
        login_success = ca.get_element_text(user_verify)
        assert "Hi user!" == login_success.text
