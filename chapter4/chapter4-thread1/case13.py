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
    # 进程队列，消费完成会通知生产者
    q = multiprocessing.JoinableQueue()
    #运行消费者进程
    p = multiprocessing.Process(target=consumer,args=(q,))
    # 守护进程，如果主进程结束，子进程同时结束
    p.daemon = True
    p.start()
    # 声场多个项，sequence达标要发送给消费者的序列
    # 实践中，这可能是生成器的输出或者通过一些全天的方式生产出来的
    producer(range(10),q)
    #等待所有的队列消费完，然后
    q.join()