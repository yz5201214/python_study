
# 打开文件，后面必须追加关闭操作
# r表示后面字符串内容不需要转义
# 在当前模块的路径内，创建了一个test01.txt
def test01():
    f = open(r"test01.txt", "w")
    f.close()
# with ,文件作用域会自动执行关闭文件操作
def test02():
    with open(r"test01.txt", "r") as f: # 中文好像有编码问题
        l1 = f.readline()
        # 此结构能够保证完整读取文件知道结束
        # 一直往下读，直到读不到内容， 返回空
        while l1:
            print(l1)
            l1 = f.readline()
# list 将文件内容转换成集合 以行为单位
def test03():
    with open(r"test01.txt", "r") as f:
        l1 = list(f)
        for x in l1:
            print(x)
# read 操作
def test04():
    with open(r"test01.txt", "r") as f:
        i = 1;
        l1 = f.read(i)
        while l1:
            print(l1)
            i +=1
            l1 = f.read(i)
# seek 案例
# 打开文件后，从第4个字节开始读取
def test05():
    with open(r"test01.txt","r") as f:
        # seek是以字节为单位
        f.seek(3,0)
        l1 = f.read()
        print(l1)
import time
def test06():
    with open(r"test01.txt", "r") as f:
        # read参数的单位是字符，可以理解成一个汉字就是一个字符
        f1 = f.read(3)
        while f1:
            print(f1)
            time.sleep(1)
            f1 = f.read(3)
# tell 案例
def test07():
    with open(r"test01.txt", "r") as f:
        l1 = f.read(3)
        post = f.tell()
        while l1:
            print(post)
            print(l1)
            l1 = f.read(3)
            post = f.tell()
# write，writelines 案例
# 注意这里是以a的module打开-append
def test08():
    with open(r"test01.txt", "w",encoding="utf-8") as f:
        # f.write("\n我日你妈 \n 日你全家")
        l = ["我","日","你","大","爷zx"]
        f.writelines(l)
if __name__ == '__main__':
    test08()