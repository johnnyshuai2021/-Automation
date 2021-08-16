# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/14
DESCRIPTION:切换模板
"""

import pytest, allure, time
from Config.settings import GLOBAL_PARAMS
from PageObj.CheckList.page_check_list import CheckList
from Utils.fault_tolerant import fault_tolerant


class TestSwitchTemplate:

    @pytest.mark.check
    @fault_tolerant
    def test_point_switch_to_mark(self, driver_setup, log, tag_params):
        """编辑模板-扣分模板切换为评分模板"""

        template_percent = GLOBAL_PARAMS[0]['persent']
        template_type = GLOBAL_PARAMS[0]['template_type'][0]
        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项菜单"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("扣分模板切换为评分模板"):
            check_list.click_select_template_status()
            check_list.click_select_points_status()
            check_list.click_search_template_button()
            check_list.click_template_detail()
            check_list.click_close_button(tag_params)
            check_list.click_edit_button()
            time.sleep(1)
            check_list.click_detail_mark()
            time.sleep(1)
            check_list.input_detail_template_percent(template_percent)
            check_list.click_confirm_edit()
            template = check_list.find_text(template_type)

        with allure.step("断言"):
            assert template


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
