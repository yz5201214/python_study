import re
'''
之前讲过，这里复述
其实前面都写过。太久了。。都忘记了。。哈哈哈哈哈
'''
def test01():
    str = "http://www.runoob.com:80/html/html-tutorial.html"
    # r表示原生字符串，后面不需要转义
    # p 是Pattern对象
    p = re.compile(r"/(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)/")
    # m是Match对象
    # 默认匹配从头开始
    m = p.match(str)
    print(m)

def test02():
    str = 'ni hao'
    s = r'([a-z]+) ([a-z]+)'
    p = re.compile(s,re.I) # s.I忽略大小写
    m = p.match(str,0,100)
    print(m)
    # 匹配成功后的整个字符串
    print(m.group(0))
    #  返回匹配成功的整个字符串的宽度
    print(m.span(0))
    # 返回第一个分组匹配成功的字符串
    print(m.group(1))
    # 等价于m.group(1),m.group(2)..........
    print(m.groups())

def test03():
    s = r'\d+'
    str = 'one123123123tuwo23142342thre213434'
    p = re.compile(s,re.I)
    # 从头位置找，找不到
    m = p.match(str,0,100)
    print(m)
    # 查找全世界，一次匹配
    m = p.search(str)
    print(m)
    # 全部匹配返回列表
    m = p.findall(str)
    print(m)
    # 这里返回的是一个可迭代对象，直接输出不可以，需要迭代输出
    m = p.finditer(str)
    x = 0
    for item in m:
        # 这个item是个Match对象
        print("迭代对象{0}：{1}".format(x,item.group(0)))
        x = x+1

# 这里主要讲中文匹配
def test04():
    str1 = u"你好啊 老子要 匹配 中文 啊"
    s = r'([\u4300-\u9fa5])+ ([\u4300-\u9fa5])+ ([\u4300-\u9fa5])+ ([\u4300-\u9fa5])+'
    p = re.compile(s)
    m = p.match(str1)
    print(m)
# 贪婪，非贪婪
def test05():
    str1 = u"你好啊老子要匹配中文啊"
    # 默认贪婪模式
    s = r'[\u4300-\u9fa5]+'
    # 注意？号的位置，非贪婪模式
    s1 = r'[\u4300-\u9fa5]+?'
    p = re.compile(s)
    m = p.match(str1)
    print(m)
    p = re.compile(s1)
    m = p.match(str1)
    print(m)




if __name__ == '__main__':
    # test01()
    # test02()
    # test03()
    # test04()
    test05()