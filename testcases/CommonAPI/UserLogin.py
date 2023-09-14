from common.operate_excel import OperateExcel
from common.http_request import RequestType
from common.operate_log import log
import unittest
from ddt import ddt, data
import json

excel = OperateExcel("UserLogin")


@ddt
class UserLogin(unittest.TestCase):
    cases = excel.read_excel()

    def setUp(self):
        log.info("................开始执行用例{}................".format(self.__class__.__name__))

    @data(*cases)
    def test_user_login(self, cases):
        """
        :param cases
        """
        log.info("当前执行用例：{}, 请求url:{}".format(cases["Title"], cases["URL"]))
        # 实例化RequestType并执行用例
        test_response = RequestType().get_request(cases["Request Method"], cases["URL"],
                                                  json.loads(cases["header"]),
                                                  params=eval(cases['params']))
        # 将返回值由str转化为字典型
        test_res = json.loads(test_response)
        test_assert = test_res["resp_msg"]

        try:
            # 正常登录的情况
            if test_res['resp_code'] == 0:
                self.assertEqual("succeed", test_assert)
                # 将实际返回值写入测试用例文件，并将测试结果置为pass
                excel.write_excel(cases["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # 密码错误的情况
            elif 'The password' in test_assert and test_res['resp_code'] == 1:
                self.assertIn('The password is wrong', test_assert, msg='密码错误')
                excel.write_excel(cases["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # 账号错误的情况
            elif 'wrong user' in test_assert and test_res['resp_code'] == 1:
                self.assertEqual('wrong user name or password', test_assert, msg='用户名或密码错误')
                excel.write_excel(cases["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # 账号为空的情况
            elif test_res['resp_code'] == 1 and 'Account' in test_assert:
                self.assertEqual('Account cannot be empty', test_assert, msg='账号不能为空')
                excel.write_excel(cases["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))

            # 密码为空的情况
            elif test_res['resp_code'] == 1 and 'blank' in test_assert:
                self.assertEqual('password can not be blank', test_assert, msg='密码不能为空')
                excel.write_excel(cases["id"] + 1, test_response, "pass")
                log.info("当前断言部分：预期:{},实际：{}".format(cases["expected result"], test_res))
            else:
                log.error("请求失败 {}".format(test_response))
                self.fail()

        except AssertionError as e:
            excel.write_excel(cases["id"] + 1, test_response, "failed")
            raise e

    def tearDown(self) -> None:
        log.info("................执行用例{}结束................".format(self.__class__.__name__))


if __name__ == '__main__':
    unittest.main()
