import multiprocessing,time,os

def info(title):
    print(title)
    # 进程名称
    print('module name :',__name__)
    #父进程ID
    print('parent process Pid:',os.getppid())
    # 进程ID
    print('process Pid:', os.getpid())
def f(name):
    info('function f')
    print('hello',name)

if __name__ == '__main__':
    info('main line')
    p = multiprocessing.Process(target=f,args=('yz',))
    p.start()
    p.join()