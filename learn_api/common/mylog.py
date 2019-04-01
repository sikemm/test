# coding:utf-8
# Author:liuyan
# time:2019/3/12 21:00
# file:mylog.py
import logging
from learn_api.common import project_path
from learn_api.common.config import ConfigCommon
class MyLog:
    '''定义一个日志类'''
    def __init__(self):
        self.cf = ConfigCommon()
        #从配置文件得到日志的显示格式
        self.formatter = logging.Formatter(self.cf.getstr('MyLog','formater'))

    def wlog(self,status,msg):
        # ====定义一个日志收集类====
        self.my_logging = logging.getLogger(self.cf.getstr('MyLog','loggername'))
        # 定义日志收集类的日志收集级别
        self.my_logging.setLevel(self.cf.getstr('MyLog','loglevel'))
        #日志输出到文件
        fh = logging.FileHandler(project_path.log_path,encoding='utf-8')
        #写入文件的日志收集级别
        fh.setLevel(self.cf.getstr('MyLog','floglevel'))
        #设置日志的格式
        fh.setFormatter(self.formatter)

        # 对接最终输出的信息是取两者的交集（my_logging和fh)
        self.my_logging.addHandler(fh)

        if status == 'DEBUG':
            self.my_logging.debug(msg)
        elif status == 'INFO':
            self.my_logging.info(msg)
        elif status == 'WARNING':
            self.my_logging.warning(msg)
        elif status == 'ERROR':
            self.my_logging.error(msg)
        else:
            self.my_logging.critical(msg)

        self.my_logging.removeHandler(fh)  # fh ch

    def info(self,msg):
        self.wlog('INFO',msg)

    def error(self,msg):
        self.wlog('ERROR',msg)

    def debug(self,msg):
        self.wlog('DEBUG',msg)
