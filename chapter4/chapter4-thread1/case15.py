import multiprocessing,time


def consumer(input_q):
    print('Into consumer:',time.ctime())
    while True:
        # 处理项
        item = input_q.get()
        if item is None:
            break
        print('pull', item, 'out of q') #此处替换为有用的工作
        input_q.task_done() #发出信号通知任务完成
    print('Out of consumer:',time.ctime())

def producer(sequence, output_q):
    print('Into producer:',time.ctime())
    for item in sequence:
        output_q.put(item)
        print('put',item,'into q')
    print('Out of producer:',time.ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    p1 = multiprocessing.Process(target=consumer,args=(q,))
    p1.start()

    p2 = multiprocessing.Process(target=consumer, args=(q,))
    p2.start()
    producer(range(100),q)
    # 如果是多个进程的情况下，可以设置多个哨兵，多个哨兵并不互相影响
    q.put(None)
    q.put(None)
    p1.join()
    p2.join()