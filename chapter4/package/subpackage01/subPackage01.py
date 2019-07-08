# python高级语法，包的使用01
# 模块案例 package02.py 负责模块使用和调用
# 用于包导入调用，copy与package01.py
class Student():
    def __init__(self,name = "NoName",age = 18):
        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))


def SayHello(name):
    print("Hi, my nams is {0}.hello".format(name))

#只有运行文件本体的时候，才会执行。妈的，类似java的Main一样的效果。CTMD这里才将
#if __name__ == '__main__':
print("这里是模块测试01，我是01，我是01")
