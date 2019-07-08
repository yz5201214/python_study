'''
利用time函数，生成两个函数
顺序调用
计算总的运行时间
'''
import time, _thread,threading
def test01():
    print("start test01",time.ctime())
    time.sleep(4)
    print("end test01", time.ctime())
def test02(var1,var2):
    print("start test02",time.ctime(),var1,var2)
    time.sleep(2)
    print("end test02", time.ctime())
# 不用线程写法
def test03():
    print("开始", time.ctime())
    test01()
    test02()
    print("结束", time.ctime())
# 多线程写法
def test04():
    # 启动多个线程，指定线程执行指定任务
    # 启动线程函数：start_new_thread，参数两个，第一个运行的函数名称，第二个是函数的参数作为元祖使用，为空则使用空元祖
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    print("开始", time.ctime())
    _thread.start_new_thread(test01,())
    _thread.start_new_thread(test02,('参数1','参数2',))# 参数的传递注意，参数作为元祖，元祖的定义('参数1',)注意一个参数的时候，逗号结束，这里也可以传入数据库连接或者其他的连接
    print("结束", time.ctime())
    # 看不到打印结果集，是因为主线程已经结束


if __name__ == '__main__':
    # 下面是常规写法
    # test03()
    # 多线程写法，这里用的是老的方法
    # 为了等待线程执行完成
    test04()
    time.sleep(10)


