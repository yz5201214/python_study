'''
    面向对象课程1的案例
'''
# 空类
class Student():
    # pass直接跳过，空类的定义必须使用pass，否则异常
    pass
# 定义一个对象
student1 = Student()

class PythonStudent():
    # 类属性
    name = None
    sex = None
    age = None
    course = 'Python'
    # 注意缩进
    # 系统默认一个self参数
    def doHomeWork(self):
        print('在做作业')
        #所有方法建议使用return
        return None

# 实例化一个学生2
student2 = PythonStudent()
student2.name = '名字'
student2.sex = '男'
student2.age = 18
student2.doHomeWork()
print(student2)

print(PythonStudent.__dict__)
print(student2.__dict__)
print("*"*20)

