import requests
from urllib import parse
'''
两种请求方式test01,test02返回的内容一致
'''
def test01():
    url = "http://www.baidu.com"
    # 这里返回的是整个页面的源码模式
    rsp = requests.get(url)
    print(rsp.text)

def test02():
    url = "http://www.baidu.com"
    # 这里返回的是整个页面的源码模式
    rsp = requests.request("get",url)
    print(rsp.text)

'''
注意headers和params设置
返回结果集
'''
def test03(str1):
    # 查询请求地址
    url = "https://www.baidu.com/s?"
    kw = {
        'wd':str1
    }
    reqHeader = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
    }
    rsq = requests.get(url=url,params=kw,headers=reqHeader)
    print(rsq.text)# unicode格式
    print(rsq.content)
    print(rsq.url)# 最终形成的请求地址
    print(rsq.encoding)# 字符集编码
    print(rsq.status_code)  # 请求返回码

'''
上面三个方法都是get请求，下面的案例是POST请求
'''
def test04Post(str1):
    url = "http://www.fanyi.baidu.com/sug"
    # 注意data并没有进行任何转码，直接传入
    data = {
        'kw':str1
    }
    handles = {
        'Content-Length':str(len(data))
    }
    rsq = requests.post(url,data=data,headers=handles)
    print(rsq.text)
    print(rsq.json())



if __name__ == '__main__':
    str1 = input("请输入你想搜索的内容:")
    # test01() # 普通get请求
    # test02() # 普通get请求
    # test03(str1) # 普通带headles的get请求
    # 妈的。百度翻译一直连接超时。
    test04Post(str1)