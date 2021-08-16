# -*- coding:UTF-8 -*-
"""
AUTHOR: Johnny Shuai
DATE: 2021/01/08 Fri
DESCRIPTION:创建检查项模板-评分模板
"""

import pytest, allure
from Config.settings import GLOBAL_PARAMS
from PageObj.CheckList.page_check_list import CheckList
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestCreateMarkist:

    @pytest.mark.check
    @fault_tolerant
    def test_create_mark_list(self, driver_setup, log, tag_params):
        """创建检查项模板-评分模板"""

        template_percent = GLOBAL_PARAMS[0]['persent']
        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("创建评分模板"):
            check_list.click_create_template()
            list_name = GLOBAL_PARAMS[0]['common_text']
            template_name = list_name + random_string(7)
            check_list.input_template_name(template_name)
            check_list.click_mark_template()
            check_list.input_template_percent(template_percent)
            check_list.click_submit_template()
            check_list.click_close_button(tag_params)

        with allure.step("断言"):
            reault = check_list.find_text(template_name)
            assert reault


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
