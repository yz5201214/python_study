# 高级函数编程，装饰器
import time
def test01(f):
    def case01(*args,**kwargs):
        print("Time:",time.ctime())
        return f(*args,**kwargs)
    return case01
# 先执行teset01，在执行test02
# 装饰器的第一种写法
@test01
def test02():
    print("测试装饰函数")
# 装饰器手动执行
def test03():
    print("手动执行")

# 偏函数
from functools import partial
def test04(x, base=16):
    # 默认10十进制
    print(int(x))
    # 设置成8进制
    print(int(x,base))

if __name__ == '__main__':
    test02()
    print("*"*100)
    test3 = test01(test03)
    test3()
    print("*" * 100)
    test04("123")
    # 实现了test04()函数的功能，偏函数的用法
    test4 = partial(int,base = 16)
    print(test4("123"))