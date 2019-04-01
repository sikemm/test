#__coding__:'utf-8'
#auther:ly
'''正则参数化思路：
1，将Excel中的手机号码，memberid 进行参数化设置，同步在配置文件中或者GetData中增加相关配置或者属性。（注意KEY保持一致）
2，编写正则表达式，匹配查找参数化的KEY，提取出来
3，根据提取出来的KEY，获取配置文件的值或者GetData相关的属性值
4，将获取的配置值或者属性值替换到原来的参数化的地方'''

import re
from learn_api.common.get_data import GetData
from learn_api.common import config

class DoRe:
    def do_re(self,target):
        '''target:需要替换的目标字符串'''
        p = '#(.*?)#'
        while re.search(p,target):
            resp = re.search(p,target)
            key = resp.group(1)
            # value = config.ConfigCommon().getstr('DaTa', key)
            value = getattr(GetData,key)
            target = re.sub(p,value,target,count=1)  #每次替换完
            # 成后赋给一个新字符串target（和target一样）
        return target

if __name__ == '__main__':
    d = DoRe().do_re("{'mobilephone':'#nomal_mobilephone#','pwd':'#nomal_pwd#'}")
    print(d)