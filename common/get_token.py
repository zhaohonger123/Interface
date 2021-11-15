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
from common.operate_config import get_config
from common.operate_log import log
import json


def get_token(test_account):
    """
    通过调用获取认证接口拿到token值
    :param test_account: 测试账号
    :return: 测试账号的token值
    """
    # 获取接口地址
    test_url = get_config("api", "host") + get_config("api", "url")
    # 获取测试账号
    account = get_config("data", test_account)
    test_params = '{"account":"%s"}' % account
    log.info("获取账号{}的token".format(account))
    # 将test_params转化成字典型
    test_data = json.loads(test_params)
    # 调用request请求
    test_http = requests.get(url=test_url, params=test_data).text
    # 将返回值由str转化为字典型
    test_res = json.loads(test_http)
    # 判断接口是否成功并返回token值
    if "code" in test_http and test_res["msg"] == "success":
        return test_res["data"]
    else:
        log.error("请求失败{}".format(test_http))
