# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     get_token
   Description :
   Author :       xiaoyu
   date：          2021/11/13
-------------------------------------------------
"""
import requests
from common.operate_config import GetConfig
from common.operate_log import log
import json


def get_token(account):
    """
    使用配置文件conf中test_account的值，通过调用获取认证接口拿到test_account的token值
    :param account: 测试账号
    :return: 测试账号的token值
    """
    # 获取接口地址
    test_url = GetConfig().get_config("api", "host") + GetConfig().get_config("api", "url")
    # 获取测试账号
    test_params = '{"account":"%s"}' % GetConfig().get_config("data", account)
    log.info("获取账号{}的token".format(account))
    # 将test_params转化成字典型
    test_data = json.loads(test_params)
    # 调用request请求
    test_http = requests.get(url=test_url, params=test_data).text
    # 将返回值由str转化为字典型
    test_res = json.loads(test_http)
    # print(test_res)
    # 判断接口是否成功并返回token值
    if "code" in test_http and test_res["msg"] == "success":
        # 拼接header成字典形式
        header = '{"Authorization": "%s"}' % test_res["data"]
        # print(header)
        return header
    else:
        log.error("请求失败{}".format(test_http))
