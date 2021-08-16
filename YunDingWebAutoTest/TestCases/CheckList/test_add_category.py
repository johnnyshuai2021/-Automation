# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/14
DESCRIPTION: 添加评分项
"""

import pytest, allure, time
from Config.settings import GLOBAL_PARAMS
from PageObj.CheckList.page_check_list import CheckList
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestAddCategory:

    @pytest.mark.check
    @fault_tolerant
    def test_confirm_add_category(self, driver_setup, log, tag_params):
        """确认添加分类"""

        category = GLOBAL_PARAMS[0]['common_text']
        category_name = category + random_string(7)
        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("确认添加分类"):
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            check_list.click_add_classification()
            check_list.input_description(category_name)
            check_list.click_confirm()
            time.sleep(1)
            name = check_list.get_detail_template_catefory_list()

        with allure.step("断言"):
            assert category_name in name

    @pytest.mark.check
    @fault_tolerant
    def test_cancel_add_category(self, driver_setup, log, tag_params):
        """取消添加分类"""

        category = GLOBAL_PARAMS[0]['common_text']
        category_name = category + random_string(7)
        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("取消添加分类"):
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            before_name = check_list.get_detail_template_catefory_list()
            check_list.click_add_classification()
            check_list.input_description(category_name)
            check_list.click_cancel()
            time.sleep(1)
            after_name = check_list.get_detail_template_catefory_list()

        with allure.step("断言"):
            assert before_name == after_name


if __name__ == "__main__":
    pytest.main(['-s', f'{__file__}'])
