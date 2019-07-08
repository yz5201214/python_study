import time
from datetime import datetime,timedelta
'''
常用类方法：
    today
    now
    utcnow
    fromtimestamp
'''
def test01():
    dt = datetime(2019,4,25)
    print(dt.today())
    print(dt.now())
    print(dt.fromtimestamp(time.time()))

def test02():
    t1 = datetime.now()
    print(t1)
    print(t1.strftime("%Y-%m-%d %H:%M:%S"))
    # t2 = 一个小时后的时间格式
    t2 = timedelta(hours=1)
    print(t2)
    print((t1+t2).strftime("%Y-%m-%d %H:%M:%S"))
# timeit- 时间测量工具
# 常规写法
def test03():
    t1 = time.time()
    time.sleep(3)
    print("*"*100)
    print(time.time()-t1)

# 执行一段代码的时间
import timeit
def test04():
    for i in range(1000):
        pass
def test05():
    c = []
    for i in range(1000):
        c.append(i)
# 带参数的写法
t6 = '''
def test06(num):
    for i in range(num):
        pass
'''
t7 = '''
def test07(num):
    c = []
    for i in range(num):
        c.append(i)
'''
if __name__ == '__main__':
    # 证明谁运行的快
    t1 = timeit.timeit(stmt=test04,number=10000)
    t2 = timeit.timeit(stmt=test05, number=10000)
    print(t1-t2)
    # 带参数运行
    # setup 负责把环境变量准备好，实际详单与给timeit创造了一个小环境，在执行过程中，执行的顺序大概是：
    '''
        def t6(num):
            for i in range(num):
            pass
        num = 1000
        t6(num)
    '''
    tx = timeit.timeit(stmt = "test06(num)",setup=t6+"num=1000",number=10000)
    ty = timeit.timeit(stmt="test07(num)", setup=t7 + "num=1000", number=10000)
    print(tx - ty)