# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/16
DESCRIPTION:列表页面删除模板
"""

import pytest, allure
from Config.settings import GLOBAL_PARAMS
from PageObj.CheckList.page_check_list import CheckList
from Utils.fault_tolerant import fault_tolerant


class TestDeleteMarkist:

    # @pytest.mark.repeat(50)
    @pytest.mark.check
    @fault_tolerant
    def test_delete_check_list_confirm(self, driver_setup, log):
        """删除模板-确定"""

        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项页面"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("删除第一个模板"):
            check_list.click_delete_template()
            check_list.click_confirm_delete_template()

        with allure.step("获取弹窗提示内容"):
            alert = check_list.find_text(GLOBAL_PARAMS[0]['alert'])

        with allure.step("断言"):
            assert alert

    @pytest.mark.check
    @fault_tolerant
    def test_delete_check_list_cancel(self, driver_setup, log):
        """删除模板-取消"""

        with allure.step("绕过登录页面"):
            check_list = CheckList(driver_setup)
            check_list.checker(driver_setup, log)

        with allure.step("打开巡店检查项页面"):
            check_list.click_shop_management()
            check_list.click_check_management()

        with allure.step("删除第一个模板"):
            before_template_name = check_list.get_template_name()
            check_list.click_delete_template()
            check_list.click_cancel_delete_template()
            after_template_name = check_list.get_template_name()

        with allure.step("断言"):
            assert before_template_name == after_template_name


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
