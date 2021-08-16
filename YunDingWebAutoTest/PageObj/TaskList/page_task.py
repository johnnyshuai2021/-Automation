# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/13 Tue
DESCRIPTION:
"""

import os, sys, allure
from PageObj.page_base import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TaskListPage(BasePage):
    shop_management_loc = (By.XPATH, "//*[contains(text(), '巡店管理')]")
    task_list_loc = (By.CSS_SELECTOR, '#巡店管理\$Menu>li:nth-child(1)')
    calendar_loc = (By.CSS_SELECTOR, '.iconfont.icon-Calendar.ant-calendar-picker-icon')  # 日历框
    # start_time_loc = (By.CSS_SELECTOR, '.ant-calendar-range-part.ant-calendar-range-left>div>div>input')  # 开始日期
    # end_time_loc = (By.CSS_SELECTOR, '.ant-calendar-range-part.ant-calendar-range-right>div>div>input')  # 结束日期
    start_time_loc = (By.CSS_SELECTOR, '.ant-calendar-picker-input.ant-input>input:nth-child(1)')  # 开始日期
    end_time_loc = (By.CSS_SELECTOR, '.ant-calendar-range-part.ant-calendar-range-right>div>div>input')  # 结束日期
    create_task_loc = (By.CSS_SELECTOR, ".create-task>.ant-btn.ant-btn-primary")  # 创建任务按钮
    task_list_name_loc = (By.CSS_SELECTOR, ".flex-item>p")  # 任务名称
    inspect_single_store_loc = (
        By.CSS_SELECTOR, ".ant-radio-group.ant-radio-group-outline.single>label:nth-child(2)>span:nth-child(1)")  # 巡单店
    stores_box_loc = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal>div:nth-child(6)>div:nth-child(2)")  # 区域门店下拉框
    search_store_loc = (
        By.CSS_SELECTOR, ".ant-select-focused.ant-select-enabled.ant-select-allow-clear>span>ul>li>span>input")  # 搜索门店
    select_stores_loc = (By.CSS_SELECTOR, ".ant-select-tree-checkbox-inner")  # 选择门店，定位一组元素
    select_single_stores_loc = (By.CSS_SELECTOR, '.ant-select-tree-title')  # 选择单个门店
    task_name_loc = (By.CSS_SELECTOR, ".ant-form-item-children>input")  # 任务名称输入框
    person_box_loc = (By.CSS_SELECTOR, ".ant-select-selection__rendered>span")  # 巡店人员下拉框
    single_page_loc = (By.CSS_SELECTOR, ".ant-select-selection__rendered")  # 定位一组元素

    search_person_loc = (By.CSS_SELECTOR, ".ant-select-dropdown-search>span>input")  # 巡店人员搜索框
    select_person_loc = (By.CSS_SELECTOR, ".ant-select-tree-treenode-switcher-open>ul")  # 选择巡店人员框
    store_inspectiontype_type_loc = (
        By.CSS_SELECTOR, ".ant-form.ant-form-horizontal>div:nth-child(3)>div:nth-child(2)")  # 巡店类型下拉框
    real_time_loc = (By.XPATH, '//li[contains(text(), "实时巡店" )]')  # 实时巡店
    on_site_loc = (By.XPATH, '//li[contains(text(), "现场巡店" )]')  # 现场巡店
    video_loc = (By.XPATH, '//li[contains(text(), "录像巡店" )]')  # 录像巡店
    template_box_loc = (By.CSS_SELECTOR, ".ant-form.ant-form-horizontal>div:nth-child(5)")  # 巡店模板下拉框
    task_remark_loc = (
        By.CSS_SELECTOR,
        ".ant-form.ant-form-horizontal>div:nth-child(10)>div:nth-child(2)>div>span>textarean")  # 任务备注输入框
    submit_task_loc = (By.CSS_SELECTOR, ".create-task-button>button:nth-child(1)")  # 创建按钮
    cancel_submit_task_loc = (By.CSS_SELECTOR, ".create-task-button>button:nth-child(2)")  # 取消创建任务按钮
    close_loc = (By.CSS_SELECTOR, ".ant-modal-close-x")  # 关闭弹窗
    input_text_loc = (By.CSS_SELECTOR, "input.ant-select-search__field")  # 搜索输入框
    person_loc = (By.CSS_SELECTOR, 'span[title="七七1"]')  # 巡店人员名字
    check_box_loc = (By.CSS_SELECTOR, "span.ant-select-tree-checkbox-inner")  # 多选框
    delete_task_loc = (By.CSS_SELECTOR, ".svg-icon.delItem-icon")  # 删除按钮
    confirm_delete_loc = (By.CSS_SELECTOR, ".ant-modal-confirm-btns>button:nth-child(2)")  # 确认删除按钮
    task_top_loc = (By.CSS_SELECTOR, ".ant-modal-title")  # 新建任务弹窗顶部
    single_person_loc = (By.CSS_SELECTOR, ".ant-select-search__field__placeholder")  # 新建任务弹窗顶部

    @allure.step("点击巡店人员下拉框")
    def click_single_person(self):
        elements = self.find_elements(*self.single_person_loc)
        elements[2].click()

    @allure.step("删除任务")
    def delete_task(self):
        elements = self.find_elements(*self.delete_task_loc)
        elements[0].click()

    @allure.step("点击新建任务框顶部")
    def click_task_top(self):
        self.find_element(*self.task_top_loc).click()

    @allure.step("确认删除任务")
    def delete_task_confirm(self):
        self.find_element(*self.confirm_delete_loc).click()

    @allure.step("点击创建任务按钮")
    def click_create_task(self):
        self.find_element(*self.create_task_loc).click()

    @allure.step("选择巡店人员")
    def select_person(self):
        self.find_element(*self.person_loc).click()

    @allure.step("选择区域门店")
    def select_multiple_area(self, store_name, _index=-1):
        self.input_text(4, store_name)
        check_box_elements = self.find_elements(*self.check_box_loc)
        check_box_elements[_index].click()

    # 创建任务单巡店页面输入搜索的名字
    def input_text(self, _index, _text):
        """

        :param _index: 传1：单店区域门店搜索框，4：单店巡店人员搜索框、多店区域搜索框， 5：单店报告通知人搜索框
        :param _text: 传入名称
        :return:
        """
        elements = self.find_elements(*self.input_text_loc)
        elements[_index].send_keys(_text)

    @allure.step("点击日历图标")
    def click_calendar(self):
        self.find_element(*self.calendar_loc).click()

    @allure.step("输入开始时间")
    def input_start_time(self, start_time):
        self.send_key(start_time, *self.start_time_loc, clear=True)

    @allure.step("输入结束时间")
    def input_end_time(self, end_time):
        self.send_key(end_time, *self.end_time_loc, clear=True)

    @allure.step("选择输入的目标")
    def select_content(self):
        elements = self.find_elements(*self.select_single_stores_loc)
        elements[-1].click()

    @allure.step("点击创建任务按钮")
    def click_create_task(self):
        self.find_element(*self.create_task_loc).click()

    @allure.step("下拉框选择门店")
    def click_select_stores(self):
        buttons = self.find_elements(*self.select_stores_loc)
        buttons[1].click()

    @allure.step("输入门店名称")
    def input_stores_name(self, name):
        self.send_key(name, *self.stores_box_loc, clear=True)

    @allure.step("点击任务列表")
    def click_task_list(self):
        self.find_element(*self.task_list_loc).click()

    @allure.step("点击巡单店")
    def click_inspect_single_store(self):
        self.find_element(*self.inspect_single_store_loc).click()

    @allure.step("点击巡店管理")
    def click_shop_management(self):
        self.find_element(*self.shop_management_loc).click()

    @allure.step("点击区域门店下拉框")
    def click_stores_box(self):
        self.find_element(*self.stores_box_loc).click()

    @allure.step("输入任务名称")
    def input_task_name(self, name):
        self.send_key(name, *self.task_name_loc, clear=True)

    @allure.step("输入门店名称搜索门店")
    def input_store_name(self, name):
        self.send_key(name, *self.search_store_loc, clear=True)

    @allure.step("输入任务备注")
    def input_task_remark(self, name):
        self.send_key(name, *self.task_remark_loc, clear=True)

    @allure.step("输入巡店人员名称")
    def input_person_name(self, name):
        self.send_key(name, *self.search_person_loc, clear=True)

    @allure.step("点击巡店人员下拉框")
    def click_person_box(self):
        self.find_element(*self.person_box_loc).click()

    # 创建单店页面元素,参数传4：区域门店下拉框 5：巡店类型下拉框 6：巡店模板 7：巡店人员 8：报告通知人
    # 创建多店任务页面元素，参数7： 区域门店下拉框
    def click_single_page_element(self, _index):
        elements = self.find_elements(*self.single_page_loc)
        elements[_index].click()

    @allure.step("点击选择巡店人员")
    def click_select_person(self):
        self.find_element(*self.select_person_loc).click()

    @allure.step("点击巡店类型下拉框")
    def click_store_inspectiontype_type(self):
        self.find_element(*self.store_inspectiontype_type_loc).click()

    @allure.step("选择实时巡店")
    def click_real_time(self):
        self.find_element(*self.real_time_loc).click()

    @allure.step("选择现场巡店")
    def click_on_site(self):
        self.find_element(*self.on_site_loc).click()

    @allure.step("选择录像巡店")
    def click_video(self):
        self.find_element(*self.video_loc).click()

    @allure.step("点击巡店模板下拉框")
    def click_template_box(self):
        self.find_element(*self.template_box_loc).click()

    @allure.step("点击选择模板")
    def click_template_title(self, name):
        template_title_loc = (By.XPATH, f"//li[contains(text(), '{name}')]")
        self.find_element(*template_title_loc).click()

    @allure.step("点击创建按钮")
    def click_submit_task(self):
        self.find_element(*self.submit_task_loc).click()

    @allure.step("点击取消按钮")
    def click_cancel_submit_task(self):
        self.find_element(*self.cancel_submit_task_loc).click()

    @allure.step("点击巡店模板下拉框")
    def click_close(self):
        self.find_element(*self.close_loc).click()

    @allure.step("获取所有任务名称")
    def get_task_list_name(self):
        task_list = self.find_elements(*self.task_list_name_loc)
        name = [i.text for i in task_list]
        return name
