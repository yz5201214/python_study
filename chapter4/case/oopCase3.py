# 这里主要讲封装
class testA():
    name = "zhansan"
    __age = 18



mA = testA()
mA.name = "lisi"
# __age 点不出来
print(testA.__dict__)
# 强行访问私有，一般不建议用
mA._testA__age = 20
print(mA._testA__age)