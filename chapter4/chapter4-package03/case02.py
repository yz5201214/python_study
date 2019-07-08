# time 模块简介
'''
    年   tm_year 2019
    月   tm_mon  1-12
    日   tm_mday 1-31
    时   tm_hour 0-23
    分   tm_min  0-59
    秒   tm_sec  0-61 60闰秒，61保留值
    周几  tm_wday 0-6
    第几天 tm_yday 1-266
    夏令时 tm_isdst    0，1，-1 表示夏令时
'''

import time

# timezone 当前失去和UTC时间相差的秒数，没有夏令时的情况下的时间间隔
# altzone 相差秒数，但是在有夏令时的情况下
# daylight 是否是夏令时，0是，1非
# 东八区 -28800
def test01():
    print(time.timezone)
    print(time.altzone)
    # 是否是夏令时
    print(time.daylight)

def test02():
    try:
        # 时间戳
        print(time.time())
        # 获取时间格式，与注释一样
        # 可以根据需要获取指定时间
        t = time.localtime()
        print(t)
        # asctime() 返回元祖的正常字符串化之后的时间格式
        print(time.asctime())
        # ctime：获取字符串化后的时间,与上面一致
        print(time.ctime())
        # mktime():使用时间元祖获取对应的时间戳
        # 返回浮点数时间戳
        print(time.mktime(t))
        # clock：获取CPU时间 3.0-3.3版本能用，3.6，3.7调用有问题
        # DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
        print(time.process_time())
        # sleep：使程序进入睡眠，N秒后继续
        print("*"*100)
        for i in range(10):
            time.sleep(1)
            print(i)
    except Exception as e:
        print(e)
# 时间格式化
def test03():
    t = time.localtime()
    ct = time.strftime("%Y{0}%m{1}%d{2}  %H{3}%M{4}%S{5}",t).format("年","月","日","时","分","秒")
    print(ct)
import datetime
def test04():
    dt = datetime.date(2018,5,5)
    print(dt)
    print(dt.year)
    dt = datetime.time(11,11,11)
    print(dt)
    print(datetime .datetime(2018,5,5,11,11,11))
    print(datetime.timedelta())

if __name__ == '__main__':
    test04()