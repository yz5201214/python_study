# 本身python的文件命名是不允许数字开头，但是如果有的情况下，直接import会异常，这个时候需要借助importlib包来导入以数字开头的模块名称
# 使用方法：name = importlib.import_module("包名")
import chapter4.package.package01 as test01 # 这里也可以直接写包名，不写路径，但是不能有命名重复的模块名称，一般通过全路径引入，然后使用别名

stu = test01.Student()
stu.name = "张三"
print(stu.name)
print(stu.age)
stu.say()

test01.SayHello(stu.name)