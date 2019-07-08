
# zip的用法,两个list集合，合并成一个tuple的集合
# 压缩的长度，决定于最短的集合
def test01():
    l1 = [x for x in range(1,7)]
    l2 = [i for i in range(100) if i %11 ==0 and i !=0]
    print(l1)
    print(l2)
    z = zip(l1,l2)
    print([y for y in z])
# enumerate用法
def test02():
    l1 = [x for x in range(1, 7)]
    # 这个与zip基本一致，只是索引是自行处理，下标0开始，自增长处理索引
    z = enumerate(l1)
    # 这个与zip基本一致，只是索引是自行处理，下标自定义开始坐标，索引只能是数字
    z1 = enumerate(l1,start=10)
    print([x for x in z])
    print([x for x in z1])

from collections import namedtuple,deque,defaultdict,Counter
# namedtuple,deque
# 不是很常用，了解
def test03():
    Point = namedtuple("xyz",['x','y'])
    n1 = Point("11","22")
    print(n1.x)
    print(n1[0])
    print(type(n1))
    #检测变量是不是tuple的子类
    print(isinstance(n1,tuple))
# deque 有点类似list的扩展函数，一般不会用到
def test04():
    q = deque([i for i in range(1,11)])
    print(q)
    # 默认尾巴追加，
    q.append(15)
    # 可以插入前面
    q.appendleft(100)
    print(q)

def test05():
    d1 = {"one":1,"two":2,"three":3}
    # 如果取的字典值没有的情况下，会直接异常
    print(d1["one"])
    # defaultdict
    # lambda表达式，直接返回字符串
    fun_d2 = lambda :"员外"
    d2 = defaultdict(fun_d2)
    d2["one"] = 1
    d2["two"] = 2
    d2["three"] = 3
    # 不会异常，会直接调用函数，但是我直接异常捕获也可以实现。扩展函数，平常不用
    print(d2["xx"])

# 统计字符
def test06():
    # 统计每个字符出现的次数，返回一个可迭代对象
    abc = "asdasdfasdfasdfasfdasdfasdfasdfasdfadfvvvvvv"
    print(Counter(abc))
    c = Counter(abc)
    # 注意下列取值写法
    for x in c:
        print(x)
        print(c.get(x))
# 也可以统计数组
def test07():
    s = ["wo","cao","ni","ma","ma","cao","cao","cao","cao"]
    print(Counter(s))

def test08(name):
    print("输入的内容是:{0}".format(name))
    print("hello ,{0}".format(name))

def test09():
    inputName = input("请输入你的姓名:")
    test08(inputName)

if __name__ == '__main__':
    test09()
