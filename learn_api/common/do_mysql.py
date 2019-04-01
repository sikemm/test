#__coding__:'utf-8'
#auther:ly
#操作数据库的类
# from mysql import connector
import  pymysql
from learn_api.common.config import ConfigCommon
class DoMysql:

    def do_mysql(self,query,flag):
        '''
        :param query: sql查询语句
        :param flag: 1表示获取一条数据，2 获取所有
        :return: 返回查询到的数据
        '''
        db_config = ConfigCommon().getdic('DB','db_config')
        #建立连接
        cnn = pymysql.connect(**db_config)
        #获取游标
        cursor = cnn.cursor()
        cursor.execute(query)
        if flag ==1:
            res = cursor.fetchone() #得到的是一个元祖
        else:
            res = cursor.fetchall() #得到的是一个列表嵌套元祖
        return res
if __name__ == '__main__':
    # query = 'select MAX(Id),Amount from invest where MemberID =1125548 '
    # d = DoMysql().do_mysql(query,1)
    # print(d[1])
    query = 'select LeaveAmount from member where Id = 1125548'
    leaveamount = DoMysql().do_mysql(query, 1)
    print(str(leaveamount[0]))