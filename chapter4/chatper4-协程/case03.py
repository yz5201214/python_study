#协程
from time import ctime,sleep
import inspect
# 注意send的使用
def test01():
    print('---->star')
    x = yield
    print('--->recived',x)
# 注意调用的地方，next预激，send开始下一步，并且推送参数
def test02(a):
    print('---->star')
    # 这里值得注意，返回a，接收send的b值
    b = yield a
    # 返回a+b 接收send的c
    c = yield a+b
    print('--->recived', a,b,c)

if __name__ == '__main__':
    # 主线程 test01的调用
    '''
    t = test01()
    print('111')
    # 可以使用t.send(None)，效果一样
    next(t) # 预激
    print('2222')
    # sned('参数') 参数会发送给上一步的yield
    t.send('ceshi')
    '''
    # test02的调用
    t = test02(5)
    status = inspect.getgeneratorstate(t)
    print(status)
    a = next(t)
    status = inspect.getgeneratorstate(t)
    print(status)
    print('a='+str(a))
    x = t.send(2)
    print('a+b='+str(x))
    t.send(8)


