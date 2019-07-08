# 关于concurrent的案例
import time,re,os,datetime
from concurrent import futures


# 线程池案例
def return_future(msg):
    time.sleep(3)
    return msg
# map案例
data = ['1','2']
def mapFun(argument):
    print(argument)
    time.sleep(2)
    return 'ok'

if __name__ == '__main__':
    '''
    #创建一个线程池,2个线程来进行工作
    pool = ThreadPoolExecutor(max_workers=2)
    #线程池里面增加2个task
    t1 = pool.submit(return_future,'hello')
    t2 = pool.submit(return_future,'nihao')
    print(t1.done())
    time.sleep(3)
    print(t2.done())
    print(t1.result())
    print(t2.result())
    '''
    # 注意下面的线程池mao的使用
    # map的线程池，不需要submit，默认自动提交
    ex = futures.ThreadPoolExecutor(max_workers=2)
    for i in ex.map(mapFun,data):
        print(i)

