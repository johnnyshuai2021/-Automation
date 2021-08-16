# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/08/06 Thu
DESCRIPTION:登录测试用例
"""

import sys, pytest, allure
import time
from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
from Utils.fault_tolerant import fault_tolerant
#from PageObj.Task.page_task import Task


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

        # Login.login_full_login(self,yuding, johhny, password)
        task = Task(driver_setup)
        task.click_xdgl_botton()
        time.sleep(3)
        task.click_rwlb_loc()
        time.sleep(3)
        #task.click_calender_loc()
        #time.sleep(3)
        task.click_storeselect_loc()



if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
