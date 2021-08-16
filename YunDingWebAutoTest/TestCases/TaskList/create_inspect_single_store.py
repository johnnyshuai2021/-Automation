# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/11/09
DESCRIPTION:任务列表-创建巡单店任务
"""

import pytest, allure, time
from Config.settings import GLOBAL_PARAMS
from PageObj.TaskList.page_task import TaskListPage
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestCreateTask:

    @pytest.mark.task_mark
    @fault_tolerant
    def test_create_inspect_single_store(self, driver_setup, log):
        """创建巡单店任务"""

        store_name = GLOBAL_PARAMS[0]['single_store_name']
        task_name = GLOBAL_PARAMS[0]['common_text']
        person_name = GLOBAL_PARAMS[0]['person_name']
        template = GLOBAL_PARAMS[0]['template_name'][0]
        with allure.step("绕过登录页面"):
            task = TaskListPage(driver_setup)
            task.checker(driver_setup, log)

        with allure.step("进入任务列表页面"):
            task.click_shop_management()
            task.click_task_list()

        with allure.step("创建巡单店任务"):
            task.click_create_task()
            task.click_inspect_single_store()
            after_task_name = task_name + random_string(7)
            task.input_task_name(after_task_name)

            with allure.step("点击区域门店下拉框"):
                task.click_single_page_element(4)
            task.input_text(3, store_name)
            task.select_content()

            with allure.step("点击巡店类型下拉框"):
                task.click_single_page_element(5)
            task.click_on_site()

            with allure.step("点击巡店模板下拉框"):
                task.click_single_page_element(6)
            task.click_template_title(template)

            with allure.step("点击巡店人员下拉框"):
                task.click_single_person()

            task.input_text(4, person_name)
            task.select_person()

            task.click_submit_task()
            time.sleep(2)
            task_list_name = task.get_task_list_name()

        with allure.step("断言"):
            assert after_task_name in task_list_name


if __name__ == "__main__":
    pytest.main(['-s', f'{__file__}'])
