# coding:utf-8
# Author:liuyan
# time:2019/3/11 22:34
# file:project_path.py
'''此文件是配置项目中所需的路径的'''
import os
project_path1 = os.path.realpath(__file__) #获取当前文件的路径
#====excel表格的地址=====
excel_path2 = os.path.split(os.path.split(project_path1)[0])[0]
excel_path = os.path.join(excel_path2,'test_data','api_case.xlsx')

#====配置文件的地址====
conf_path1 = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
conf_path = os.path.join(conf_path1,'conf','config.conf')
# print(conf_path1)
# print(conf_path)

#====生成的日志文件的地址====
log_path = os.path.join(excel_path2,'test_result','my_log.conf')

#====测试报告的生成地址
report_path = os.path.join(excel_path2,'test_result','test_result.html')