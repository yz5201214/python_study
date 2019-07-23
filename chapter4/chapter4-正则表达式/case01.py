# re所有python的正则的包
import re

def test01():
    # r 表示字符串不转义
    p = re.compile(r'\d+')
    #字符串中是否含有指定的正则表达式内容
    a = 'j31lk2j3oi12j31oi2j31oi2j3oi1j23oi1j2io3j1oi23j'
    m = p.match(a)
    print(m)

def test02():
    # r 表示字符串不转义
    p = re.compile(r'\d+')
    #字符串中是否含有指定的正则表达式内容
    a = 'as98df8asd8fa9d8f9a8dsf'
    # 指定范围查找
    m = p.match(a,2,101)
    print(m)
    print(m[0])
    print(m.start())
    print(m.end())

def test03():
    # 参数re.I 表示忽略大小写
    # 正则表达式，里面包含了两组，所以后面的输出也会有组的概念
    p = re.compile(r'([a-z]+) ([a-z]+)',re.I)
    m = p.match("I want to cao ni ma")
    print(m)
    # 输出全部
    print(m[0])
    # 输出全部 注意下面两种的输出的内容格式
    print(m.group(0))
    print(m.groups())
    # 下标 1 开始，输出的内容是按照正则分组来
    print(m.group(1) + '---')
    print(m.group(2)+'---')
    # 越界 IndexError: no such group
    # print(m.group(3) + '---')

# 查找
def test04():
    p = re.compile(r'\d+')
    m = p.search("a9d8fs9d8f9sd8f9s8df9sd89fdf")
    print(m.group())
    # 返回的是结果集合
    m1 = p.findall("a9d8fs9d8f9sd8f9s8df9sd89fdf")
    print(m1)
    # 注意下面的写法 返回的是一个m 集合
    m2 = p.finditer("a9d8fs9d8f9sd8f9s8df9sd89fdf")
    for x in m2:
        print(x[0])

# 替换，注意替换的内容
def test05():
    p = re.compile(r'(\w+) (\d+)')
    s = 'hello 123 wang 456 cheng, wo cao ni ma'
    sTest = p.sub('Hello world',s)
    print(sTest)

# 中文匹配
def test06():
    # 这里是中文匹配
    # 注意全角标点什么的不包括
    p = re.compile(r'[\u4e00-\u9fa5]')
    m = p.findall("我日你妈mmp，，，，,,,,你晓得个chuizi")
    print(m)
# 贪婪和非贪婪
def test07():
    a = u'<div>name</div><div>age</div><div>sex</div>'
    # 默认是下面这种贪婪模式
    p1 = re.compile(r'<div>.*</div>')
    # ? 下面是非贪婪模式
    p2 = re.compile(r'<div>.*?</div>')
    # 注意输出内容
    m1 = p1.search(a)
    print(m1.group())
    m2 = p2.search(a)
    print(m2.group())

if __name__ == '__main__':
    # test01()
    test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()

