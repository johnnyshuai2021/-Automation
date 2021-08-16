# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/07/29 Wed
DESCRIPTION:基础类
"""

import json
import requests
import time
from urllib import parse
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Config.settings import login_url1, home_url, domain, GLOBAL_PARAMS


class BasePage:

    def __init__(self, selenium_driver):
        self.driver = selenium_driver
        self.time = 0.3

    # 二次封装find_element方法
    def find_element(self, *loc):
        time.sleep(self.time)
        try:
            WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            raise Exception(u" %s 页面未找到元素 %s " % (self, loc))

    # 二次封装find_elements方法
    def find_elements(self, *loc):
        time.sleep(self.time)
        try:
            WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(loc))
            return self.driver.find_elements(*loc)
        except:
            raise Exception(u" %s 页面未找到元素 %s ", (self, loc))

    # 二次封装send_keys方法
    def send_key(self, value, *loc, clear=None):
        time.sleep(self.time)
        try:
            WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located(loc))
            if clear:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except:
            raise Exception(u" %s 未找到 %s 元素" % (self, loc))

    # 查找text
    def find_text(self, content):
        message = "//*[contains(text(), '{}')]".format(content)
        try:
            WebDriverWait(self.driver, 10, 0.1).until(EC.visibility_of_element_located((By.XPATH, message)))
            return True
        except:
            return False

    # 获取Set-Cookies 和user_data
    def session_id(self, log):
        try:
            login_url = login_url1
            # print(login_url)
            data = {
                'account': GLOBAL_PARAMS[0]['account'],
                'enterpriseCode': GLOBAL_PARAMS[0]['enterprise'],
                'password': GLOBAL_PARAMS[0]['port_password']
            }
            headers = {
                'Accept': 'application/json, text/plain, */*',
                'api-version': 'v1',
                'Content-Type': 'application/json;charset=UTF-8'
            }
            _response = requests.post(login_url, data=json.dumps(data), headers=headers)
            user_data = _response.text
            user_data_encode = parse.quote(user_data)
            # 对返回数据进行url编码
            set_cookies = _response.headers['Set-Cookie'].split(';')[0]
            # log.info('获取Set-Cookie: {}'.format(set_cookies))
            return set_cookies, user_data_encode
        except BaseException as e:
            log.error('获取Set-Cookie失败: {} '.format(e))

    # 写入cookies和userdata'
    def user_cookies(self, get_driver, log):
        login_code = GLOBAL_PARAMS[0]['loginCode']
        get_driver.get(home_url)
        _session_id = self.session_id(log)[0]
        user_data_encode = self.session_id(log)[1]
        log.info('session_id {}'.format(_session_id))
        cookies = [{'domain': domain,
                    'httpOnly': False,
                    'name': 'login',
                    'path': '/', 'secure': False,
                    'value': 'true'}]
        js = f'''
        var storage = window.localStorage;
        storage.setItem("userData", "{user_data_encode}");
        storage.setItem("loginCode", '{login_code}');
        '''
        get_driver.execute_script(js)
        for cookie in cookies:
            get_driver.add_cookie(cookie)

    # 为了解决绕过登录会刷新2次home页面的问题
    def checker(self, get_driver, log):
        if get_driver.current_url == 'data:,':
            log.info('rerun时重启driver, 执行登录')
            self.user_cookies(get_driver, log)
        get_driver.get(home_url)

    def __find_ele(self,locator=""):
        '''
        支持八种定位方式
        :param locator: xpath=//*[@id="username"]
        :return: 放回定位到的元素
        '''
        ele = None
        self.ele = None
        if locator.startswith('xpath='):
            ele = self.driver.find_element_by_xpath(locator[locator.find('=') + 1:])
        elif locator.startswith('id='):
            ele = self.driver.find_element_by_id(locator[locator.find('=') + 1:])
        elif locator.startswith('name='):
            ele = self.driver.find_element_by_name(locator[locator.find('=') + 1:])
        elif locator.startswith('tag_name='):
            ele = self.driver.find_element_by_tag_name(locator[locator.find('=') + 1:])
        elif locator.startswith('link_text='):
            ele = self.driver.find_element_by_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('partial_link_text='):
            ele = self.driver.find_element_by_partial_link_text(locator[locator.find('=') + 1:])
        elif locator.startswith('css_selector='):
            ele = self.driver.find_element_by_partial_css_selector(locator[locator.find('=') + 1:])
        else :
            ele= self.driver.find_element_by_xpath(locator)
        self.ele = ele
        return ele
