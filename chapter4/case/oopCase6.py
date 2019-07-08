# Mixin案例
class Person():
    age = 18
    def eat(self,name):
        print("{0} to eat....".format(name))
    def drink(self,name):
        print("{0} to drink....".format(name))
    def sleep(self,name):
        print("{0} to sleep....".format(name))
# 常规类
class Teacher():
    def work(self,name):
        print("{0} to wotk....".format(name))
# 常规类
class Student():
    def study(self,name):
        print("{0} to study....".format(name))
class Tutor(Teacher,Student):
    pass
# Mixin类 Mixin大概写法
class TeacherMixin():
    def work(self,name):
        print("{0} to wotk....".format(name))
class StudentMixin():
    def study(self,name):
        print("{0} to study....".format(name))
class TutorM(Person,TeacherMixin,StudentMixin):
    pass

t = Teacher()
tm = TutorM()
print(Tutor.__mro__)
print(TutorM.__mro__)
# issubclass 函数使用
print(issubclass(Tutor,Person))
print(issubclass(TutorM,Person))
# isinstace 函数使用
print(isinstance(t,Teacher))
print(isinstance(t,Student))
# hasattr 函数使用，可检测变量，也可以检测方法名称
p = Person()
print(hasattr(p,"age"))
print(hasattr(p,"eat"))
# 如果忘记了某一个函数使用
help(setattr)