# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     operate_log
   Description :    操作日志
   Author :       xiaoyu
   date：          2021/11/9
-------------------------------------------------
"""
from logging import handlers
import logging
import os
import colorlog

# 定义不同级别日志颜色
log_colors_config = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "exception": "red"
}

# 日志保存路径
file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")


class OperateLog:
    def __init__(self, name):
        # 日志文件名字
        self.logname = os.path.join(file_path, "{}.log".format(name))
        # 定义一个log收集器
        self.logger = logging.getLogger()
        # 给收集器定义一个级别debug
        self.logger.setLevel("DEBUG")
        # 设置日志输出格式
        fmt = '%(log_color)s[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] : %(message)s'
        # 日志按不同级别不同颜色输出到控制台
        self.format = colorlog.ColoredFormatter(fmt=fmt, log_colors=log_colors_config)
        # 日志输出到文件无需颜色，使用格式去掉%(log_color)s
        self.ft = logging.Formatter('[%(asctime)s][%(filename)s:%(lineno)d][%(levelname)s] : %(message)s')

        # 定义一个FileHandle将日志输出到磁盘文件,文件接近或超过maxBytes，则依次创建Interface.log,Interface1.log
        self.fh = handlers.RotatingFileHandler(filename=self.logname,mode='w+', maxBytes=1024 * 100, backupCount=5, encoding="utf-8")
        # 设置文件日志的最小级别
        self.fh.setLevel("INFO")
        # 设置文件日志输出格式
        self.fh.setFormatter(self.ft)
        self.logger.addHandler(self.fh)

        # 定义一个StreamHandler将日志输出到控制台
        self.sh = logging.StreamHandler()
        # 设置控制台日志的最小级别
        self.sh.setLevel("INFO")
        # 设置控制台日志输出格式
        self.sh.setFormatter(self.format)
        self.logger.addHandler(self.sh)

    def console(self, level, message):
        """
        避免每次输出日志后都需要移除重复日志及关闭文件，所以根据日志级别调用对应日志
        :param level:
        :param message:
        :return:
        """
        if level == "debug":
            self.logger.debug(message)

        elif level == "info":
            self.logger.info(message)

        elif level == "warning":
            self.logger.warning(message)

        elif level == "error":
            self.logger.error(message)

        elif level == "exception":
            self.logger.exception(message)

        # 避免日志重复
        self.logger.removeHandler(self.fh)
        self.logger.removeHandler(self.sh)
        # 关闭文件
        self.fh.close()

    def debug(self, message):
        self.console("debug", message)

    def info(self, message):
        self.console("info", message)

    def warning(self, message):
        self.console("warning", message)

    def error(self, message):
        self.console("error", message)

    def exception(self, message):
        self.console("exception", message)


# 直接对OperateLog实例化，后续可直接调用log，无需再次实例化
log = OperateLog("Interface").logger
