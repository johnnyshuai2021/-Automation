# -*- coding:UTF-8 -*-
"""
AUTHOR: Johnny Shuai
DATE: 2021/01/08 Fri
DESCRIPTION:添加评分项
"""
import time

import pytest, allure
from Config.settings import GLOBAL_PARAMS
from PageObj.CheckList.page_check_list import CheckList
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestAddScoringItems:

    @pytest.mark.check
    @fault_tolerant
    def test_confirm_add_scoring_items(self, driver_setup, log, tag_params):
        """确认添加评分项"""

        items = GLOBAL_PARAMS[0]['common_text']
        items_name = items + random_string(7)
        score = GLOBAL_PARAMS[0]['score']
        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("确认添加评分项"):
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            check_list.click_add_scoring_items()
            check_list.input_score(score)
            check_list.input_point_content(items_name)
            check_list.click_confirm()
            time.sleep(2)
            scoring = check_list.get_detail_scoring_list()

        with allure.step("断言"):
            assert items_name in scoring

    @pytest.mark.check
    @fault_tolerant
    def test_cancel_add_scoring_items(self, driver_setup, log, tag_params):
        """取消添加评分项"""

        items = GLOBAL_PARAMS[0]['common_text']
        items_name = items + random_string(7)
        score = GLOBAL_PARAMS[0]['score']
        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("取消添加评分项"):
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            check_list.click_add_scoring_items()
            check_list.input_score(score)
            check_list.input_point_content(items_name)
            check_list.click_cancel()
            time.sleep(2)
            scoring = check_list.get_detail_scoring_list()

        with allure.step("断言"):
            assert items_name not in scoring


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
