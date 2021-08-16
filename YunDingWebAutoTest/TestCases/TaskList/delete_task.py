# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/11/10
DESCRIPTION:任务列表-删除任务
"""

import pytest, allure, time
from Config.settings import GLOBAL_PARAMS
from PageObj.TaskList.page_task import TaskListPage
from Utils.random_text import random_string
from Utils.fault_tolerant import fault_tolerant


class TestDeleteTask:

    @pytest.mark.task_mark
    @fault_tolerant
    def test_delete_task(self, driver_setup, log):
        """确认删除任务"""

        with allure.step("绕过登录页面"):
            task = TaskListPage(driver_setup)
            task.checker(driver_setup, log)

        with allure.step("进入任务列表页面"):
            task.click_shop_management()
            task.click_task_list()
        before_task = task.get_task_list_name()
        task.delete_task()
        task.delete_task_confirm()
        time.sleep(2)
        after_task = task.get_task_list_name()

        with allure.step("断言"):
            assert before_task != after_task


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
