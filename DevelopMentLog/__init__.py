import json,re,operator
import pymysql
import pandas as pd
from redis import Redis

if __name__ == '__main__':
    redis_db = Redis(host='dev.kuituoshi.com', port=6379, password='88888888', db=4)
    redis_data_btbbt = 'btbbt_cache'

    my = pymysql.connect(
        host='www.findbt.com',  # 数据库地址
        port=3306,  # 端口 注意是int类型
        db='ultrax',  # 数据库名称
        user='root',  # 用户名
        passwd='cyfU2ypeM9AVeVzh',  # 用户密码
        charset='utf8',  # 字符编码集 ,注意这里，直接写utf8即可
        use_unicode=True)
    selectSQL = 'select * from pre_common_pluginvar'
    common = pd.read_sql(selectSQL, my)  # 影视大全参数配置表
    for commonItem in common.get_values():
        sItem = pd.Series(commonItem)
        if sItem[5] == 'yuyan':
            for xItem in sItem[7].split('\r\n'):
                abc = xItem.split('=')
                redis_db.hset('yuyan', abc[1], abc[0])# 结构：key=国语，value=1

    yuyan = []  # 其他
    for rKye in redis_db.hkeys('yuyan'):
        rValue = redis_db.hget('yuyan', rKye)
        if '英语中字'.find(rKye.decode('utf-8')[0:1]) >= 0:
            yuyan.append(rValue.decode('utf-8'))
    print(','.join(yuyan))


