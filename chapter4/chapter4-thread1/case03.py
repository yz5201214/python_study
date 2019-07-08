import time,threading

# 类需要继承自threading.Thread
class MyThread(threading.Thread):
    # 初始化自己
    def __init__(self,arg):
        super(MyThread,self).__init__()
        self.arg = arg
    def run(self):
        time.sleep(2)
        print('MyThread args is {0}'.format(self.arg))
for i in range(5):
    t = MyThread(i)
    t.start()
    t.join()
print('全部结束')
