#第三课
* 线程替代方案
* subprocess
    * 完全跳过线程，使用进程
    * 是python进程的主要替代方案
    * python2.4之后引入
* multiprocessiong
    * 使用的threading接口排成，使用子进程
    * 允许为多核和或者多CPU派生进程，接口跟threading非常相似
    * python2.6引入
* cuoncurrent.futures
    * 新的异步执行模块
    * 任务级别的操作
    * python3.2后引入
# 多进程
* 进程间通讯(InterprocessCommunication,IPC)
* 进程之间无任何共享状态
* 进程的创建
    * 案例case11.py
    * liunx下，如果主进程结束，则子进程不运行，并且会出现异常。windows不会出现前面的问题
* 进程相关操作
    * 在OS中查看PID，PPID以及他们的关系，PID=进程ID，PPID=父进程ID 
    * 案例case12.py 主要是用于查看多进程之间的ID关系，执行顺序关系
* 进程内的生产者消费者模型
    * 在某种程度下，利用生产者消费者模型可以让两个进程产生关系
    * JoinableQueue 案例case13.py
        * 当消费者，消费了对应的生产者的任务时候，会通知生产者
    * 队列中哨兵的使用 案例case14.py
    * 队列中哨兵的改进使用 案例case15.py
        