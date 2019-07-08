# 类和对象的三种方法案例
class Person():
    # 实例方法，实例化之后才能调用
    name = "None"
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("{0}开始吃饭了".format(self.name))
    # 类方法声明
    # 第一个参数：cls ，也可以自行定义，但是惯例默认
    @classmethod
    def pay(cls,name):
        print("{0}开始去玩了".format(name))
    # 静态方法声明
    # 不需要参数
    @staticmethod
    def say(self):
        print("{0}开始说话了".format(self.name))

# 三种方法内存使用的区别 自行百度
p = Person("张三")
# 实例方法可以直接调用
p.eat()
p.pay(p.name)
p.say(p)
# 类方法
Person.pay("李四")
# 静态方法
Person.say(p)