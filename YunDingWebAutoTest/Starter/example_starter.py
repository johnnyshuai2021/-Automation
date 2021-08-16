"""
AUTHOR: Seamus
DATE: 2020/09/14
DESCRIPTION:
"""

import os

from Starter.starter import Starter


class ExampleStarter(Starter):
    marker = 'example'
    test_paths = ['../TestCases/']
    additions = ['--alluredir=PytestReports\\report']


if __name__ == '__main__':
    ExampleStarter().start()
    # os.system('allure generate PytestReports\\report\\ -o PytestReports\\html\\ --clean')
    # os.system('allure serve -p 8819 PytestReports\\report')
