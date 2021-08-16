# -*- coding:UTF-8 -*-
'''
AUTHOR: johnny
DATE: 2020/10/14
DESCRIPTION:评分项管理元素
'''

from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Cim(BasePage):

    startime_loc = (By.CSS_SELECTOR,"[placeholder='开始日期']")
    endtime_loc = (By.CSS_SELECTOR,"[placeholder='结束日期']")
    calender_loc = (By.CSS_SELECTOR,"i.iconfont")
    storeselect_loc = (By.CSS_SELECTOR,"span.ant-select-search__field__mirror")
    emode_loc = (By.CSS_SELECTOR,".ant-select.ant-select-enabled") #评分模式框
    cim_loc = (By.XPATH,"//a[@to='/templates']")  #评分项管理标签

    option_loc=(By.XPATH,"//ul[@role='listbox']//li[text()='评分模式']")  #评分模式下拉项选择
    #optiongroup_loc=(By.XPATH,"//li[@role='option']")
    xdgl_loc=(By.XPATH,"//li[@role='menuitem']//span[text()='巡店管理']")  #巡店管理标签
    rwlb_loc=(By.XPATH,"//a[@to='/patrol/task/list']")   #任务列表标签
    searchbtn_loc =(By.CSS_SELECTOR,".filter-bar>button[class='ant-btn']") #查询按钮

    def click_xdgl_botton(self):
        self.find_element(*self.xdgl_loc).click()

    def click_rwlb_loc(self):
        self.find_element(*self.rwlb_loc).click()

    def click_calender_loc(self):
        self.find_element(*self.calender_loc).click()

    def click_storeselect_loc(self):
        self.find_element(*self.storeselect_loc).click()

    def click_cim_loc(self):
        self.find_element(*self.cim_loc).click()

    def click_emode_loc(self):
        self.find_element(*self.emode_loc).click()

    def click_option_loc(self):
        self.find_element(*self.option_loc).click()

    def select_optiongroup_loc(self, option_name):
        print("//ul[@role='listbox']//li[text()='"+ option_name+"']")
        self.find_element(By.XPATH, "//ul[@role='listbox']//li[text()='"+ option_name+"']").click()

    def input_tempfiled_loc(self, temp_name):
        print(temp_name)
        self.find_element(By.XPATH, "//input[@placeholder='模板名称']").send_keys(temp_name)

    def click_searchbtn_loc(self):
        self.find_element(*self.searchbtn_loc).click()


#
# if __name__ == "__main__":
#     click_calender_loc()
#     print('test"')

