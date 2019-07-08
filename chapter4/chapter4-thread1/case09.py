import threading,time

def func():
    print('方法开始-------')
    time.sleep(4)
    print('方法结束-------')


if __name__ == '__main__':
    t1 = threading.Timer(6,func)
    t1.start()
    i = 0
    while True:
        print('{0}******************'.format(i))
        time.sleep(3)
        i +=1