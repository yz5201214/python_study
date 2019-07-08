# 函数式编程

# lambda表达式
# 以lambda开头
# 紧跟参数（如果有）
# 参数后用冒号和表达式主体分隔开
# 只是一个表达式，所以没有返回，renturn
# 与函数的调用一样
# 匿名函数 lamdba表示的使用
test01 = lambda x:x*100
test02 = lambda x, y, z: (x * y * z) + 100


# 高阶函数案例
def test03(x, y, z):
    return x * y * z
# fun4 是一个函数，这里只是简单的案例
# 实际的项目中，应该是一个简单的复用函数，有点类似java的工具类，但是工具类实际上可以作为模块，所以这里只能说是一个高阶用法
# 优化了写法，fun4可以直接是函数名称或者函数变量
def test04(fun4,num):
    print(fun4(num,num,num) * 100)
# 案例2 系统函数map
def Testx(n):
    return n * 10
def test05(fun4,listA):
    return map(fun4,listA)


# 案例3 系统函数与reduce
from functools import reduce
def testy(n1,n2):
    return n1 + n2
def test06(ls):
    # 将ls中的值进行累加
    return reduce(testy,ls)

if __name__ == '__main__':
    # 将函数作为值给变量赋值
    funA = test03
    print(funA(1,2,3))
    # 用变量或者函数名都可以
    test04(funA, 2)
    test04(test03,2)
    print("*"*100)
    la = [x for x in range(10)]
    # lb是一个map
    lb = test05(Testx, la)
    # 这里如果操作过一次，map的值，取出来就等于remove，所以后面就输出了一个空集合
    for x in lb:
        pass
    lc = [i for i in lb]
    print(lc)
    print("*"*100)
    lt = [1,2,3,5]
    print(test06(lt))