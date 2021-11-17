# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     add_bankcard
   Description :
   Author :       xiaoyu
   date：          2021/11/16
-------------------------------------------------
"""
from common.get_token import get_token
from common.http_request import RequestType
from common.operate_excel import OperateExcel
from common.operate_log import log
from ddt import ddt, data
import unittest
import json

# 调用鉴权接口获取token
token = get_token("test_account2")
# 实例化操作Excel
excel = OperateExcel("add_bankcard")
# 将token写入Excel的header
excel.write_header(token)
log.info("向Excel中写入header")


@ddt
class AddBankCard(unittest.TestCase):
    # 读取add_bankcard获取测试数据
    cases = excel.read_excel()

    def setUp(self):
        log.info("................开始加载用例................")

    @data(*cases)
    def test_add_bankcard(self, case):
        """
        新增银行卡
        """
        log.info("当前执行用例：{}".format(case["标题"]))
        test_response = RequestType().get_request(case["请求方式"], case["URL"], json.loads(case["header"]),
                                                  json.loads(case["param"]))
        # print(test_response)
        # 将返回值转化为json格式，并获取msg值
        test_actually = json.loads(test_response)["msg"]
        try:
            # 断言成功则将返回写入Excel并将测试结果置为pass
            self.assertEqual(case["预期返回"], test_actually)
            log.info("当前预期结果：{},实际返回结果:{}".format(case["预期返回"], test_actually))
            excel.write_excel(case["id"] + 1, test_response, "pass")
        except AssertionError as e:
            log.error("断言失败{}".format(e))
            # 断言失败则将返回写入Excel并将测试结果置为failed
            excel.write_excel(case["id"] + 1, test_response, "failed")
            log.error("向Excel写入接口返回结果:{}及测试结果:failed".format(test_response))

    def tearDown(self):
        pass

# if __name__ == "__main__":
#     unittest.main()
