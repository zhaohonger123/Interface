# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :       xiaoyu
   date：          2021/11/10
-------------------------------------------------
"""
from BeautifulReport import BeautifulReport
import os
import unittest


# 测试用例路径
case_path = os.path.join(os.path.dirname(os.path.abspath(".")), "testcases")
# 测试报告路径
report_path = os.path.join(os.path.dirname(os.path.abspath(".")),"reports")
# 测试套件实例化
test_suite = unittest.TestSuite()
# 实例化收集器defaultTestLoader并用其discover方法收集测试用例
test_discover = unittest.defaultTestLoader.discover(case_path, pattern="*.py")
# 将收集到的用例放到测试套件中
test_suite.addTests(test_discover)
# print(test_suite)

if __name__ == "__main__":
    result = BeautifulReport(test_suite)
    result.report(filename="Test Report", description="接口测试报告", report_dir=report_path)
