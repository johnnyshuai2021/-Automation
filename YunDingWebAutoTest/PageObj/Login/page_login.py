# -*- coding:UTF-8 -*-
'''
AUTHOR: Zhong xinqi
DATE: 2020/08/06 Thu
DESCRIPTION:登录页面元素
'''

import os, sys, allure
from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By
import Action
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login(BasePage):
    enterprise_loc = (By.CSS_SELECTOR, "[placeholder='企业号']")
    account_loc = (By.CSS_SELECTOR, "[placeholder='登录账户']")
    password_loc = (By.CSS_SELECTOR, "[placeholder='密码']")
    login_botton_loc = (By.CSS_SELECTOR, ".ant-btn.submit-btn")
    home_text_loc = (By.CSS_SELECTOR, "[to='/home']")

    @allure.step("输入企业号")
    def input_enterprise(self, enterprise):
        self.send_key(enterprise, *self.enterprise_loc, clear=True)

    @allure.step("输入账号")
    def input_account(self, account):
        self.send_key(account, *self.account_loc, clear=True)

    @allure.step("输入密码")
    def input_password(self, password):
        self.send_key(password, *self.password_loc, clear=True)

    @allure.step("点击登录按钮")    
    def click_login_botton(self):
        self.find_element(*self.login_botton_loc).click()


    # def login_full_login(self, entre1, username2, pasword3):
    #     self.input_enterprise(entre1)
    #     self.input_account(username2)
    #     self.input_password(pasword3)
    #     self.click_login_botton()
