import threading,time

loop = [4,2]

class ThreadFun:
    def __init__(self,name):
        self.name = name

    def loop(self,nloop,nsec):
        '''

        :param nloop:loop函数名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print('开始',nloop,time.ctime())
        time.sleep(nsec)
        print('结束',nloop,time.ctime())
def main():
    print('主函数开始',time.ctime())
    # ThreadFun('loop').loop 跟以下两个式子相等：
    '''
    t = ThreadFun('loop')
    t.loop
    '''
    # 以下t1,t2的定义方式相等
    t = ThreadFun('loop')
    t1 = threading.Thread(target=t.loop,args=('LOOP1',4))
    # 外国佬都喜欢这么写
    t2 = threading.Thread(target=ThreadFun('loop').loop,args=('LOOP2',2))
    '''
    常见错误写法：
        t1 = threading.Thread(target=ThreadFun('loop'),args=('LOOP1',4))
        t2 = threading.Thread(target=ThreadFun('loop'),args=('LOOP1',2))
    '''
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    main()