from collections.abc import Iterable,Iterator
# 是否是迭代对象

# 是否是迭代器
# l 可迭代对象
def test01():
    l = [i for i in range(10)]
    for idx in l:
        print(idx)
# range(5) 是个迭代器
def test02():
    for idx in range(5):
        print(idx)
# 判断对象是否是迭代对象，还是迭代器
def test03():
    l = [i for i in range(10)]
    print(isinstance(l,Iterable))
    print(isinstance(l, Iterator))
# 通过iter进行迭代对象和迭代器转换
def test04():
    s1 = 'i am you baba'
    print(isinstance(s1, Iterable))
    print(isinstance(s1, Iterator))
    s2 = iter(s1)
    print(isinstance(s2, Iterable))
    print(isinstance(s2, Iterator))
    s3 = iter(s2)
    print(isinstance(s3, Iterable))
    print(isinstance(s3, Iterator))
if __name__ == '__main__':
    # test03()
    test04()