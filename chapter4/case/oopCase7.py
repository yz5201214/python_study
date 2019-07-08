# 属性案例
# 创建Student类，描述学生
# 学生具有Student.name 属性
# 但是name格式并不统一
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)
    def infoTro(self):
            print("my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()

s1 = Student("weiwei", 20)
s2 = Student("ZhangSan", 30)
s1.infoTro()
s2.infoTro()

# property 案例
# 定义一个Person类，具有name，age属性
# 需求，对于任意输入的姓名，我们希望都使用大写方式保存
# 年龄，希望都是整数保存
# x = property(fget, fset, fdel, doc)
class Person():
    '''
    用户property操作案例，注释信息必须写内部，外部没法读取
    '''
    def fget(self):
        # 获取的时候 * 2
        return self._name
    def fset(self,name):
        # 所有输入大写
        self._name = name.upper()
    def fdel(self):
        self._name = "NoneName"


    def aget(self):
        return self._age
    def aset(self,age):
        self._age = int(age)
    def adel(self):
        self._age = 0
    age = property(aget, aset, adel, "对age进行操作")
    name = property(fget, fset, fdel, "对name进行操作")

p1 = Person()
p1.name = "zhansan"
p1.age = 2.111111
print(p1.name)
print(p1.age)

# 类的内置属性案例
# 以字典的方式显示类的成员组成
#print(Person.__dict__)
# 显示类的注释信息
#print(Person.__doc__)
# 类的名称，或者模块名称
print(Person.__name__)
# 类的父类，如果多层父类，以元祖的形式展示
print(Person.__bases__)
