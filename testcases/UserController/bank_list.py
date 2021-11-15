# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     bank_list
   Description :
   Author :       xiaoyu
   date：          2021/11/11
-------------------------------------------------
"""
from common.operate_excel import OperateExcel
from common.http_request import RequestType
from common.operate_log import log
import unittest
from ddt import ddt, data
import json
from common.get_token import get_token

#调用鉴权接口获取token
token = get_token("test_account")
# 实例化操作Excel
excel = OperateExcel("bank_list")
# 将token以字典格式写入Excel的header
excel.write_excel("", "", Authorization=token)


@ddt
class BankList(unittest.TestCase):
    # 获取测试用例数据
    cases = excel.read_excel()

    @classmethod
    def setUpClass(cls):
        pass

    @data(*cases)
    def test_bank_list(self, case):
        """
        获取用户银行卡列表
        """
        # 获取用例标题，用例请求方式，用例URL，用例header，用例入参
        test_tile = case["标题"]
        test_method = case["请求方式"]
        test_url = case["URL"]
        test_header = json.loads(case["header"])
        test_expected = case["预期返回"]
        log.info("..............测试用例开始执行...............")
        log.info("当前执行用例：{}, 请求url:{}".format(test_tile, test_url))
        # 实例化RequestType并执行用例
        test_http = RequestType().get_request(test_method, test_url, test_header)
        # 将返回值由str转化为字典型
        test_res = json.loads(test_http)
        test_assert = test_res["msg"]
        if "code" in test_http:
            try:
                log.info("当前断言部分：预期:{},实际：{}".format(test_expected, test_assert))
                self.assertEqual(test_expected, test_assert)
                # 将实际返回值写入测试用例文件，并将测试结果置为pass
                excel.write_excel(test_http, "pass")

            except AssertionError as e:
                log.error(e)
                # 将实际返回值写入测试用例文件，并将测试结果置为failed
                excel.write_excel(test_http, "failed")
        else:
            log.error("请求失败 {}".format(test_http))

    @classmethod
    def tearDownClass(cls):
        pass
