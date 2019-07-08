from collections.abc import Iterator,Iterable

def test01():
    l = [x*x for x in range(5)] # 中括号表示列表生成器
    g = (x*x for x in range(5)) # 小括号就是生成器
    print(l)
    print(type(l)) # 注意类型
    print(g)
    print(type(g))# 注意类型

def test02():
    g = (x * x for x in range(5))  # 小括号就是生成器
    for i in g:
        print(i)
# yield 注意这个关键字
# 生成器案例
# yield 负责返回
def test03():
    yield 'star'
    g = [x*x for x in range(5)]  # 小括号就是生成器
    yield 'in for '
    for i in g:
        print('数字输出：{0}'.format(i))
    yield 'end for'
# 斐波那契额数列生成器写法
def test04(max):
    n,a,b = 0,0,1 # 注意写法
    while n < max:
        yield  b
        a,b = b, a+b #注意写法
        n +=1
    yield 'end'

if __name__ == '__main__':
    # 注意下面生成器的调用方法
    # next 调用
    '''
    g = test03()
    one = next(g)
    print(one)
    two = next(g)
    print(two)
    # for循环调用
    for funStr in test03():
        print(funStr)
    '''
    '''
     生成器最典型的写法是for里面使用
     典型的生成器，range()
    '''
    x = test04(5)
    for t in x:
        print(t)