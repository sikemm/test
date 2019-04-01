# coding:utf-8
# Author:liuyan
# time:2019/3/11 22:46
# file:test_case.py

import unittest
from ddt import ddt,data,unpack
from learn_api.common import do_excel,project_path,http_request
from learn_api.common.mylog import MyLog
from learn_api.common.config import ConfigCommon
from learn_api.common.get_data import GetData
from learn_api.common.do_re import DoRe
import traceback

# COOKIES = None
@ddt
class TestCases(unittest.TestCase):
    '''完成充值提现操作'''
    def setUp(self):
        '''用例执行之前执行'''
        MyLog().debug('开始进行用例测试')

    def tearDown(self):
        '''用例执行之后执行'''
        MyLog().debug('用例测试执行完毕')
    #获取表单名
    sheet = 'recharge'
    #从配置文件获取需要执行的用例
    case_id = ConfigCommon().getstr('RechargeCASE','case_id')
    MyLog().debug('sheet：{}'.format(sheet))
    '''读取测试用例'''
    test_data = do_excel.DoExcel(project_path.excel_path,sheet,case_id).read_data()

    @data(*test_data)
    def test_recharge(self,case):
        url = case['url']
        method = case['Method']
        # param = eval(case['Params'])  # 转换成字典格式
        # global COOKIES
        # resp = http_request.HttpRequest().http_request(method, url, param,GetData().COOKIES)
        param = eval(DoRe().do_re(case['Params']))

        resp = http_request.HttpRequest().http_request(method, url, param,COOKIES=getattr(GetData,'COOKIES'))
        if resp.cookies:
            # COOKIES = resp.cookies
            setattr(GetData,'COOKIES',resp.cookies)
        MyLog().debug('正在执行{}模块的第{}条测试用例'.format(case['Module'],case['CaseId']))
        MyLog().debug('测试数据是：{}'.format(case))

        try:
            '''判断实际结果和期望结果是否一致'''
            MyLog().info('请求返回的数据是：{}'.format(resp.json()))
            self.assertEqual(resp.json(),eval(case['ExpectedResult']))
            testResult = 'pass'
            MyLog().info('测试通过{}={}'.format(resp.text,case['ExpectedResult']))
        except AssertionError as e:
            '''将错误结果写入日志'''
            MyLog().error('测试未通过{}'.format(e))
            MyLog().error('Exception InfoMation:{0}'.format(traceback.format_exc()))
            testResult = 'failed'
            raise e   #捕获异常之后，需要抛出异常，这样才能在报告里面显示失败，不然全都是通过的
        finally:
            MyLog().info('==========正在往excel里面写入数据=============')
            do_excel.DoExcel(project_path.excel_path,self.sheet,self.case_id).write_data(case['CaseId'] + 1, resp.text, testResult)
            MyLog().info('==========往excel里面写入数据完毕=============')



