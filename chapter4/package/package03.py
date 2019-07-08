# 导入模块中，指定的类或者函数
from chapter4.package.package01 import Student,SayHello
stu = Student()
stu.name = "张三"
stu.say()

SayHello("李四")