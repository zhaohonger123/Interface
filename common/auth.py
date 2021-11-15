# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     auth
   Description :    通过接口绕开鉴权
   Author :       xiaoyu
   date：          2021/11/11
-------------------------------------------------
"""
from common.operate_excel import OperateExcel
from common.http_request import RequestType
from common.operate_log import log
from ddt import ddt,data
import unittest
import json

excel = OperateExcel("auth")


@ddt
class Auth(unittest.TestCase):
    # 获取测试用例
    cases = excel.read_excel()

    @data(*cases)
    def test_auth(self, case):
        # 获取用例标题，用例请求方式，用例URL，用例header，用例入参
        test_tile = case["标题"]
        test_method = case["请求方式"]
        test_url = case["URL"]
        test_header = case["header"]
        test_expected = case["预期返回"]
        # 将param由字符型转化为字典型
        test_param = json.loads(case["param"])
        log.info("..............测试用例开始执行...............")
        log.info("当前执行用例：{}, 请求url:{}".format(test_tile, test_url))
        # 实例化RequestType并执行用例
        test_http = RequestType().get_request(test_method, test_url, test_header, test_param)
        if "code" in test_http:
            # 将返回值由str转化为字典型
            test_res = json.loads(test_http)
            test_assert = test_res["msg"]
            try:
                log.info("当前断言部分：预期:{},实际：{}".format(test_expected, test_assert))
                self.assertEqual(test_expected, test_assert)
                # 将实际返回值写入测试用例文件，并将测试结果置为pass
                excel.write_excel(actually=test_http, result="pass")
            except AssertionError as e:
                log.error(e)
                # 将实际返回值写入测试用例文件，并将测试结果置为failed
                excel.write_excel(actually=test_http, result="failed")
        else:
            log.error("请求失败{}".format(test_http))

# if __name__ == '__main__':
#     unittest.main()
