
class A():
    def jisuan(self):
        try:
            num = int(input("input you number"))
            ret = 100/num
            print("100 / {0}结果是：{1}".format(num,ret))
        except ZeroDivisionError as e:
            print("输入异常：{0}".format(e.args))
        except Exception as a:
            print("其他错误：{0}".format(a.args))
        else:
            print("成功执行")
        finally:
            print("完成处理")
        # 异常后继续处理，除非中间执行断开exit()
        print("是否继续执行")
a = A()
#a.jisuan()

class B():
    def testRaise(self):
        try:
            print("来呀，快活呀！")
            # 程序员故意抛出异常，可以指定异常类别
            raise NameError
        except TypeError as e:
            print("手动触发异常e:{0}".format(e))
        except NameError as n:
            print("手动触发异常n:{0}".format(n))
        finally:
            print("完成")

b = B()
#b.testRaise()

# 自定义异常是否能够返回具体的错误信息呢
# 自定义异常，必须是系统异常的子类
class CustomErr(Exception):
    pass

class D():
    def testCustomErr(self):
        try:
            print("来呀，快活呀！")
            # 程序员故意抛出异常，如果是自定义的，只能指向之定义，不能指向父类,但是父类可以捕获自定义
            raise CustomErr
        # 谁在前捕获谁。注意下面
        except ValueError as e:
            print("父类异常e:{0}".format(e))
        except CustomErr as e:
            print("自定义异常e:{0}".format(e))

        finally:
            print("完成")

d = D()
d.testCustomErr()