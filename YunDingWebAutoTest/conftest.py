# coding = utf-8
"""
Author: 钟欣琪
Date: 2020-8-04
Remarks: conftest配置文件（自定义fixtrue）
"""

import pytest, logging
from selenium import webdriver
from Config.settings import GLOBAL_PARAMS


# 启动driver
@pytest.fixture(scope='session')
def driver_setup(request, log):
    log.info('初始化Driver开始')
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    def driver_close():
        driver.quit()

    request.addfinalizer(driver_close)
    return driver


# 环境变量添加到Allure报告中
def pytest_sessionfinish(session):
    with open("{}/PytestReports/report/environment.properties".format(session.config.rootdir), "w",
              encoding='utf-8') as f:
        f.write(f'WEB_NAME={GLOBAL_PARAMS[0]["WEB_NAME"]}\nWEB_VERSION={GLOBAL_PARAMS[0]["web_version"]}'
                f'\nBROWSER_NAME={GLOBAL_PARAMS[0]["BROWSER_NAME"]}\nSELENIUM_VERSION={GLOBAL_PARAMS[0]["SELENIUM_VERSION"]}')


# 实时日志
@pytest.fixture(scope='session')
def log():
    yield logging.getLogger()


# 解决找不到关闭按钮，等待时间过长的问题
@pytest.fixture(scope='session')
def tag_params():
    yield {'closeTag': 0}
