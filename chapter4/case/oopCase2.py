# 案例2
class test():
    name = None
    age = None

    def say(self):
        self.name = "ta"
        self.age = 20
# 类实例 ,特别注意ID，实际指向是同一个对象
#案例说明：类实例的属性和其对象的实例属性，在不对对象重新赋值的前提条件下，指向的是同一个变量，C语言的说法：指向同一片内存，Java：同一个变量
# 如果实话之后，重新赋值，python才会生成另外一个新的对象，指向不同的内存区域
print(test.name)
print(test.age)
print(id(test.name))
print(id(test.age))
print("*"*20)
testA = test()
print(testA.name)
print(testA.age)
print(id(testA.name))
print(id(testA.age))

testB = test()
testB.age = 22
print(testB.age)
print(id(testB.age))


class testC():
    name = 'weiwei'
    age = 30

    def say(self):
        self.name = 'zhansan'
        self.age = 22
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))

    def sayT(s):
        s.name = 'lisi'
        s.age = 23
        print("my name is {0}".format(s.name))
        print("my age is {0}".format(s.age))
# 注意这里，调用类成员方法的时候，并没有传入参数，那么python默认会使用自身self作为参数，self在python并不是关键字，可以自行替换
caseA = testC()
caseA.say()
caseA.sayT()


# self有表示非绑定类，如果没有，则是绑定类，只能通过类属性来修改
class teacher():
    name = 'abc'
    age = 40
    def say(self):
        self.name = 'aa'
        self.age = 22
        print("my name is {0}".format(self.name))
        print("my age is {0}".format(self.age))
    def sayAgain():
        print("className ===",__class__.name)
        print("hello")

teacherA = teacher()
teacherA.say()
# 这样调用会异常
# teacherA.sayAgain()
teacher.sayAgain()

# python 构造函数写法
class testD():
    name = 'wangwu'
    age = 33
    def __init__(self):
        self.name = 'aaa'
        self.age = 100

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = 'bbbb'
    age = 90

testE = testD()
# 不传值，默认使用构造函数值
testE.say()
# 这样写会异常
# testD.say()
# 需要传值，因为没有默认值
testD.say(testE)
# 注意这里
testD.say(B)
# 以上代码，利用类鸭子模式，java不存在，python特有写法
# 鸭子类型：只要属性相同即可，比方：水里游的，有脚蹼，带毛，扁嘴，就认为是鸭子，不管是什么。都认为是鸭子