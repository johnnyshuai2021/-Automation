# -*- coding:UTF-8 -*-
"""
AUTHOR: johnny
DATE: 2020/10/26
DESCRIPTION:创建部门
"""
import sys, pytest, allure
import time

from selenium.webdriver.common.keys import Keys

from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
from Utils.fault_tolerant import fault_tolerant
from PageObj.DepartConfig.page_depart import Depart

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

        depart = Depart(driver_setup)
        depart.click_configmng_loc()
        depart.click_org_loc()
        depart.click_departconfig_loc()
        depart.click_createbtn_loc()
        depart.find_element(By.XPATH, "//*[@class='ant-select ant-select-enabled ant-select-allow-clear']").click()

        elements = depart.find_elements(By.XPATH,"//*[@class='ant-select-tree-title']")
        for element in elements:
            print(element.get_attribute('textContent'))
            text = element.get_attribute('textContent')
            if text == '研发部':
                break










if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])




