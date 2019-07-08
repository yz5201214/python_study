# yield from
from collections import namedtuple


def test01():
    for c in 'AB':
        yield c

# 注意调用的地方
# yield from 可以作为一个中间库，左边连接的是接收对象list，右边连接的是内容仓库'AB'
def gen_new():
    yield from 'AB'


ResClass = namedtuple('Res','count average')
# 注意yield from的委派生成器
'''
解释：
1. 外层for 循环每次迭代会席间一个grouper实例，赋值给coroutine变量：
'''
# 子生成器
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        # None 是哨兵值
        if term is None:
            break
        total += term
        count +=1
        average = total / count
    return ResClass(count,average)
# 委派生成器
def grouper(storages,key):
    while True:
        storages[key] = yield from averager()

# 客户端代码
def client():
    process_data = {'boys_1':[1,2,32,32,3,23,23,2,1,12,12,4,5,14,24,14],'boys_2':[3,43,4,34,354,4,65,75,75,52,43,234,2,43]}
    storages = {}
    for k , v in process_data.items():
        coroutine = grouper(storages,k)
        next(coroutine)
        for dt in v:
            coroutine.send(dt)
        coroutine.send(None)
    print(storages)

if __name__ == '__main__':
    # list 直接用生成器作为参数
    '''
    print(list(test01()))
    print(list(gen_new()))
    '''
    client()