import threading, time
# 参数最多允许三个线程同时使用
semaphore = threading.Semaphore(3)

def func():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName()+'get semaphore')
        time.sleep(5)
        semaphore.release()
        print(threading.currentThread().getName()+'get semaphore')


if __name__ == '__main__':
    for i in range(8):
        t1 = threading.Thread(target=func)
        t1.start()