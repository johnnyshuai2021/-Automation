# coding:utf-8
"""
Author: 钟欣琪
Date: 2020/8/17
Description: 用例失败后截图
* 2021/02/20: 用例失败后添加浏览器控制台信息到报告
"""
import allure, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from functools import wraps


def fault_tolerant(function):
    # 作用清除__excute函数名字和注释文档,让函数名字和注释文档指向正在执行的函数
    @wraps(function)
    def _excute(self, driver_setup, log, *args, **kwargs):
        try:
            function(self, driver_setup, log, *args, **kwargs)
        except BaseException as e:
            log.error(e)
            chrome_logs = driver_setup.get_log('browser')
            error_log = [c for c in chrome_logs if c['level'] == 'SEVERE']
            log.error('浏览器控制台错误信息：{}'.format(error_log))
            allure.attach(driver_setup.get_screenshot_as_png(), "Screenshots", allure.attachment_type.PNG)
            log.error(f"用例执行失败堆栈信息如下：\n{e}", exc_info=True)
            raise

    return _excute
