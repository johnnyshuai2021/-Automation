# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/08/06 Thu
DESCRIPTION:登录测试用例
"""


import os, sys, pytest, allure

from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
from Utils.fault_tolerant import fault_tolerant


class TestAccountLogin:

    @pytest.mark.login
    @fault_tolerant
    def test_account_login(self, driver_setup, log):
        """正确账号和密码登录"""
        
        with allure.step("初始化浏览器"):
            driver_setup.get(SERVER)
        login = Login(driver_setup)

        with allure.step("输入账号密码登录"):
            login.input_enterprise(GLOBAL_PARAMS[0]['enterprise'])
            login.input_account(GLOBAL_PARAMS[0]['account'])
            login.input_password(GLOBAL_PARAMS[0]['password'])
            login.click_login_botton()

        with allure.step("断言"):
            home_name = login.find_text(GLOBAL_PARAMS[0]['home_text'])
            assert home_name


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
