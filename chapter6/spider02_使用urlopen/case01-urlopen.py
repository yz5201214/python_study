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
    postDate = parse.urlencode(data).encode()
    # 这里开始请求
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
'''
使用request.Request
可以进行request的Head设置，与test06基本一样，只是换了request.Request来实现
'''
def test07(urlStr,content):
    # POST请求的数据，模拟form的数据一定是dict格式
    data = {
        # 传入输入的内容，此处是硬编码
        'kw': content
    }
    # 参数转码，转码后是字符串，转成bytes
    postDate = parse.urlencode(data).encode('utf-8')
    # 构造请求头 ，严格按照请求网址的需要进行构造
    # 请求头是一个dict格式
    # 主要用于身份欺骗，修改身份
    headers = {
        # 注意大小写，格式，有严格要求
        'Content-Length': len(content),
        'Content-Type': 'Application/x-www-form-urlencoded; Charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Cookie':'BAIDUID=E200EA6801B0E9C7CE6167DD50B04D5E:FG=1; BIDUPSID=E200EA6801B0E9C7CE6167DD50B04D5E; PSTM=1530116372; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=FTalQxdzhtWS1BTEhQenFmSDA4MDhYWUswbjVtY0pMQjdpcDluWnBQUDBveXBkSVFBQUFBJCQAAAAAAAAAAAEAAAC7rUAEeXo1MjAxMjE0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPQWA130FgNdR3; MCITY=-%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1562224719,1562577183,1562591128,1562679535; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1562680297; yjs_js_security_passport=b2249fca5dc95e64b6c5105009964738ab46afec_1562680336_js; from_lang_often=%5B%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'
    }
    try:
        # 构造一个Request的实例
        # 注意这里的请求参数，包含了url，post参数，以及请求Hearder信息
        req = request.Request(url=urlStr, data=postDate, headers=headers)
        # 因为构建Request的实例，所有的请求全部可以封装好，可以直接urlopen请求
        rsq = request.urlopen(req)
        json_data = rsq.read().decode('utf-8')
        # 注意返回的是json格式，如果不用json转换一下，看到的是乱码
        json_dict = json.loads(json_data.encode('utf-8'))
        print(json_dict)
        # 查看之后，发现是list
        print(json_dict.get('errno'))
        if json_dict.get('errno') == 0:
            print(json_dict.get('data'))
            for item in json_dict['data']:
                print('k-------' + item['k'])
                print('v-------' + item['v'])
    except Exception as e:
        print('error:::{0}'.format(e))
if __name__ == '__main__':
    # 自己论坛首页
    urlStr = 'http://www.cnmmp.net/forum.php'
    # 百度搜索
    sarchUrlStr = 'http://www.baidu.com/s?'
    # 自己论坛查询
    myForumSearchUrl = 'http://www.cnmmp.net/search.php?mod=forum&formhash=461af39c&srchtype=title&searchsubmit=yes&srhlocality=forum::index&'
    # 百度翻译
    baidufanyiUrl = 'https://fanyi.baidu.com/sug'

    testUrl = 'https://fanyi.baidu.com/'
    # test01(urlStr,chats_utf_8)
    # test02(urlStr)
    # test03(testUrl)
    content = input('search content:')
    # test04(sarchUrlStr,content)
    # test05(myForumSearchUrl,content)
    # test06(baidufanyiUrl,content)
    test07(baidufanyiUrl, content)
