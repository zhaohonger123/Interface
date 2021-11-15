# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     operate_config
   Description :
   Author :       xiaoyu
   date：          2021/11/13
-------------------------------------------------
"""
import os
import configparser

def get_config(section, option):
    """
    获取配置文件值
    :param section: 配置文件中[]
    :param option: 配置文件中[]下一级
    :return:
    """
    config_path = os.path.join(os.path.dirname(os.path.abspath(".")), "testconfig", "conf")
    # 实例化
    test_config = configparser.ConfigParser()
    # 读指定路径config文件
    test_config.read(config_path)
    res = test_config.get(section, option)
    return res
