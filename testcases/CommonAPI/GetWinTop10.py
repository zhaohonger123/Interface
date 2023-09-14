from common.operate_excel import OperateExcel
from common.http_request import RequestType
from common.get_token import get_token
from common.operate_log import log
from ddt import ddt, data
import unittest
import json
import ast


@ddt
class GetWinTop10(unittest.TestCase):
    excel = OperateExcel("GetWinTop10")
    cases = excel.read_excel()

    @classmethod
    def setUpClass(cls) -> None:
        log.info("................开始执行用例>>>{}<<<................".format(cls.__name__))

    @data(*cases)
    def test_get_win_top10(self, cases):

        # 更新请求头header内容,加入token
        log.info(">>>>开始组装请求头数据<<<<")
        self.headers = ast.literal_eval(cases['header'])
        self.headers['Authorization'] = 'Bearer {}'.format(get_token('user1'))
        log.info(">>>>请求头数据组装完成<<<<")
        log.info("开始执行用例：{}, 用例条件是>>>{}<<<, 请求params是 >>>:{}<<<"
                 .format(cases["Title"], cases['Condition'], cases["params"]))
        test_response = RequestType().get_request(cases["Request Method"], cases["URL"], headers=self.headers,
                                                  params=ast.literal_eval(cases['params']))
        test_res = json.loads(test_response)
        test_assert = test_res["resp_msg"]
        try:
            # 数据均正常情况请求
            if 'datas' in test_res.keys():
                self.assertEqual("succeed", test_assert)
                # 将实际返回值写入测试用例文件，并将测试结果置为pass
                self.excel.write_excel(cases["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))
            else:
                log.error("请求失败 {}".format(test_response))
                self.fail()

        except AssertionError as e:
            self.excel.write_excel(cases["id"] + 1, test_response, "failed")
            raise e

    @classmethod
    def tearDownClass(cls) -> None:
        log.info("................执行用例>>>{}<<<结束................".format(cls.__name__))


if __name__ == '__main__':
    unittest.TestCase()
