# coding = utf-8
"""
Author: 钟欣琪
Date: 2020-8-04
Remarks: 参数分离
"""

SERVER = 'http://192.168.0.227:8888/login'
login_url1 = 'http://192.168.0.227:8888/webapp/oauth/token'
<<<<<<< Updated upstream
home_url = 'http://192.168.0.227:8888/V3/home'
=======
home_url = 'http://192.168.0.227:8888/V1/home'
>>>>>>> Stashed changes
domain = "192.168.0.227"
# SERVER = 'https://yd.yunding360.com'
# login_url1 = 'https://yd.yunding360.com/webapp/oauth/token'
# home_url = 'https://yd.yunding360.com/home'
# domain = "yd.yunding360.com"
# allure_server = '192.168.0.227:8888'
GLOBAL_PARAMS = [
    {
<<<<<<< Updated upstream
        'account': 'qiqi55555',
        "enterprise": 'qiqi1',
        'password': 'zxq12345..',
        'loginCode': 'qiqi1',
        # 'account': 'admin',
        # 'password': '123456',
        # "enterprise": 'yunding',
=======
        'account': 'admin',
        "enterprise": 'testpw',
        'password': 'P@ssw0rd',
        'loginCode': 'testpw',
        # 'account': 'admin',
        # 'password': '123456',
        # "enterprise": 'yunding',
        'port_password': '+oM2Xe5OHWzenQdM+C+a5w==',
>>>>>>> Stashed changes
        # 'loginCode': 'yunding',
        'port_password': '+bifEY4ulJhI+YAgdzcnTA==',
        'WEB_NAME': 'YunDing360',
        'BROWSER_NAME': 'Chrome 85.',
        'SELENIUM_VERSION': '3.141.0',
        'mail_from': 'xq.zhong@yunding360.com',
        'mail_pwd': 'jb@123',
        'mail_to': ["xq.zhong@yunding360.com"],
        'mail_subject': '云盯web自动化测试报告',
        'smtp_host': 'mail.4ioa.com',
        'web_version': '4.1.3.',
        'persent': '20',
        'home_text': '首页',
        'common_text': '自动化测试',
        'person_name': '七七1',
        "alert": "操作成功",
        "area_name": "自动化测试区域",
        "single_store_name": "自动化测试门店",
        "template_type": ["扣分模式", "评分模式"],
        "template_name": ["自动化测试模板1"],
        "score": "10",
        "start_time": "2020-01-01",
        "end_time": "2020-10-01"
    }
]
