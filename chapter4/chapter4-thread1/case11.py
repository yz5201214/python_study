import multiprocessing,time

def clock(var1):
    while True:
        print('the time is %s' % time.ctime())
        time.sleep(var1)

# 进程派生写法
class ClockProcess(multiprocessing.Process):
    '''
    两个必须函数
    1.init构造函数
    2.run运行启动函数
    '''
    def __init__(self,interval):
        # 首先需要初始化父类构造函数
        super().__init__()
        self.interval = interval
    def run(self):
        while True:
            print('the time is %s' % time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    # 常规写法
    '''
    p = multiprocessing.Process(target=clock,args=(5,))
    p.start()
    '''
    # 派生写法
    p = ClockProcess(3)
    p.start()