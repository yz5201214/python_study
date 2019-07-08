import time,threading


def test01():
    print("start test01",time.ctime())
    time.sleep(4)# 看下执行时间
    print("end test01", time.ctime())
def test02(var1,var2):
    print("start test02",time.ctime(),var1,var2)
    time.sleep(2)# 看下执行时间
    print("end test02", time.ctime())

# 常规新的多线程写法
def test03():
    t1 = threading.Thread(target=test01,args=())
    t1.start()
    t2 = threading.Thread(target=test02,args=('1号','2号',))
    t2.start()
    # 如果是用线程的join，那么主线程，需要等待其他线程执行完，才继续往下走如果不是，则直接一路顺序往下
    t1.join()
    t2.join()
    print('到底我是不是最后执行的')
# 守护线程写法
def test04():
    t1 = threading.Thread(target=test01,args=())
    t1.setDaemon(True)#设置成守护线程，主线程结束，本线程也马上结束
    t1.start()
# 线程常规属性写法
def test05():
    t1 = threading.Thread(target=test01,args = ())
    t1.setName('Number1')
    t2 = threading.Thread(target=test02,args=('参数1','参数2',))
    t2.setName('Number2')
    t1.start()
    t2.start()
    for thr in threading.enumerate():# 循环线程List集合
        print('当前正在运行的线程名称：{0}'.format(thr.getName()))#输出线程名称
    print('当前运行的线程总数：{0}'.format(threading.active_count()))#在运行线程数量,这里输出3是因为包含了主线程
    print('你好：{0}'.format(threading.current_thread()))


if __name__ == '__main__':
    # 常规线程，都是非守护线程，独立运行，不论主线程是否结束，其他子线程独立运行
    # test03()
    # 下面是守护线程案例测试
    # 这里的子线程只打印了第一句，其他的随着主线程的结束，同时结束
    '''
    print('主线程开始了')
    test04()
    '''
    # 下面是线程常规属性方法
    test05()
