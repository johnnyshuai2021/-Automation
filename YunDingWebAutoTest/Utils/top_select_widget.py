# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/20
DESCRIPTION: 页面顶部框
"""

import time
from selenium.webdriver.common.by import By
from PageObj.page_base import BasePage
from selenium.webdriver.common.keys import Keys


class TopWidget(BasePage):
    start_time_loc = (By.CSS_SELECTOR, '.ant-calendar-range-part.ant-calendar-range-left>div>div>input')  # 开始日期
    end_time_loc = (By.CSS_SELECTOR, '.ant-calendar-range-part.ant-calendar-range-right>div>div>input')  # 结束日期
    calendar_loc = (By.CSS_SELECTOR, '.ant-calendar-picker-input.ant-input')  # 日历框
    top_nav_loc = (By.CSS_SELECTOR, '#top-nav')  # 顶部栏
    area_loc = (By.CSS_SELECTOR, "span.ant-select-search__field__placeholder")  # 下拉框
    check_box_loc = (By.CSS_SELECTOR, "span.ant-select-tree-checkbox-inner")  # 多选框
    tree_title_loc = (By.CSS_SELECTOR, "span.ant-select-tree-title")  # 门店名字
    area_input_box_loc = (By.CSS_SELECTOR, ".ant-select-search__field")  # 区域门店输入框
    shop_personnel_loc = (
        By.CSS_SELECTOR, ".personSelectStyle.ant-select.ant-select-enabled.ant-select-allow-clear")  # 巡店人员框

    @staticmethod
    def check_time_format(_date_time):
        try:
            time.strptime(_date_time, "%Y-%m-%d")
            year, month, day = _date_time.split('-')
            if 1 in (len(month), len(day)): return False
            return True
        except ValueError:
            return False

    # 选择日历开始和结束时间
    def select_date_time(self, start_time, end_time):
        """
        :start_time: 开始日期
        :end_time: 结束日期
        """

        # 检查日期输入格式是否正确
        check_start, check_end = [TopWidget.check_time_format(i) for i in (start_time, end_time)]
        compare = lambda x, y: x <= y
        if not check_start & check_end or not compare(start_time, end_time):
            raise ValueError('开始和结束时间格式为“YYYY-mm-dd”！且开始时间不能大于结束时间！请检查！！')

        # 输入开始和结束日期
        for _index, _time in enumerate([start_time, end_time]):
            self.find_element(*self.calendar_loc).click()
            _loc = self.start_time_loc if _index == 0 else self.end_time_loc

            if not _index:
                self.send_key(_time, *_loc)
                year, month, day = _time.split('-')
                self.find_element(By.CSS_SELECTOR, '[title="{}年{}月{}日"]'.format(year, int(month), int(day))).click()
            else:
                endElement = self.find_element(*_loc)
                endElement.send_keys(Keys.CONTROL, 'a')
                endElement.send_keys(Keys.BACKSPACE)
                self.send_key(_time, *_loc)
                self.find_element(*self.top_nav_loc).click()

    # 适用多选框，传入区域或者门店名称，选中输入的区域或者门店
    def select_store(self, store_name, _index=-1):
        """
        :store_name: 区域或者门店名称
        ：_index=-1: 输入的门店或者区域的索引值，调用时不用修改值
        """

        self.find_element(*self.area_loc).click()
        self.send_key(store_name, *self.area_input_box_loc)
        check_box_elements = self.find_elements(*self.check_box_loc)
        check_box_elements[_index].click()

    # 传入巡店人员名字，选择传入的人员
    def select_person(self, name):
        """
        :name : 巡店人员名字
        """

        shop_personnel_name_loc = (By.XPATH, f"//li[contains(text(), '{name}')]")
        self.find_element(*self.shop_personnel_loc).click()
        self.find_element(*shop_personnel_name_loc).click()
