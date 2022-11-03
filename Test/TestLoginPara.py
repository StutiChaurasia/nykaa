import pytest
from Pages.LoginPageLocators import *
from Utilities.CommonUtilities import CommonUtil
from Utilities.LoginPageUtilities import LoginPageFunctions

class TestLoginPages:
    @pytest.mark.usefixtures("initiate_driver")
    @pytest.mark.parametrize('phone_num',
                             [("811412951"), ("81141295123"), (""), ("stuti")])
    def test_login_with_invalid_details(self, initiate_driver, phone_num):
        ca = CommonUtil()
        ca.click_element(account)
        ca.click_element(sign_up_btn)
        LoginPageFunctions().perform_login(username=phone_num)

