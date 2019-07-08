# 变量的三种用法
class A():
    def __init__(self):
        self.name = "zhangsan"
        self.age = 18

a = A()
print(a.name)
# 属性的三种用法
# 1 赋值，2 读取，3 删除
a.name = "李四"# 赋值
print(a.name) # 读取
del a.name # 删除
#print(a.name)
print("*"*100)
# 类属性 property
# 应用场景： 对变量除了普通的三种操作，还想增加一些操作，那么可以通过property来完成
class B():
    def __init__(self):
        self.name = "李四"
        self.age = 18
        # 此功能表示，赋值的同时执行该函数的内部操作
    def fset(self,name):
        print("{0}参数被写入成：{1}".format("name",name))
        self.name = name
    def fget(self):
        print("读取了参数{0},值是：{1}".format("name",self.name))
        return self.name
    def fdel(self):
        print("执行了删除")
    # 顺序，get，set，del
    name2 = property(fget,fset,fdel,"这里是备注")

b = B()
b.name2 = "王五"
b.name2
del b.name2
