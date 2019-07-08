'''
使用urllib.request请求一个网页内容，并把内容打印出来
http://www.cnmmp.net/forum.php
'''
from urllib import request,error,parse
import chardet
import json

chats_utf_8 = 'utf-8'
# 获取网页所有内容
def test01(urlStr,chats):
    try:
        rep = request.urlopen(urlStr)
        html = rep.read()
        # 返回结果读取，类型为bytes，需要解码
        print(html.decode(chats))
    except error as e:
        e
# 自动获取网页编码集，爬取完成后，根据网页原生的编码集进行转码
def test02(urlStr):
    try:
        rep = request.urlopen(urlStr)
        html = rep.read()
        testChats = chardet.detect(html)
        # 使用get获取到网页的编码集，如果有值，使用取到的值，没有则使用utf-8
        print(html.decode(testChats.get("encoding","utf-8")))
    except error as e:
        e
# urlopen 返回的对象b
def test03(urlStr):
    try:
        rep = request.urlopen(urlStr)
        print(type(rep))
        print(rep)
        print(rep.geturl())
        print('返回mate信息 :\n{0}'.format(rep.info()))
        print('请求状态 :{0}'.format(rep.getcode()))
    except error as e:
        e
# 请求的同时，传输参数
'''
对url进行参数传入的时候，需要parse转码才能使用
baidu搜索的写法
GET
'''
def test04(urlStr,sarchContent):
    # 想要传入参数，需要使用字典结构
    requestData = {
        'wd': sarchContent
    }
    # 转换URL编码
    qs = parse.urlencode(requestData)
    print(qs)
    urlstr = urlStr + qs;
    # 如果直接使用刻度的带参数的URL，是不能访问的，需要URL转码
    rep = request.urlopen(urlstr)
    html = rep.read()
    print(html.decode(chardet.detect(html).get("encoding", "utf-8")))

# 自己的论坛查询写法
'''
一直返回：您当前的访问请求当中含有非法字符，已经被系统拒绝
浏览器访问没问题，应该是做了爬虫限制，可能要模拟Heard信息才行
'''
def test05(urlStr,sarchContent):
    requestData = {
        'srchtxt': sarchContent
    }
    # 转换URL编码
    qs = parse.urlencode(requestData)
    urlstr = urlStr + qs;
    print(urlstr)
    rep = request.urlopen(urlstr)
    html = rep.read()
    print(html.decode(chardet.detect(html).get("encoding","utf-8")))


'''
    post传递参数，test04，03都是GET的
    案例是针对百度翻译
    百度翻译请求，返回的头部：content-type: application/json，表示返回内容是json格式，注意导入的json包
    利用data构造内容，然后urlopen打开
    返回一个json格式结果
    问题，返回的内容不全
'''
def test06(urlStr,content):
    # POST请求的数据，模拟form的数据一定是dict格式
    data = {
        # 传入输入的内容，此处是硬编码
        'kw':content
    }
    # 参数转码，转码后是字符串，转成bytes
    postDate = parse.urlencode(data).encode('utf-8')
    # 构造请求头 ，严格按照请求网址的需要进行构造
    # 请求头是一个dict格式
    headers = {
        #注意大小写，格式，有严格要求
        'Content-Length':len(content),
        'Content-Type':'application/json'
    }
    # 这里开始请求
    request.AbstractHTTPHandler(headers)
    rsp = request.urlopen(urlStr,data = postDate)
    # 出来的是乱码。需要转码
    json_data = rsp.read().decode('utf-8')
    # 注意返回的是json格式，如果不用json转换一下，看到的是乱码
    json_dict = json.loads(json_data.encode('utf-8'))
    # 查看之后，发现是list
    print(json_dict.get('errno'))
    if json_dict.get('errno') == 0:
        print(json_dict.get('data'))
        for item in json_dict['data']:
            print('k-------'+item['k'])
            print('v-------' + item['v'])



if __name__ == '__main__':
    # 自己论坛首页
    urlStr = 'http://www.cnmmp.net/forum.php'
    # 百度搜索
    sarchUrlStr = 'http://www.baidu.com/s?'
    # 自己论坛查询
    myForumSearchUrl = 'http://www.cnmmp.net/search.php?mod=forum&formhash=461af39c&srchtype=title&searchsubmit=yes&srhlocality=forum::index&'
    # 百度翻译
    baidufanyiUrl = 'https://fanyi.baidu.com/sug'
    # test01(urlStr,chats_utf_8)
    # test02(urlStr)
    # test03(urlStr)
    content = input('search content:')
    # test04(sarchUrlStr,content)
    # test05(myForumSearchUrl,content)
    test06(baidufanyiUrl,content)
