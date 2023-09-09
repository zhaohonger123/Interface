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
report_path = os.path.join(os.path.dirname(os.path.abspath(".")), "reports")
# 测试套件实例化
test_suite = unittest.TestSuite()
test_loader = unittest.TestLoader()
# 收集器TestLoader方法discover收集测试用例
test_discover = test_loader.discover(case_path, pattern="*.py", top_level_dir=None)
# 将空用例排除
for case in test_discover:
    if not case:
        pass
    else:
        test_suite.addTests(case)
# print(test_suite)
# 将收集到的用例放到测试套件中
# test_suite.addTest(test_discover)
# print(test_suite)

if __name__ == "__main__":
    result = BeautifulReport(test_suite)
    result.report(filename="Test Report", description="接口测试报告", report_dir=report_path)
