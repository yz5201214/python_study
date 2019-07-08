import time,threading
sum = 0
loopSum = 1000000

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        sum +=1
def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        sum -= 1
# 如果机器够好，执行循环够快，实际输出的还是0，只有当循环次数超出了机器性能，那么线程执行每次结果不一致
# 因为我电脑100000的时候输出0，多一位的时候才会不一致
# 这里就出现多线程共享变量的问题
def myThread():
    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMinu,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()

# 以下为线程变量上锁写法
lock = threading.Lock()
def lockMyAdd():
    global sum,loopSum
    for i in range(1, loopSum):
        # 上锁，申请锁住，后面的变量锁住
        lock.acquire()
        sum += 1
        # 释放锁
        lock.release()
def lockMyMiun():
    global sum,loopSum
    for i in range(1, loopSum):
        # 上锁，申请锁住，后面的变量锁住
        lock.acquire()
        sum -= 1
        # 释放锁
        lock.release()
# 案例测试是否锁住
def locakMyThread():
    t1 = threading.Thread(target=lockMyAdd,args=())
    t2 = threading.Thread(target=lockMyMiun,args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__ == '__main__':
    #myThread()# 没有锁变量，结果会不一致
    locakMyThread() # 进行变量锁，结果一直为0
    print(sum)