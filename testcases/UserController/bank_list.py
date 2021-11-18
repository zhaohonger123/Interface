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

# 调用鉴权接口获取配置文件中test_account1的token
token = get_token("test_account1")
# 实例化操作Excel
excel = OperateExcel("bank_list")
# 将token写入Excel的header
excel.write_header(token)


@ddt
class BankList(unittest.TestCase):
    # 获取测试用例数据
    cases = excel.read_excel()

    def setUp(self):
        log.info("................开始执行用例................")

    @data(*cases)
    def test_bank_list(self, case):
        """
        获取用户银行卡列表
        """
        log.info("当前执行用例：{}, 请求url:{}".format(case["标题"], case["URL"]))
        # 实例化RequestType并执行用例
        test_response = RequestType().get_request(case["请求方式"], case["URL"], json.loads(case["header"]))
        # 将返回值由str转化为字典型
        test_res = json.loads(test_response)
        test_assert = test_res["msg"]
        if "code" in test_response:
            try:
                self.assertEqual(case["预期返回"], test_assert)
            except AssertionError as e:
                # 将实际返回值写入测试用例文件，并将测试结果置为failed
                excel.write_excel(case["id"] + 1, test_response, "failed")
                log.error(e)
                raise
            else:
                # 将实际返回值写入测试用例文件，并将测试结果置为pass
                excel.write_excel(case["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(case["预期返回"], test_assert))
        else:
            log.error("请求失败 {}".format(test_response))

    def tearDown(self):
        pass
