"""
AUTHOR: Zhong xinqi
DATE: 2020/10/15
DESCRIPTION:运行标签为check的用例
"""

import os
from Starter.starter import Starter


class CheckStarter(Starter):
    marker = 'check'
    reruns = 1
    test_paths = ['../TestCases/']
    additions = ['--alluredir=../PytestReports/report', '--clean-alluredir']


if __name__ == '__main__':
    CheckStarter().start()
    os.system('allure generate ../PytestReports/report/ -o ../PytestReports/html/ --clean')
    os.system('allure serve -p 18819 ../PytestReports/report')
