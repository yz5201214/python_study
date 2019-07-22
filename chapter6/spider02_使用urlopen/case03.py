'''
修改reuqeest的代理。user-agent
'''
from urllib import request,error,parse

# 第一种设置用户代理的方式
def test01():
    try:
        url = 'http://www.baidu.com'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        req = request.Request(url,data=None,headers=headers)
        rsq = request.urlopen(req)
        msg = rsq.read().decode('utf8')
        print(msg)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
# 第二种设置用户代理的方式
def test02():
    try:
        url = 'http://www.baidu.com'
        req = request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        rsq = request.urlopen(req)
        msg = rsq.read().decode('utf8')
        print(msg)
    except error.HTTPError as e:
        print(e)

# Ip代理ProxyHandler
def test03():
    url = 'http://www.baidu.com'
    # 这里开始设置IP代理
    proxy = {
        'http:':'121.10.141.149'
    }
    # 创建一个IP代理
    proxy_handle = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxy_handle)
    # 安装opener
    request.install_opener(opener)
    # 现在访问url，则使用的是代理IP
    try:
        rsp = request.urlopen(url)
        msg = rsp.read().decode('utf-8')
        print(msg)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)


# Ip代理 扩展
def test04():
    url = 'http://www.baidu.com/s?'
    # 这里开始设置IP代理
    proxy = {
        'http:':'115.204.206.172:8118'
    }
    # 创建一个IP代理
    proxy_handle = request.ProxyHandler(proxy)
    # 创建opener
    opener = request.build_opener(proxy_handle)
    # 安装opener
    request.install_opener(opener)
    # 现在访问url，则使用的是代理IP
    # 这里有个问题，通过百度，搜索IP的时候，显示的ip不是代理的IP
    searchData = {
        'wd':'ip'
    }
    try:
        dataStr = parse.urlencode(searchData)
        print(url+dataStr)
        rsp = request.urlopen(url+dataStr)
        msg = rsp.read().decode('utf-8')
        print(msg)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)

if __name__ == '__main__':
    test04()