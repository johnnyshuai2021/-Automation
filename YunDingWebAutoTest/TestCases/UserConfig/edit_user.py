# -*- coding:UTF-8 -*-
"""
AUTHOR: johnny
DATE: 2020/10/26
DESCRIPTION:编辑用户
"""
import sys, pytest, allure
import time

from selenium.webdriver.common.keys import Keys

from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
from Utils.fault_tolerant import fault_tolerant
from PageObj.UserConfig.page_user import User
from selenium.webdriver import ActionChains

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
        #找到要编辑的用户
        user = User(driver_setup)
        user.click_configmng_loc()
        user.click_org_loc()
        user.click_userconfig_loc()
        user.click_seldpart_loc()
        user.select_departlist_loc("七测试企业1")
        #user.click_selpostion_loc()
        user.select_positionlist_loc("")
        user.input_namefiled_loc("jtest06")
        user.click_searchbtn_loc()
        user.is_element_exist("//td[text()='jtest06']")

        #编辑找到的用户
        user.click_detailbtn_loc()
        user.click_edituserbtn_loc()
        user.input_psw_loc("123456")
        user.input_name_loc("jtest05")
        user.input_phone_loc("18521523626")
        user.input_email_loc("jtest22@163.com")
        user.click_gender_loc("1")
        user.click_calendar_loc()
        user.input_birthday_loc("2012/10/12")

        user.click_label_loc()
        user.input_note_loc("edit user auomation testing")

        # 鼠标悬停到下拉箭头直到小X出现并点击
        hover_element = user.find_element(By.XPATH, "//i[@class='anticon anticon-down ant-cascader-picker-arrow']")
        ActionChains(driver_setup).move_to_element(hover_element).perform()

        user.click_closecircle_loc()
        #点击下拉箭头
        user.click_arrow_loc()
        user.select_depart_loc("七测试企业1")
        # 二级部门菜单
        # user.select_depart1_loc("研发部")
        user.select_position_loc()
        #删除关联门店
        if user.is_element_exist("//*[@class='anticon anticon-close-circle']"):
            user.find_elements(By.XPATH,"//*[@class='anticon anticon-close-circle']")[0].click()
        else:
            return
        #保存编辑
        user.click_savebtn_loc()
        user.find_element(By.XPATH,"//span[text()='保存更改']/..").click()

if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
