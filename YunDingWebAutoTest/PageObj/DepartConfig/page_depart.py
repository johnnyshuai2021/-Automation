# -*- coding:UTF-8 -*-
'''
AUTHOR: johnny
DATE: 2020/10/22
DESCRIPTION:添加部门
'''

from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Depart(BasePage):

    # startime_loc = (By.CSS_SELECTOR,"[placeholder='开始日期']")
    configmng_loc = (By.XPATH, "//*[text()='配置管理']")
    org_loc = (By.XPATH, "//*[text()='组织架构']")
    departconfig_loc = (By.XPATH, "//*[@to='/users/department']")  # 部门配置
    createbtn_loc = (By.XPATH, "//span[text()='新建部门']/..")  # 新建按钮
    departname_loc = (By.XPATH, "//input[@placeholder='请输入部门名称']")
    departcode_loc = (By.XPATH, "//input[@placeholder='请输入部门编号']")
    #parentdepart_loc = (By.XPATH,"//*[@class='ant-select-tree-title']")


    def click_configmng_loc(self):
        self.find_element(*self.configmng_loc).click()

    def click_org_loc(self):
        self.find_element(*self.org_loc).click()

    def click_departconfig_loc(self):
        self.find_element(*self.departconfig_loc).click()

    def click_createbtn_loc(self):
        self.find_element(*self.createbtn_loc).click()

    # def select_parentdepart_loc(self):
    #     self.find_element(By.XPATH, "//*[@class='ant-form-item-control has-success']").click()
    #     elements = self.find_elements(*self.parentdepart_loc)
    #     for element in elements:
    #         print(element.get_attribute('textContent'))

        #     if i == depart_name:
        #         #     list.click()
        #         #     break
        #         # else:
        #         #     return






