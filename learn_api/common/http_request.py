# coding:utf-8
# Author:liuyan
# time:2019/3/11 21:37
# file:http_request.py
import requests

class HttpRequest:
    '''http请求类，完成get post请求
        method 请求的方法get  post
        url：请求的接口路径
        param：需要传递的接口数据
    '''
    def http_request(self,method,url,param,COOKIES=None):
        if method.upper() == 'GET':
            resp = requests.get(url,params=param,cookies=COOKIES)
        elif method.upper() == 'POST':
            resp = requests.post(url,data=param,cookies=COOKIES)
        else:
            print('不支持此种类型的请求！')
            resp = None
        return resp
# 测试代码
if __name__ == '__main__':
    pass
