# 高级函数编程02

# 案例 filter 过滤函数
def test01(a):
    return a % 2 == 0
def test02(funA,l):
    # 返回的内容是可迭代对象，一个集合list
    ret = filter(funA, l)
    print([x for x in ret])

# 集合排序案例
def test03(l):
    # 按照升序进行排列
    print(sorted(l))
# 案例，如果l中包含负数，这个时候需要按照绝对值排序
# 绝对值倒叙排列
def test04(l):
    print(sorted(l,key=abs, reverse=True))
# 字符串操作
def test05(l):
    print(sorted(l, key = str.lower))

# 将函数作为结果，在函数中进行函数返回
def test06():
    def test07():
        print("我是一个子函数")
        return 3
    return test07
# 上一个案例，深入处理
# 传入一个集合，返回一个函数，函数执行的结果是将集合所有的值累加
# 参数值会持续存在
def test08(*args):
    def test09():
        rst = 0
        for i in args:
            rst +=i
        return rst
    return test09

# 闭包函数常见坑，经典案例
def test10():
    fs = []
    for i in range(1,5):
        def f():
            return i*i
        fs.append(f)
    return fs
# 解决方案 ，注意结构
def test11():
    def f(i):
        def g():
            return i * i
        return g
    fs = []
    for i in range(1, 5):
        fs.append(f(i))
    return fs

if __name__ == '__main__':
    l = [i for i in range(21)]
    test02(test01,l)
    print("*"*100)
    l = [8,6,5,4,12,43,6,56,73,542,34,6,234,23,543,62,3]
    test03(l)
    print("*" * 100)
    l = [8, 6, 5, 4, -12, -43, 6, 56, 73, -542, 34, -6, 234, 23, -543, 62, 3]
    test04(l)
    print("*" * 100)
    l = ["b","c","ab","Ec","m","n","q","r","fe","D","ev","Ad","F"]
    print(sorted(l))
    test05(l)
    print("*" * 100)
    l6 = test06()# 返回了一个函数
    print(l6())# 因为发案值是一个函数，所以可以直接执行
    print("*" * 100)
    # 注意参数的传承性
    l8 = test08(1,4,5,6,1,23,32)
    l8a = test08(10, 40, 50, 60)
    print(l8())
    print(l8a())
    print("*" * 100)
    # 这里都只输出了最后的值
    f1,f2,f3,f4 = test11()
    print(f1())
    print(f2())
    print(f3())
    print(f4())