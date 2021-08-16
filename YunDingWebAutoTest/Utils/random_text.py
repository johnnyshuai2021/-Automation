# -*- coding:UTF-8 -*-
'''
AUTHOR: Zhong xinqi
DATE: 2020/08/07 Fri
DESCRIPTION:生成随机字符
'''

from random import Random


def random_string(times):
    string_name = ""
    for i in range(times):
        num = Random().randint(0, 10)
        string_name += str(num)
    return string_name
