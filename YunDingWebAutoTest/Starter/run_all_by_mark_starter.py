"""
AUTHOR: Seamus
DATE: 2020/09/14
DESCRIPTION:通过用例的标签来运行case，用例执行顺序按照用例名称的首字母排序执行
"""

import os

from Starter.starter import Starter


class ExampleStarter(Starter):
    marker = 'example'
    test_paths = ['../TestCases/']
    additions = ['--alluredir=PytestReports/report']


if __name__ == '__main__':
    ExampleStarter().start()
    # os.system('allure generate PytestReports/report/ -o PytestReports/html/ --clean')
    # os.system('allure serve -p 8819 PytestReports/report')
