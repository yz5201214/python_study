# 多继承的案例
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish():
    def __init__(self,name):
        self.name = name
    def swim(self):
        print("{0} is swimming".format(self.name))
class Brid():
    def __init__(self,name):
        self.name = name
    def fly(self):
        print("{0} is flying".format(self.name))
class Person():
    def __init__(self,name):
        self.name = name
    def work(self):
        print("{0} is working".format(self.name))
class SuperMan(Person,Brid,Fish):
    def __init__(self,name):
        self.name = name
    pass
class SwimMan(Person,Fish):
    def __init__(self,name):
        self.name = name
    pass
s = SuperMan("超人")
sw = SwimMan("蛙人")
s.fly()
s.swim()
s.work()
print("*"*100)
sw.work()
sw.swim()
print("*"*100)
#菱形继承问题
class A():
    pass
class B(A):
    pass
class C(A):
    pass
class D(B,C):
    pass
