# os 相关操作
import os
def test01():
    # 获取当前的工作目录
    print(os.getcwd())
# chdir() 改变当前的工作目录
# os.chdir(路径)
# 切换os内容，并不是实际位置切换
def test02():
    os.chdir('C:/Users')
    print(os.getcwd())

# listdir() 获取目录中所有子目录和文件的名称列表
# windows下隐藏文件也会出现
def test03():
    print(os.listdir())

# makedirs()递归创建文件夹
# 如果参数不是绝对路径，则在os当前工作目录中间创建
# 初始化的时候会执行
def test04():
    os.makedirs("test03")# 当前工作目录
    os.makedirs("C:/test01/test02/test03")
    pass

#system() 运行系统的shell命令
# 输出命令执行的内容
# 中文乱码怎么处理
# 0 表示执行成功
def test05():
    rs = os.system("mkdir c:\\test")
    print(rs)
# getenv() 获取指定的系统环境变量值
# putenv() 设置环境变量
def test06():
    print(os.getenv("PATH"))

def test07():
    print("*"*100)
    print(os.name)
    print(os.pardir)
    print(os.curdir)
    print(os.sep)# 系统分隔符
    print(os.linesep)# 换行

# 绝对路径操作
def test08():
    # 中 .表示当前目录 ..父目录
    abstr01 = os.path.abspath(".")
    abstr02 = os.path.abspath("..")
    print(abstr01)
    print(abstr02)
# 获取路径中的基础文件名部分
def test09():
    abstr01 = os.path.abspath(".")
    # 获取最后的文件名部分
    nameStr = os.path.basename(abstr01)
    print(nameStr)
# join()
# os.path.join(pathStr1, pathStr2, pathStr3...)路径拼接
# split()文件路径和文件部分分离操作，返回元祖
def test10():
    # 主要用于文件操作中，拼接目录，防止因为操作系统不同导致目录分隔符号不一样导致异常
    absstr01 = os.path.abspath(".")
    print(os.path.join(absstr01,"test01", "test02"))
    # 文件路径和文件部分分离操作
    pathStr01 = os.path.abspath(".")+"\case01.py"
    x,y = os.path.split(pathStr01)
    print("文件路径：{0}，文件名称:{1}".format(x,y))

# isdir() 是否是目录
def test11():
    absstr01 = os.path.abspath(".")
    pathStr01 = os.path.abspath(".") + "\case01.py"
    print(os.path.isdir(pathStr01))
    print(os.path.isdir(absstr01))
# exists()目录是否存在
def test12():
    absstr01 = os.path.abspath(".")
    absstr02 = os.path.join(absstr01, "test01", "test02")# 拼接目录，实际电脑上不存该目录
    print(os.path.exists(absstr01))
    print(os.path.exists(absstr02))


#shutile详解
import shutil
def test13():
    # copy() 文件绝对路径拷贝 ，可以重命名，返回拷贝后的路径
    # shutil.copy2 与shutil.copy 唯一的区别在于copy2复制文件时尽量保留元数据
    str01 = shutil.copy("C:/kms8.log","C:/test/kms8_1111.log")
    print(str01)
# 拷贝，移动文件
def test14():
    # 只拷贝内容，当时目标文件不存在的时候，会自动创建，会将目标文件内容替换
    shutil.copyfile("C:/kms8.log","C:/test/kms8_22222.log")
    # 这里的move类似windows里面的剪切操作
    # 如果是linux的文件移除，copy创建操作，需要注意权限
    shutil.move("C:/test/kms8_22222.log","C:/")

# 文件归档和压缩处理
# make_archive()：归档操作
# make_archive('归档之后的目录和文件名','后缀','需要归档的文件夹')
# 返回归档后的地址
def test15():
    # 'format' is the archive format: one of "zip", "tar", "gztar",
    #"bztar", or "xztar".  Or any other registered format.
    shutil.make_archive('C:/mak','zip','C:/test')
# 归档之后，也可以解包，其实就是解压
# unpack_archive('压缩包地址','解压之后的地址')
def test16():
    shutil.unpack_archive('c:/mak.zip','c:/test01')

#zip压缩文件处理
import zipfile
def test17():
    # 获取压缩包信息
    zf = zipfile.ZipFile('c:/mak.zip')
    # 获取压缩包里面文件基本信息，大小，名称，类型等
    zf.getinfo("kms8_1111.log")
    # 获zip文档内所有文件的名称列表，返回数组
    nl = zf.namelist()
    print(nl)
    # 解压 ,如果解压的文件夹不存在，会自动创建，将压缩包解压
    zf.extractall("c:/test01")

# exit() 退出当前程序
if __name__ == '__main__':
    test17()