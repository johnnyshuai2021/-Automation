"""
AUTHOR: Seamus
DATE: 2020/09/14
DESCRIPTION:按指定顺序运行case
"""

import os

from Starter.starter import Starter
from Utils.parse_error import get_error


class ExampleGroupStarter(Starter):
    stdout = True
    reruns = 0
    reruns_delay = 5
    nodes = [
        # './TestCases/Example/test_case2.py::TestCase2::test_case2_1',
        # './TestCases/Example/test_case1.py::TestCase1'
        '../TestCases/Login/test_account_login.py',
        '../TestCases/TaskList/create_inspect_single_store.py',
        '../TestCases/CheckList/test_add_category.py::TestAddCategory::test_cancel_add_category',
        '../TestCases/CheckList/test_add_category.py::TestAddCategory::test_confirm_add_category',
        '../TestCases/CheckList/test_scoring_items.py::TestAddScoringItems::test_confirm_add_scoring_items',
        '../TestCases/CheckList/test_scoring_items.py::TestAddScoringItems::test_cancel_add_scoring_items',
        '../TestCases/CheckList/test_create_mark_template.py',
        '../TestCases/CheckList/test_create_points_template.py',
        '../TestCases/CheckList/test_edit_template.py::TestEditMarkist::test_edit_check_list_cancel',
        '../TestCases/CheckList/test_edit_template.py::TestEditMarkist::test_edit_check_list_confirm',
        '../TestCases/CheckList/test_point_switch_to_mark.py',
        '../TestCases/CheckList/test_mark_switch_to_point.py',
        '../TestCases/TaskList/create_inspect_multiple_stores.py',
        '../TestCases/TaskList/delete_task.py',
        '../TestCases/CheckList/test_delete_template.py::TestDeleteMarkist::test_delete_check_list_confirm',
        '../TestCases/CheckList/test_delete_template.py::TestDeleteMarkist::test_delete_check_list_cancel',

    ]
    additions = ['--alluredir=../PytestReports/report', '--clean-alluredir']


if __name__ == '__main__':
    exit_code = ExampleGroupStarter().start()
    print(get_error(exit_code))
    if exit_code in (0, 1):
        os.system('allure generate ../PytestReports/report/ -o ../PytestReports/html/ --clean')
        os.system('allure serve -p 8819 ../PytestReports/report')
