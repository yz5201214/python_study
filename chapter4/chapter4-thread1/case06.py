import threading,time,queue

# python2 中 需要from Queue import Queue

testQueue = queue.Queue()
class Producer(threading.Thread):
    def run(self):
        count = 0
        while True:
            if testQueue.qsize() < 500:
                for i in range(100):
                    count += 1
                    msg = '产品编号：'+str(count)
                    testQueue.put(msg)
                    print(msg)
                time.sleep(0.5)

class Consumer(threading.Thread):
    def run(self):
        while True:
            if testQueue.qsize()>100:
                for i in range(3):
                    msg = self.name + '消费了' + testQueue.get()
                    print(msg)
            time.sleep(1)

if __name__ == '__main__':
    for i in range(500):
        testQueue.put('初始化产品{0}'.format(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
