# coding:utf-8
# Author:liuyan
# time:2019/3/9 17:31
# file:run.py
import HTMLTestRunnerNew
import unittest
from learn_api.test_data import test_case,test_recharge
from learn_api.common import project_path

suite = unittest.TestSuite()
loder = unittest.TestLoader()
suite.addTest(loder.loadTestsFromModule(test_case))  #将注册登陆的测试用例加到测试套件里
suite.addTest(loder.loadTestsFromModule(test_recharge)) #将充值的测试用例加到测试套件里
with open(project_path.report_path,'wb') as file:
    # runner = unittest.TextTestRunner(stream=file,verbosity=2)
    # stream = sys.stdout,标准输入输出流，所以用wb，wb模式不需要指定编码
    runner= HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                             verbosity=2,
                                             title='20190312报告',
                                             description='2019年第一份报告',
                                             tester='sikemm')
    runner.run(suite)
# from learn_api.common import do_excel, http_request,project_path
#
# #1. 读取测试数据
# test_data = do_excel.DoExcel(project_path.excel_path, 'register').read_data()
# # 2.执行测试数据
# for case in test_data:
#     url = case['url']
#     method = case['Method']
#     param = eval(case['Params'])  #转换成字典格式
#     resp = http_request.HttpRequest().http_request(method, url, param)
#     print(resp.text)
#     if resp.json() == eval(case['ExpectedResult']):
#         testresult = 'pass'
#     else:
#         testresult = 'failed'
#     # 3.写回测试结果
#     do_excel.DoExcel(project_path.excel_path, 'register').write_data(case['CaseId'] + 1, resp.text, testresult)
#




