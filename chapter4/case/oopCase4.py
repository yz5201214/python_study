# 这里主要讲继承
# 实际上python中，任何类都有一个共同的父类叫Object
# 如果类的定义过程中，没有参数，()可以不写，但是为了便于代码阅读，建议写
class Person():
    name = "NoName"
    age = 0
    _petName = "小名"# 受保护的
    __secret = "秘密" # 私有的秘密
    def sleep(self):
        print("大家都要睡觉")
    def work(self):
        print("make money")

# 继承写在类的括号内
class Teacher(Person):
    class_type = "语文老师"
    # 重名优先使用子类
    _petName = "小张"
    def make_test(self):
        print("老师可以发起考试")
    def work(self):
        self.make_test()
        super().work()
        # 调用父类方法，扩充
        Person().sleep()

teatcherA = Teacher()
teatcherA.name = "张老师"
teatcherA.age = 22
print(teatcherA.name)
print(teatcherA.age)
print(teatcherA._petName)
print(teatcherA.class_type)
# 这里会异常，私有不允许访问
# print(teatcherA.__secret)
#teatcherA.make_test()
teatcherA.work()
print("*"*100)

# 构造函数
class Animel():
    def __init__(self):
        print("Animel")

class Dog(Animel):
    # __init__ 就是构造函数
    # 实例化的同时，第一个被调用，必须有参数
    def __init__(self,name):
        print("{0}--汪汪".format(name))
# 如果是继承关系，优先调用子类，如果子类没有__init__ 则会找父类，父类没有，啥都不干
class HaBaDog(Dog):
    def __init__(self):
        super().__init__("哈巴狗")
        print("哈哈")

class QiutianDog(Dog):
    pass

liDog = HaBaDog()
# 这里会异常，因为构造函数除开本身外，有多的参数
# yangDog = QiutianDog()
yangDog = QiutianDog("秋田犬")
print("*"*100)
# super 是一个类
print(type(super))
help(super)