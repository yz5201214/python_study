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
    # test05()

    s = r'magnet:\?xt=urn:btih:[0-9a-fA-F]{40}'
    str = '香港 | 犯罪 | 警匪 | 2019 | 动作 | 黑帮 | 剧情 | 悬疑<br><br>◎简悍匪龙志强，在香港回归前趁香港英政府不作为，而屡犯巨案，先后绑架富豪利家及雷家之长子，勒索超过二十亿元，事主怕被报复,\n \n交赎款后都不敢报警。中国公安部极为关注，与香港警方合力，派香港警员何天卧底潜入龙志强犯罪团伙，发现他正策划绑架澳门富豪贺不凡，最终陆港警察合力勇擒龙志强，救出贺不凡。<br><br><img src="https://www.gogoimg.com/images/2019/07/24/2.Chasing.The.Dragon.II.Master.Of.Ransom.2019.WEB-1080p.X264.AAC-UUMp4_preview.jpg" width="1599" height="994"><span style="color:Red;"><strong>磁力链接<br><br>magnet:?xt=urn:btih:2B77512CBA241741632E91BBE8DF473372C31D5B<br><br>电驴链接<br><br>ed2k://|file|追龙2.Chasing.The.Dragon.II.Master.Of.Ransom.2019.WEB-1080p.X264.AAC-UUMp4.mp4|2125109805|3B2D49369C68EFDBDB9EBE4853467BD5|h=4YSGX37U5B6HMZEHUNOYK4VOYDIDLWTV|/</strong></span><br><br></p><p><br></p></div><div class="bg1 border post">\r\n\t\t\t\t\r\n\t\t\t\t\t\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t<div id="message_31980548" class="message">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t\t\t\t\t<!--\r\n\t\t\t\t\t\t\t\t\t\t\t\t-->\r\n<!-- #第一楼右侧广告 -->\n感谢楼主分享</div>\r\n\t\t\t\t\t\r\n\t\t\t\t\t\r\n\t\t\t\t\t\r\n\t\t\t\t\t\r\n\t\t\t'
    p = re.compile(s)
    print(str.replace('\t','').replace('\r','').replace('\n',''))
    m = p.findall(str.replace('\t','').replace('\r','').replace('\n',''))
    print(m)