from subpackage02 import *
# 这里直接使用模块名称即可
stu = subPackage01.Student()
stu.name = "张三"
stu.say()
subPackage01.SayHello("李四")
# 因为__init__.py 中__all__所以不会执行其他的内容
# 下面会异常
inInit()