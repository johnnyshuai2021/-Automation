# -*- coding:UTF-8 -*-
"""
AUTHOR: johnny
DATE: 2020/10/26
DESCRIPTION:删除用户
"""
import sys, pytest, allure
import time

from selenium.webdriver.common.keys import Keys

from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
from Utils.fault_tolerant import fault_tolerant
from PageObj.UserConfig.page_user import User

from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestAccountLogin:

    @pytest.mark.basic
    @fault_tolerant
    def test_account_login(self, driver_setup, log):
        """正确账号和密码登录"""

        with allure.step("初始化浏览器"):
            driver_setup.get(SERVER)
        login = Login(driver_setup)

        with allure.step("输入企业号"):
            login.input_enterprise(GLOBAL_PARAMS[0]['enterprise'])

        with allure.step("输入账号"):
            login.input_account(GLOBAL_PARAMS[0]['account'])

        with allure.step("输入密码"):
            login.input_password(GLOBAL_PARAMS[0]['password'])

        with allure.step("点击登录"):
            login.click_login_botton()

        with allure.step("断言"):
            home_name = login.find_text(GLOBAL_PARAMS[0]['home_text'])
            assert home_name

        user = User(driver_setup)
        user.click_configmng_loc()
        user.click_org_loc()
        user.click_userconfig_loc()
        user.click_seldpart_loc()
        user.select_departlist_loc("七测试企业1")
        #user.click_selpostion_loc()
        user.select_positionlist_loc("")
        user.input_namefiled_loc("jtest05")
        user.click_searchbtn_loc()
        user.is_element_exist("//td[text()='jtest05']")
        user.click_deletebtn_loc()
        user.click_confirmdelbtn_loc()
        user.is_element_exist("//*[text()='删除成功']")

if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
