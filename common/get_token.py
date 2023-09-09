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
    # 通过配置文件获取登录账号信息
    login_account = GetConfig().get_config("data", account)
    user_pwd = GetConfig().get_config("data", 'user_pwd')
    # 请求接口地址
    rq_url = GetConfig().get_config('api', 'host') + GetConfig().get_config('api', 'path')
    rq_headers = {
        "Content-Type": "application/json"
    }
    data = {
        "username": login_account,
        "password": user_pwd
    }
    # 登录请求用户token
    log.info('登录用户{}，获取token'.format(login_account))
    try:
        response = requests.post(rq_url, headers=rq_headers, params=data)
        log.info("请求成功")
        result = json.loads(response.text)
        # 通过逻辑判断执行获取Token操作
        if 'accessToken' in result["datas"]:
            log.info("获取Token数据成功")

            return result["datas"]["accessToken"]
        else:
            log.error("获取Token数据异常")
            raise
    except Exception as e:
        log.error("因为{}执行失败".format(e))


if __name__ == '__main__':
    print(get_token('user1'))
