# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     http_request
   Description :    封装接口不同的请求方式
   Author :       xiaoyu
   date：          2021/11/9
-------------------------------------------------
"""
import requests
from common.operate_config import GetConfig


class RequestType:
    @staticmethod
    def get_request(method, url, headers=None, params=None, files=None):
        """
        根据接口不通请求方式选择调用不通方法
        :param method: 请求方式
        :param url: 接口地址
        :param headers: 请求头
        :param params: 请求参数
        :param files: 带文件形式的参数
        :return: 接口返回值
        """
        # 获取host
        host = GetConfig().get_config("api", "host")
        resp = None
        if method == "get":
            resp = requests.get(url=host + url, headers=headers, params=params)

        elif method == "post":
            resp = requests.post(url=host + url, headers=headers, data=params, files=files)

        elif method == "put":
            resp = requests.put(url=host + url, headers=headers, data=params, files=files)

        elif method == "delete":
            resp = requests.delete(url=host + url, headers=headers, data=params, files=files)

        else:
            print("不支持该请求类型，请查看你的请求方式是否正确！！！")

        # 将resp.text由字符转换为json格式
        return resp.text
