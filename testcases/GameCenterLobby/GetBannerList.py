from common.get_token import get_token
from common.operate_excel import OperateExcel
from common.http_request import RequestType
from common.operate_log import log
import unittest
from ddt import ddt, data
import json

excel = OperateExcel("GetBannerList")


@ddt
class GetBannerList(unittest.TestCase):
    cases = excel.read_excel()
    case_data = cases[0]

    def setUp(self) -> None:
        # 用户登录Token
        self.headers = eval(self.case_data['header'])
        self.headers['Authorization'] = 'Bearer {}'.format(get_token('user1'))

    def test_get_carousel(self):
        log.info("当前执行用例：{}, 请求url:{}".format(self.case_data["Title"], self.case_data["URL"]))
        # 实例化RequestType并执行用例
        test_response = RequestType().get_request(self.case_data["Request Method"], self.case_data["URL"],
                                                  headers=self.headers)

        # 将返回值由str转化为字典型
        test_res = json.loads(test_response)
        test_assert = test_res["resp_msg"]
        if test_assert:
            try:
                self.assertEqual("succeed", test_assert)
                # 将实际返回值写入测试用例文件，并将测试结果置为pass
                excel.write_excel(self.case_data["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(self.case_data["expected result"], test_res))

            except AssertionError as e:
                # 将实际返回值写入测试用例文件，并将测试结果置为failed
                excel.write_excel(self.case_data["id"] + 1, test_response, "failed")
                log.error(e)
                raise
        else:
            log.error("请求失败 {}".format(test_response))

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
