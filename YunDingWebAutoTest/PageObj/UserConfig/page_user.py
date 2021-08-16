# -*- coding:UTF-8 -*-
'''
AUTHOR: johnny
DATE: 2020/10/22
DESCRIPTION:添加员工
'''

from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class User(BasePage):

    # startime_loc = (By.CSS_SELECTOR,"[placeholder='开始日期']")
    # endtime_loc = (By.CSS_SELECTOR,"[placeholder='结束日期']")
    # calender_loc = (By.CSS_SELECTOR,"i.iconfont")
    # storeselect_loc = (By.CSS_SELECTOR,"span.ant-select-search__field__mirror")
    # emode_loc = (By.CSS_SELECTOR,".ant-select.ant-select-enabled") #评分模式框
    # cim_loc = (By.XPATH,"//a[@to='/templates']")  #评分项管理标签
    #
    # option_loc=(By.XPATH,"//ul[@role='listbox']//li[text()='评分模式']")  #评分模式下拉项选择
    # #optiongroup_loc=(By.XPATH,"//li[@role='option']")
    # xdgl_loc=(By.XPATH,"//li[@role='menuitem']//span[text()='巡店管理']")  #巡店管理标签
    # rwlb_loc=(By.XPATH,"//a[@to='/patrol/task/list']")   #任务列表标签

    configmng_loc =(By.XPATH,"//*[text()='配置管理']")
    org_loc = (By.XPATH,"//*[text()='组织架构']")
    userconfig_loc = (By.XPATH,"//a[@to='/users/employee']")  #员工配置
    searchbtn_loc =(By.XPATH,"//*[@class='search-top flex']//button[1]") #搜索按钮
    createbtn_loc = (By.XPATH,"//*[@class='flex-item--none']//button[1]") #新建按钮
    seldpart_loc = (By.XPATH,"//*[@style='outline: none;']//i[@aria-label]")#选择部门下拉按钮
    #departlist_loc = (By.XPATH,"//span[@class='ant-select-tree-title' and text()='测试1']")
    selpostion_loc = (By.XPATH,"//*[@style='user-select: none;']//i[@aria-label]") #选择岗位下拉按钮
    namefiled_loc = (By.XPATH,"//input[@placeholder='请输入姓名/账号']")
    deletebtn_loc = (By.XPATH,"//a[text()='删除']")
    #确定删除按钮
    confirmdelbtn_loc = (By.XPATH,"//*[@class='ant-btn ant-btn-danger']")
    #用户详情按钮
    detailbtn_loc = (By.XPATH, "//a[text()='详情']")
    #编辑用户按钮
    edituserbtn_loc = (By.XPATH,"//span[text()='编 辑']/..")
    #保存编辑按钮
    savebtn_loc = (By.XPATH,"//span[text()='保 存']/..")
    #取消编辑按钮
    cancelbtn_loc = (By.XPATH,"//*[text()='取 消']/..")


    account_loc = (By.CSS_SELECTOR,".ant-form-item-children>[placeholder='请输入账号']")
    psw_loc =(By.XPATH,"//input[@placeholder='请输入密码']")
    name_loc = (By.XPATH, "//input[@id='nickname']")
    phone_loc = (By.XPATH, "//input[@id='mobile']")
    email_loc = (By.XPATH,"//input[@placeholder='请输入邮箱']")
    gender_loc = (By.CSS_SELECTOR, ".ant-radio")
    calendar_loc = (By.XPATH,"//input[@placeholder='请选择生日']")
    birthday_loc = (By.XPATH,"//div[@class='ant-calendar-date-input-wrap']//input[@placeholder='请选择生日']")
    note_loc = (By.XPATH,"//textarea")
    label_loc=(By.XPATH,"//label[@for='mobile']")
    #下拉箭头
    arrow_loc= (By.XPATH,"//i[@class='anticon anticon-down ant-cascader-picker-arrow']")
    # 选择部门小×
    closecircle_loc = (By.XPATH,"//*[@class='anticon anticon-close-circle ant-cascader-picker-clear']")
    #关联门店小×
    #closecircle1_loc = (By.XPATH, "//*[@class='anticon anticon-close-circle']")



    depart_loc= (By.XPATH,"//li[@title='云盯科技']")
    depart1_loc= (By.XPATH,"// li[text() = '研发部']")

    position_loc = (By.XPATH, "// span[text() = '普通用户'] /../ span[1]")
    # 添加门店按钮
    addstore_loc = (By.XPATH,"//div[@class='ant-row']//*[@class='ant-btn ant-btn-primary']")
    #区域门店输入框
    storefiled_loc = (By.XPATH, "//input[@placeholder='请输入关键字搜索区域、门店']")

    searchstorebtn_loc = (By.XPATH,"//i[@class='anticon anticon-search ant-input-search-icon']")

    #storeselect_loc = (By.XPATH,"//span[text()='经营1门店']/../../../../span[@class='ant-tree-checkbox']")
    storeselect_loc = (By.XPATH,"//*[@class='ant-tree-checkbox']")
    #确定按钮
    confirmbtn_loc =(By.XPATH,"//span[text()='确 定']/..")
    #提交按钮
    submitbtn_loc = (By.XPATH,"//span[text()='提 交']/..")





    def click_configmng_loc(self):
        self.find_element(*self.configmng_loc).click()

    def click_org_loc(self):
        self.find_element(*self.org_loc).click()

    def click_userconfig_loc(self):
        self.find_element(*self.userconfig_loc).click()

    def click_createbtn_loc(self):
        self.find_element(*self.createbtn_loc).click()

    def input_account_loc(self,account):
        if account != None:
            self.send_key(account,*self.account_loc,clear=True)
        else:
            return

    def input_psw_loc(self,psw):
        if psw != None:
            self.send_key(psw,*self.psw_loc,clear=True)
        else:
            return

    def input_name_loc(self, name):
        if name != None:
            self.send_key(name,*self.name_loc,clear=True)
        else:
            return

    def input_phone_loc(self, pnumber):
        if pnumber!= None:
            self.send_key(pnumber,*self.phone_loc,clear=True)
        else:
            return

    def input_email_loc(self, email):
        if email != None:
            self.send_key(email,*self.email_loc,clear=True)
        else:
            return

    def click_gender_loc(self, n):
        self.find_elements(*self.gender_loc)[int(n)].click()

    def click_calendar_loc(self):
        self.find_element(*self.calendar_loc).click()

    def input_birthday_loc(self, day):
        if day != None:
            self.send_key(day,*self.birthday_loc,clear=True)
        else:
            return

    def input_note_loc(self, note):
        if note != None:
            self.send_key(note,*self.note_loc,clear=True)
        else:
            return

    def click_label_loc(self):
        self.find_element(*self.label_loc).click()

    def click_arrow_loc(self):
        self.find_element(*self.arrow_loc).click()

        # 点击小×
    def click_closecircle_loc(self):
        self.find_element(*self.closecircle_loc).click()
        #点击关联门店小×
    # def click_closecircle1_loc(self):
    #     self.find_elements(*self.closecircle1_loc)[0].click()


    def select_depart_loc(self,depart):
        self.find_element(By.XPATH, "//li[@title='"+ depart+"']").click()

    def select_depart1_loc(self,depart1):
        self.find_element(By.XPATH, "//li[text()='"+ depart1+"']").click()

    def select_position_loc(self):
        self.find_element(*self.position_loc).click()

    def click_addstore_loc(self):
        self.find_element(*self.addstore_loc).click()

    def input_storefiled_loc(self, storename):
        if storename != None:
            self.send_key(storename, *self.storefiled_loc,clear=True)
        else:
            return

    def click_searchstorebtn_loc(self):
        self.find_element(*self.searchstorebtn_loc).click()

    def click_storeselect_loc(self):
        self.find_element(*self.storeselect_loc).click()

    def click_confirmbtn_loc(self):
        self.find_element(*self.confirmbtn_loc).click()

    def click_submitbtn_loc(self):
        self.find_element(*self.submitbtn_loc).click()

    #for search user:
    #点击部门下拉箭头
    def click_seldpart_loc(self):
        self.find_element(*self.seldpart_loc).click()
    #选择部门
    def select_departlist_loc(self, departlist):
        if departlist != None:
            self.find_element(By.XPATH,"//span[@class='ant-select-tree-title' and text()='"+ departlist+"']").click()
        else:
            return
    #点击岗位下拉箭头
    #
    #选择岗位def click_selpostion_loc(self):
    #     self.find_element(*self.selpostion_loc).click()
    def select_positionlist_loc(self, positionlist):
        if positionlist != '':
            self.find_element(*self.selpostion_loc).click()
            self.find_element(By.XPATH,"//li[@role='option' and text()='"+ positionlist+"']").click()
        else:
            return
    #输入姓名账号
    def input_namefiled_loc(self, name):
        if name != None:
            self.send_key(name,*self.namefiled_loc,clear=True)
        else:
            return

    #点击搜索按钮
    def click_searchbtn_loc(self):
        self.find_element(*self.searchbtn_loc).click()

    #根据XPATH判断页面元素是否存在
    def is_element_exist(self,xpath):
        s = self.find_elements(By.XPATH, xpath)
        if len(s) == 0:
            print("元素未找到:%s")
            return False
        elif len(s) == 1:
            return True
        else:
            print("找到%s个元素：%s % (len(s)")
            return False
    #点击删除按钮
    def click_deletebtn_loc(self):
        self.find_element(*self.deletebtn_loc).click()
    #点击确定删除按钮
    def click_confirmdelbtn_loc(self):
        self.find_element(*self.confirmdelbtn_loc).click()
    #点击详情按钮
    def click_detailbtn_loc(self):
        self.find_element(*self.detailbtn_loc).click()
    #点击编辑按钮
    def click_edituserbtn_loc(self):
        self.find_element(*self.edituserbtn_loc).click()
    #点击保存按钮
    def click_savebtn_loc(self):
        self.find_element(*self.savebtn_loc).click()
    # 点击取消按钮
    def click_cancelbtn_loc(self):
        self.find_element(*self.cancelbtn_loc).click()


    # def select_optiongroup_loc(self, option_name):
    #     print("//ul[@role='listbox']//li[text()='"+ option_name+"']")
    #     self.find_element(By.XPATH, "//ul[@role='listbox']//li[text()='"+ option_name+"']").click()



