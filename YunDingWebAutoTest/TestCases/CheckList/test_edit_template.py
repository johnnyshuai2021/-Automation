# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/13
DESCRIPTION:详情页面编辑模板
"""

import pytest, allure, time
from Config.settings import GLOBAL_PARAMS
from PageObj.CheckList.page_check_list import CheckList
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestEditMarkist:

    @pytest.mark.check
    @fault_tolerant
    def test_edit_check_list_cancel(self, driver_setup, log, tag_params):
        """编辑模板-取消编辑"""
        common_name = GLOBAL_PARAMS[0]['common_text']
        template_name = common_name + random_string(7)

        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("取消编辑模板"):
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            time.sleep(2)
            before_name = check_list.get_detail_template_name()
            check_list.click_edit_button()
            check_list.input_template_name(template_name)
            check_list.click_cancel_edit()
            after_name = check_list.get_detail_template_name()

        with allure.step("断言"):
            assert before_name == after_name

    @pytest.mark.check
    @fault_tolerant
    def test_edit_check_list_confirm(self, driver_setup, log, tag_params):
        """编辑模板-确定编辑"""

        common_name = GLOBAL_PARAMS[0]['common_text']
        template_name = common_name + random_string(7)

        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("确认编辑模板"):
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            before_name = check_list.get_detail_template_name()
            check_list.click_edit_button()
            check_list.input_template_name(template_name)
            check_list.click_confirm_edit()
            time.sleep(2)
            after_name = check_list.get_detail_template_name()

        with allure.step("断言"):
            assert before_name != after_name


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
