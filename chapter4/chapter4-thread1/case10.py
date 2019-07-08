import threading,time


class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)
        if lock1.acquire(1):
            num = num + 1
            print(self.name + ' set num to ' + str(num))
            lock1.acquire()
            lock1.release()
            lock1.release()

num = 0
# lock1 = threading.Lock() 锁
lock1 = threading.RLock() # 可重入锁，可以重复锁
if __name__ == '__main__':
    for i in range(5):
        t = MyThread()
        t.start()

