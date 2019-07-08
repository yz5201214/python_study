# python类常用的魔术方法
class A():
    def __init__(self,name = 0):
        print("A的初始化被调用了")
# 自动调用，实例化的同时，调用类的构造函数
# __init__
a = A()
print("*"*100)
#__call__

class B():
    def __init__(self):
        print("B的初始化开始调用")
    def __call__(self, *args, **kwargs):# *args, **kwargs 不明白
        print("B的call被调用")
b = B()
# 下列这样使用类，就必须要要有call函数，否则异常
b()
print("*"*100)
# __str__ 类强转String的时候调用
class C():
    def __init__(self):
        print("C的初始化开始调用")
    def __call__(self, *args, **kwargs):# *args, **kwargs 不明白
        print("C的call被调用")
    def __str__(self):
        return "C被强转成String了"
c = C()
c()
# 这里获取的内容是__str__返回的字符串
print(c)
print("*"*100)
# getattr
class D():
    def __getattr__(self, item):
        # 这里需要返回，如果不返回，会输出None
        return "{0} 在D里面找不到啊，找不到".format(item)
d = D()
print(d.attr)

print("*"*100)
# __setattr__
class E():
    def __setattr__(self, key, value):
        print("对属性：{0} 设置成：{1}".format(key,value))
        # 这里不能写下列赋值操作，否则死循环
        #self.name = value
        # 此情况，为了避免死循环，规定统一调用父类魔法函数
        super().__setattr__(key,value)
e = E()
# 赋值的时候会调用__setattr__，如果在__setattr__ 再次赋值，会进入死循环
e.age = 18

print("*"*100)

class F():
    def __init__(self,name):
        self._name = name
    def __gt__(self, other):
        print("哈哈，{0}会比{1}大么？".format(self._name,other._name))
        return self._name > other._name

# 字符串的比较，是根据字母的顺序来排序，倒叙判断，b>a
# 中文不知道怎么判断 百度一哈
f1 = F("张三")
f2 = F("李四")
print(f1 > f2)