# -*- coding:UTF-8 -*-
"""
AUTHOR: Zhong xinqi
DATE: 2020/12/08
DESCRIPTION:记录用户使用记录
"""

import pytest, allure, time
from PageObj.page_base import BasePage
from PageObj.Login.page_login import Login
from Config.settings import SERVER, GLOBAL_PARAMS
url_list = ['http://192.168.0.227:8888/V1/auth/list',
  'http://192.168.0.227:8888/V1/auth/edit/:id',
  'http://192.168.0.227:8888/V1/auth/create',
  'http://192.168.0.227:8888/V1/cashier/list',
  'http://192.168.0.227:8888/V1/cashier/report',
  'http://192.168.0.227:8888/V1/cashier/conf/base',
  'http://192.168.0.227:8888/V1/cashier/conf/pos',
  'http://192.168.0.227:8888/V1/cashier/create',
  'http://192.168.0.227:8888/V1/customerAnalysis/store',
  'http://192.168.0.227:8888/V1/customerAnalysis/group',
  'http://192.168.0.227:8888/V1/customerCompareGroup',
  'http://192.168.0.227:8888/V1/customerCompareStore',
  'http://192.168.0.227:8888/V1/customer',
  'http://192.168.0.227:8888/V1/customer/details/:id',
  'http://192.168.0.227:8888/V1/entry/videoEntry',
  'http://192.168.0.227:8888/V1/entry/imgEntry',
  'http://192.168.0.227:8888/V1/equipment/list',
  'http://192.168.0.227:8888/V1/export/config',
  'http://192.168.0.227:8888/V1/export/list',
  'http://192.168.0.227:8888/V1/export/record',
  'http://192.168.0.227:8888/V1/flow/conf',
  'http://192.168.0.227:8888/V1/home',
  'http://192.168.0.227:8888/V1/hotspot/conf',
  'http://192.168.0.227:8888/V1/hotspot/analysis/deviceHeat',
  'http://192.168.0.227:8888/V1/hotspot/analysis/storeHeat',
  'http://192.168.0.227:8888/V1/hotspot/analysis/heatStatistics',
  'http://192.168.0.227:8888/V1/imgGallery/cashier',
  'http://192.168.0.227:8888/V1/login',
  'http://192.168.0.227:8888/V1/member/analysis',
  'http://192.168.0.227:8888/V1/member/analysis/ageTrend',
  'http://192.168.0.227:8888/V1/member/analysis/repurchase',
  'http://192.168.0.227:8888/V1/member/analysis/newMember',
  'http://192.168.0.227:8888/V1/member/list',
  'http://192.168.0.227:8888/V1/member/conf',
  'http://192.168.0.227:8888/V1/member/car/conf',
  'http://192.168.0.227:8888/V1/member/visit',
  'http://192.168.0.227:8888/V1/member/car/visit',
  'http://192.168.0.227:8888/V1/member/visit/recomer/:id',
  'http://192.168.0.227:8888/V1/member/visit/recomernew/:id',
  'http://192.168.0.227:8888/V1/member/detail/:id',
  'http://192.168.0.227:8888/V1/member/add',
  'http://192.168.0.227:8888/V1/member/edit/:id',
  'http://192.168.0.227:8888/V1/member/intentionDetail/:id',
  'http://192.168.0.227:8888/V1/movingline/conf',
  'http://192.168.0.227:8888/V1/analysis/conf',
  'http://192.168.0.227:8888/V1/notificationMessage/index',
  'http://192.168.0.227:8888/V1/passengerStore',
  'http://192.168.0.227:8888/V1/passengerArea',
  'http://192.168.0.227:8888/V1/passengerBatch',
  'http://192.168.0.227:8888/V1/passengerCompareGroup',
  'http://192.168.0.227:8888/V1/compareStore',
  'http://192.168.0.227:8888/V1/passwordSecurity/configuration',
  'http://192.168.0.227:8888/V1/patrol/task/list',
  'http://192.168.0.227:8888/V1/patrol/realTime',
  'http://192.168.0.227:8888/V1/patrol/patrolVideotape/videoTapePageV',
  'http://192.168.0.227:8888/V1/patrol/patrolVideotape/videoTapePageC',
  'http://192.168.0.227:8888/V1/patrol/patrolVideotape/videoTapePageVideo',
  'http://192.168.0.227:8888/V1/patrol/patrolVideotape/list',
  'http://192.168.0.227:8888/V1/patrol/patrolCustom/list',
  'http://192.168.0.227:8888/V1/patrol/patrolDrafts/list',
  'http://192.168.0.227:8888/V1/patrol/patrolDrafts/details/:id',
  'http://192.168.0.227:8888/V1/patrolGallery/index',
  'http://192.168.0.227:8888/V1/patrolReport/list',
  'http://192.168.0.227:8888/V1/patrolReport/details/:id',
  'http://192.168.0.227:8888/V1/patrolReport/summarizie/list',
  'http://192.168.0.227:8888/V1/realitime',
  'http://192.168.0.227:8888/V1/snapPatrol/config',
  'http://192.168.0.227:8888/V1/snapPatrol/imgList',
  'http://192.168.0.227:8888/V1/snapPatrol/patrol',
  'http://192.168.0.227:8888/V1/snapPatrol/list',
  'http://192.168.0.227:8888/V1/statistics/behavior',
  'http://192.168.0.227:8888/V1/statistics/results',
  'http://192.168.0.227:8888/V1/stores/list',
  'http://192.168.0.227:8888/V1/stores/conf',
  'http://192.168.0.227:8888/V1/stores/myCars',
  'http://192.168.0.227:8888/V1/stores/cars',
  'http://192.168.0.227:8888/V1/system/record',
  'http://192.168.0.227:8888/V1/system/operationLog',
  'http://192.168.0.227:8888/V1/system/accessLog',
  'http://192.168.0.227:8888/V1/templates',
  'http://192.168.0.227:8888/V1/templates/detail/:id',
  'http://192.168.0.227:8888/V1/users/employee/add',
  'http://192.168.0.227:8888/V1/users/employee/edit/:id',
  'http://192.168.0.227:8888/V1/users/employee',
  'http://192.168.0.227:8888/V1/videoAdmin/realTime',
  'http://192.168.0.227:8888/V1/videoAdmin/upload',
  'http://192.168.0.227:8888/V1/videoAdmin/upload/queryUploadData/:id',
  'http://192.168.0.227:8888/V1/videoGallery/video',
  'http://192.168.0.227:8888/V1/videoGallery/custom',
  'http://192.168.0.227:8888/V1/warning/list',
  'http://192.168.0.227:8888/V1/warning/detail',
  'http://192.168.0.227:8888/V1/warning/conf',
  'http://192.168.0.227:8888/V1/warning/edit',
  'http://192.168.0.227:8888/V1/warning/message',
  'http://192.168.0.227:8888/V1/warning/statistics',
  'http://192.168.0.227:8888/V1/warning/managemessage',
  'http://192.168.0.227:8888/V1/warning/manageconf']


class TestCreateTask:

    def test_user_record(self, driver_setup, log):
        with allure.step("绕过登录页面"):
            login = BasePage(driver_setup)
            login.checker(driver_setup, log)

        for url in url_list:
            time.sleep(3)
            driver_setup.get(url)
           # time.sleep(1)
            print(f"已经打开第{url_list.index(url) + 1}个url")
            print(driver_setup.current_url)


if __name__ == "__main__":
    pytest.main(['-s', f'{__file__}'])