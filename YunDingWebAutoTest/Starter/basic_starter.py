# coding = utf-8
"""
Author: 钟欣琪
Date:2019/08/21
DESCRIPTION:运行所有测试用例
tag 使用说明：
* ： basic: 常用功能的正向用例
* ：  
"""

import os

from Starter.starter import Starter


class BasicStarter(Starter):
    verbose = True
    stdout = True
    reruns = 1
    reruns_delay = 5
    marker = 'basic'
    test_paths = [
        './TestCases/'
    ]
    additions = ['--alluredir=PytestReports/report']


if __name__ == '__main__':
    BasicStarter().start()
    os.system('allure generate PytestReports/report/ -o PytestReports/html/ --clean')
    os.system('allure serve -p 8889 PytestReports/report')

