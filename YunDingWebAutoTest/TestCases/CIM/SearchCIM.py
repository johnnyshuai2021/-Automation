# -*- coding:UTF-8 -*-
"""
AUTHOR: johnny
DATE: 2020/10/14
DESCRIPTION:查询检查项测试用例
"""
import sys, pytest, allure
import time

from selenium.webdriver.common.keys import Keys

from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
from Utils.fault_tolerant import fault_tolerant
#from PageObj.Task.page_task import Task
from PageObj.Cim.page_cim import Cim

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

        cim = Cim(driver_setup)
        cim.click_xdgl_botton()
        time.sleep(1)
        cim.click_cim_loc()
        time.sleep(1)
        cim.click_emode_loc()
        time.sleep(1)
        cim.select_optiongroup_loc("评分模式") #选择搜索模板‘扣分模式’，‘评分模式’，‘全部’
        time.sleep(1)
        cim.input_tempfiled_loc("自动化测试2338888") #输入搜索内容
        time.sleep(1)
        cim.click_searchbtn_loc()
        time.sleep(5)

  #  self.driver.execute_script('window.scrollBy(0,250)')
        #cim.click_option_loc()
       # self.driver.switch_to.active_element.send_keys(Keys.ENTER)



if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
