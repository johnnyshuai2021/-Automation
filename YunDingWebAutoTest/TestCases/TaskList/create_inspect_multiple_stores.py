# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/10/16
DESCRIPTION:任务列表-创建巡多店任务
"""

import pytest, allure, time
from Config.settings import GLOBAL_PARAMS
from PageObj.TaskList.page_task import TaskListPage
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestCreateTask:

    @pytest.mark.task_mark
    @fault_tolerant
    def test_create_inspect_multiple_stores(self, driver_setup, log):
        """创建巡多店任务"""

        area_name = GLOBAL_PARAMS[0]['area_name']
        task_name = GLOBAL_PARAMS[0]['common_text']
        person_name = GLOBAL_PARAMS[0]['person_name']
        template = GLOBAL_PARAMS[0]['template_name'][0]
        with allure.step("绕过登录页面"):
            task = TaskListPage(driver_setup)
            task.checker(driver_setup, log)

        with allure.step("进入任务列表页面"):
            task.click_shop_management()
            task.click_task_list()

        with allure.step("创建巡多店任务"):
            task.click_create_task()
            after_task_name = task_name + random_string(7)
            task.input_task_name(after_task_name)
            task.click_person_box()
            task.input_person_name(person_name)
            task.click_select_person()
            task.click_store_inspectiontype_type()
            task.click_real_time()
            task.click_template_box()
            task.click_template_title(template)
            task.select_multiple_area(area_name)
            task.click_submit_task()
            time.sleep(2)
            task_list_name = task.get_task_list_name()

        with allure.step("断言"):
            assert after_task_name in task_list_name


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
