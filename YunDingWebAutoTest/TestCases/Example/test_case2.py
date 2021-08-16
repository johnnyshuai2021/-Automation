"""
AUTHOR: Seamus
DATE: 2020/08/06 Thu
DESCRIPTION:
"""

import pytest
import allure

from Utils.fault_tolerant import fault_tolerant


class TestCase2:

    @pytest.mark.example
    @fault_tolerant
    def test_case2_1(self, driver_setup, log):
        log.info('[TestCase2_1]: start...')
        with allure.step("step1"):
            a = 1
            log.info('[TestCase2_1]: Step 1 finished.')

        with allure.step("step2"):
            b = 2
            log.info('[TestCase2_1]: Step 2 finished.')

        with allure.step("断言"):
            assert a < b

    @pytest.mark.example
    @fault_tolerant
    def test_case2_2(self, driver_setup, log):
        log.info('[TestCase2_2]: start...')
        with allure.step("step1"):
            str1 = 'ok'
            log.info('[TestCase2_2]: Step 1 finished.')

        with allure.step("step2"):
            str2 = 'ok'
            log.info('[TestCase2_2]: Step 2 finished.')

        with allure.step("断言"):
            assert str1 != str2


if __name__ == "__main__":
    pytest.main(['-v', f'{__file__}'])
