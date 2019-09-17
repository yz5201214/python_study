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
    cur = my.cursor()
    selectSQL = 'select * from pre_common_pluginvar'
    cur.execute(selectSQL)
    df = cur.fetchall()
    print(df)


