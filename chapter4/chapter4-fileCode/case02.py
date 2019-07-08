# pickle 的操作案例
import pickle

# 这里是序列化操作
def test01():
    age = "这里是二进制写入"
    with open(r"test02.txt", "wb") as fs:
        pickle.dump(age,fs)
# 这里是反序列化操作
def test02():
    with open(r"test02.txt", "rb") as fs:
        age = pickle.load(fs)
        print(age)

# shelve 持久化案例
# 创建了三个文件，类似于数据库，
import shelve
# shelve 写入操作
def test03():
    shv = shelve.open(r"shv.db")
    shv['one'] = 1
    shv['two'] = 2
    shv['three'] = 3
    shv['for'] = 4
    shv.close()
# shelve读取操作
def test04():
    shv = shelve.open(r"shv.db")
    # 如果取没有的key值，会异常，会导致没有关闭操作，所以一般配套try使用
    try:
        print(shv['one'])
    except Exception as e:
        print(e)
    finally:
        shv.close()
# 修改内容结构操作
def test05():
    shv = shelve.open(r"shv.db")
    try:
        shv["one"] = {"wo":"my","ni":"your"}
    finally:
        shv.close()
def test06():
    shv = shelve.open(r"shv.db")
    try:
        one = shv["one"]
        print(one)
    finally:
        shv.close()
# shelve 忘记写回，需要使用强制写回
# 注意test07 与test08的区别
def test07():
    shv = shelve.open(r"shv.db")
    try:
        one = shv["one"]
        print(one)
        # 此处，虽然shelv关闭，内容实际还没有写回，导致下面读的时候，还是原来的值
        one["wo"] = "nibaba"
    finally:
        shv.close()

    shv = shelve.open(r"shv.db")
    try:
        one = shv["one"]
        print(one)
    finally:
        shv.close()
# 这里注意：writeback=True
def test08():
    shv = shelve.open(r"shv.db", writeback=True)
    try:
        one = shv["one"]
        print(one)
        # 此处，虽然shelv关闭，内容实际还没有写回，导致下面读的时候，还是原来的值
        one["wo"] = "nibaba"
    finally:
        shv.close()

    shv = shelve.open(r"shv.db")
    try:
        one = shv["one"]
        print(one)
    finally:
        shv.close()
# shelve可以使用with的上下文管理
def test09():
    with shelve.open(r"shv.db", writeback=True) as shv:
        one = shv["one"]
        print(one)
        one["wo"] = "你爷爷"

    with shelve.open(r"shv.db") as shv:
        one = shv["one"]
        print(one)

if __name__ == '__main__':
    test09()