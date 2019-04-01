#__coding__:'utf-8'
#auther:ly
from learn_api.common import config
'''此类用来完成反射数据参数定义'''
class GetData:
    COOKIES = None
    nomal_mobilephone = config.ConfigCommon().getstr('DaTa', 'nomal_mobilephone')
    nomal_memberid = config.ConfigCommon().getstr('DaTa', 'nomal_memberid')
    nomal_pwd = config.ConfigCommon().getstr('DaTa', 'nomal_pwd')

