# 死锁问题
import threading,time

lock_1 = threading.Lock()
locak_2 = threading.Lock()

def fun_1():
    print('fun_1')
    # 申请锁
    print('fun_1开始锁1')
    lock_1.acquire(timeout=4) # timeout=4秒 超时时间,如果超过4秒，则不锁了
    time.sleep(2)
    print('fun_1开始锁2')
    locak_2.acquire()
    # 释放锁
    locak_2.release()
    lock_1.release()
    print('fun_1_end')

def fun_2():
    print('fun_2')
    # 申请锁
    print('fun_2开始锁2')
    locak_2.acquire()
    time.sleep(4)
    print('fun_2开始锁1')
    lock_1.acquire()
    # 释放锁
    lock_1.release()
    locak_2.release()
    print('fun_2_end')

if __name__ == '__main__':
    # 由于fun_1已经锁了1，所以fun_2锁1的时候死锁了。
    # fun_2锁的2.所以fun_1锁2的时候卡死
    t1 = threading.Thread(target=fun_1,args=())
    t2 = threading.Thread(target=fun_2, args=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()







