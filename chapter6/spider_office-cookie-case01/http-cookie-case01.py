from urllib import request,parse
from http import cookiejar


# 创建cookie实例
cookie = cookiejar.CookieJar()
file = cookiejar.FileCookieJar()
mozilla = cookiejar.MozillaCookieJar()
lwp = cookiejar.LWPCookieJar()
# 创建cookie管理器
cookie_Headle = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_Headle = request.HTTPHandler()
# 生成https管理器
https_Headle = request.HTTPSHandler()
# 创建请求管理器
oper = request.build_opener(http_Headle,https_Headle,cookie_Headle)

'''
进行登录操作
登录完成后，将请求返回的handle信息将由请求管理器保存，可以重复使用
在请求管理器生命周期结束后，所有的hanlder信息自动销毁
'''
def test01(url):
    data = {
        # 用户名，密码，验证码
        "email":"yz120821884@163.com",
        "password":"1qaz@WSX"
        # "icode":""
    }
    try:
        # 参数编码
        data = parse.urlencode(data)
        # 创建一个请求对象
        req = request.Request(url,data=data.encode())
        # 发起请求
        rsq = oper.open(req)
        print(rsq)
    except Exception as e:
        print(e)
# 重复使用请求管理器中的信息，可以直接打开登录后个人主页
def getCookie(url):
    # 如果已经执行了登录，那么cookie自动会填充到open
    rsp = oper.open(url)
    html = rsp.read().decode()
    with open("test.html","w") as f:
        f.write(html)

'''
在请求管理器中可以直接查看到所有的请求返回的hanlder信息
'''
def printCookieInfo(url):
    data = {
        # 用户名，密码，验证码
        "email": "yz120821884@163.com",
        "password": "1qaz@WSX"
        # "icode":""
    }
    try:
        # 参数编码
        data = parse.urlencode(data)
        # 创建一个请求对象
        req = request.Request(url, data=data.encode())
        # 发起请求
        rsq = oper.open(req)
        # 直接获取登录完成后的cookie信息
        # cookie信息的类型是字典类型
        print(cookie)
        for item in cookie:
            print(type(item))
            # 这里的item是一个cookie实例
            for c in dir(item):
                # 这里输出cookie中所有的信息
                print("cookie -----------"+c)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    logUrl = "http://www.renren.com/PLogin.do"
    myProfile = "http://www.renren.com/288810313/profile"
    # test01(logUrl)
    # getCookie(myProfile)
    printCookieInfo(logUrl)