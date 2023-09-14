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


class GetConfig:
    def __init__(self):
        # 配置文件路径
        self.config_path = os.path.join(os.path.dirname(os.path.abspath("...")), r'testconfig\conf.ini')

    def get_config(self, section, option):
        """
        获取配置文件值,返回string类型
        :param self:
        :param section: 配置文件中[]
        :param option: 配置文件中[]下一级
        :return:
        """
        # 实例化
        test_config = configparser.ConfigParser()
        # 读指定路径config文件
        test_config.read(self.config_path)
        # 得到section中option值，返回string类型
        res = test_config.get(section, option)
        return res

    def get_config_int(self, section, option):
        """
        获取配置文件值，返回int类型
        :param self:
        :param section:
        :param option:
        :return:
        """
        # 实例化
        test_config = configparser.ConfigParser()
        # 读指定路径config文件
        test_config.read(self.config_path)
        # 得到section中option值，返回string类型
        res = test_config.getint(section, option)
        return res

    def get_path(self):
        return self.config_path


if __name__ == '__main__':
    A = GetConfig()
    A.get_config('api', 'host')
