# coding:utf-8
# Author:liuyan
# time:2019/3/11 22:46
# file:test_case.py
# pip freeze > requirements.txt  输出项目安装的第三方包
# pip install -r requirements.txt   做jenkins之前，执行这个文件，安装第三方库
# Jenkins默认安装目录 是再当前用户的目录
import unittest
from ddt import ddt,data,unpack
from learn_api.common import do_excel,project_path,http_request
from learn_api.common.mylog import MyLog
from learn_api.common.config import ConfigCommon
from learn_api.common.get_data import GetData
from learn_api.common.do_mysql import DoMysql
from learn_api.common.do_re import DoRe


# COOKIES = None
@ddt
class TestCases(unittest.TestCase):
    '''完成投资、竞标操作'''
    def setUp(self):
        '''用例执行之前执行'''
        MyLog().debug('开始进行用例测试')

    def tearDown(self):
        '''用例执行之后执行'''
        MyLog().debug('用例测试执行完毕')
    #获取表单名
    sheet = 'bidloan'
    #从配置文件获取需要执行的用例
    case_id = ConfigCommon().getstr('BidLoanCASE','case_id')
    MyLog().debug('sheet：{}'.format(sheet))
    '''读取测试用例'''
    test_data = do_excel.DoExcel(project_path.excel_path,sheet,case_id).read_data()

    @data(*test_data)
    def test_recharge(self,case):
        url = case['url']
        method = case['Method']
        # param = eval(case['Params'])  # 转换成字典格式
        #----调用方法，通过正则和反射完成参数替换
        param = eval(DoRe().do_re(case['Params']))
        #-----------通过反射完成参数值替换-------------
        # if case['Params'].find('mobilephone') > -1:
        #     nomal_mobilephone = ConfigCommon().getstr('DaTa', 'nomal_mobilephone')
        #     setattr(GetData, 'MOBILEPHONE', nomal_mobilephone)
        #     param = eval(case['Params'].replace('#nomal_mobilephone#',getattr(GetData,'MOBILEPHONE')))
        # elif case['Params'].find('memberId') > -1:
        #     nomal_memberid = ConfigCommon().getstr('DaTa', 'nomal_memberid')
        #     setattr(GetData, 'MEMBERID', nomal_memberid)
        #     param = eval(case['Params'].replace('#nomal_memberid#', getattr(GetData, 'MEMBERID')))
        #---------通过正则表达式完成参数替换--------------
        # if case['Params'].find('mobilephone')>-1:
        #     param = eval(DoRe().do_re(case['Params'],'nomal_mobilephone'))
        # elif case['Params'].find('memberId')>-1:
        #     param = eval(DoRe().do_re(case['Params'], 'nomal_memberid'))
        # global COOKIES
        # resp = http_request.HttpRequest().http_request(method, url, param,GetData().COOKIES)
        resp = http_request.HttpRequest().http_request(method, url, param,COOKIES=getattr(GetData,'COOKIES'))

        if resp.cookies:
            # COOKIES = resp.cookies   setattr：反射，定义了的话，就覆盖默认值，没有定义的话，就创建一个
            setattr(GetData,'COOKIES',resp.cookies)
        MyLog().debug('正在执行{}模块的第{}条测试用例'.format(case['Module'],case['CaseId']))
        MyLog().debug('发送的请求参数数据是：{}'.format(param))
        #投资成功后，进行数据库校验
        query ='select MAX(Id),Amount from invest where MemberID =1125548 '
        money = DoMysql().do_mysql(query,1)  #返回的是一个元祖

        try:
            '''判断实际结果和期望结果是否一致'''
            MyLog().info('请求返回的数据是：{}'.format(resp.json()))
            self.assertEqual(resp.json(),eval(case['ExpectedResult']))
            # 投资成功后，进行数据库校验
            baserusult=''
            if case['CaseId'] == 2:
                try:
                    self.assertEqual(int(money[1]),int(param['amount']))
                    baserusult = '数据库校验通过'
                except AssertionError as e:
                    baserusult = '数据库校验未通过'
                    raise e

            testResult = 'pass'+baserusult
            MyLog().info('测试通过{}={}'.format(resp.text,case['ExpectedResult']))
        except AssertionError as e:
            '''将错误结果写入日志'''
            MyLog().error('测试未通过{}'.format(e))
            testResult = 'failed'+baserusult
            raise e   #捕获异常之后，需要抛出异常，这样才能在报告里面显示失败，不然全都是通过的
        finally:
            MyLog().info('==========正在往excel里面写入数据=============')
            do_excel.DoExcel(project_path.excel_path,self.sheet,self.case_id).write_data(case['CaseId'] + 1, resp.text, testResult)
            MyLog().info('==========往excel里面写入数据完毕=============')



