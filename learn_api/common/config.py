# coding:utf-8
# Author:liuyan
# time:2019/3/12 22:05
# file:config.py
from configparser import ConfigParser
from learn_api.common import project_path
class ConfigCommon:
    '''读取配置文件信息'''
    def __init__(self):
        self.con = ConfigParser()  #实例化

    def get_int(self,section,option):
        '''得到整数值'''
        # ======打开文件=====
        self.con.read(project_path.conf_path,encoding='utf-8')
        #=====读取数据=====
        res = self.con.getint(section,option)
        return res

    def get_float(self,section,option):
        '''得到浮点数值'''
        self.con.read(project_path.conf_path,encoding='utf-8')
        res = self.con.getfloat(section,option)
        return res

    def get_bool(self,section,option):
        '''得到布尔值'''
        self.con.read(project_path.conf_path,encoding='utf-8')
        res = self.con.getboolean(section,option)
        return res

    def getstr(self,section,option):
        '''得到字符串'''
        self.con.read(project_path.conf_path, encoding='utf-8')
        res = self.con.get(section, option)
        return res

    def getdic(self, section, option):
        '''得到元组、列表、字典'''
        self.con.read(project_path.conf_path, encoding='utf-8')
        res = self.con.get(section, option)
        return eval(res)
if __name__ == '__main__':
    print(ConfigCommon().getdic('RowButton','button'))


