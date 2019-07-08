# python中的抽象类
# 抽象类主要的用途，就是父类中中定义类动作，但是这个动作是所有子类具有的共性，所以父类没法确定不同的子类执行不同的操作，子类自行定义具体得操作
class Test():
    # 这里就是抽象类
    def sayHello(self):
        pass

class Test2(Test):
    def sayHello(self,):
        print("这里做事情")


t = Test2()
t.sayHello()

print("*"*100)
# 抽象类的声明，定义
import abc
class Human(metaclass=abc.ABCMeta):
    #定义一个抽象类方法
    @abc.abstractmethod
    def smoking(self):
        pass
    # 定义类抽象方法 3.3开始过时，内置了classMethod函数的子类
    @abc.abstractclassmethod
    def drink(cls):
        pass
    # 定义静态抽象类方法 3.3开始过时，staticmethod函数的子类
    @abc.abstractstaticmethod
    def pay():
        pass
print("这个里面是抽象类说明，没做什么事")
print("*"*100)


# 组装案例1
# 自定义类
# 函数名称可以当成变量使用
class A():
    pass
def say(self):
    print("saying.....")
class B():
    def say(self):
        print("saying.....")
#say(9)
# 注意这里的赋值操作
A.say = say
a = A()
a.say()
b = B()
b.say()

# 函数名称可以当成变量使用   案例
def sayHello(name):
    print("{0} 打了一声招呼".format(name))
sayHello("张三")
# 注意这里的写法
testSay = sayHello
testSay("李四")

print("*"*100)
# 组装案例2
from types import MethodType
class C():
    pass
def say2(self):
    print("saying......2")
# 这里的写法特别注意
c = C()
c.say2 = say2
c.say2("1")# 这里是需要给参数的
# 注意下列写法 加上上面的引用，不需要参数
c1 = C()
c1.say2 = MethodType(say2,C)# 这里是将say2 与类C进行类绑定
c1.say2()
# MethodType说明 help(MethodType)

print("*"*100)
# type 的具体说明 help(type)
# 使用type来制造一个类
def work(self):
    print("working.......")
def sleep(self):
    print("sleeping......")
# type("类名称","父类","里面的实现方法")
E = type("AName",(object,),{"class_work":work})

e = E()
e.class_work()
print("*"*100)
# 元类演示
# 元类的写法是固定的，他必须继承自type
# 大家约定俗成元类的命名一般以：metaClass结尾
class TestleiMetaClass(type):
    # 注意写法
    def __new__(cls, name, bases, attrs):
        # 自己的业务处理
        print("卧槽你妈，有啥用嘞")# 老子估计用不到
        attrs['id'] = '0000000000';
        attrs['name'] = '姓名'
        return type.__new__(cls, name ,bases ,attrs)
# 定义完成后的使用 注意写法
class TestYuanLei(object,metaclass=TestleiMetaClass):
    pass
tx = TestYuanLei()
print(tx.id)
print(tx.name)


