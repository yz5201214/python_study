# random  随机模块
import random
def test01():
    # 获取0-1之间的随机小数
    print(random.random())
    # 指定区间的随机小数
    print(random.uniform(0,100))
    # 指定区间的随机整数 ,实际常用
    print(random.randint(0,100))
# choice() 随机返回序列中的某个值
# 参数是list
def test02():
    l = [i for i in range(10)]
    print(l)
    print(random.choice(l))

# shuffle() 随机打乱列表
# 原地打乱，并不会生成一个新的随机list
# 注意下面输出的内容
def test03():
    l = [i for i in range(10)]
    random.shuffle(l)
    print(random.shuffle(l))
    print(l)

if __name__ == '__main__':
    test03()