from urllib import request,parse
from http import cookiejar

# 创建cookie实例
cookie = cookiejar.MozillaCookieJar()
# 创建cookie管理器
cookie_Headle = request.HTTPCookieProcessor(cookie)
# 创建http，https请求管理器
http_Headle = request.HTTPHandler()
https_Headle = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_Headle,https_Headle,cookie_Headle)

def doSaveCookie(reqUrl,fileName):
    data = {
        # 用户名，密码，验证码
        "email": "yz120821884@163.com",
        "password": "1qaz@WSX"
        # "icode":""
    }
    data = parse.urlencode(data)
    req = request.Request(url=reqUrl,data=data.encode('utf-8'))
    opener.open(req)
    cookie.save(filename=fileName,ignore_discard=True,ignore_expires=True)
    rsq = opener.open("http://www.renren.com/288810313/profile")
    print(rsq.read().decode('utf-8'))

# 如果利用上面的方法将cookie保存成文件，那么后续的请求，就不要从新登陆等操作了。直接请求完事
def doReadCookie(reqUrl,fileName):
    # 创建cookie实例
    cookie1 = cookiejar.MozillaCookieJar()
    cookie1.load(filename=fileName)
    # 创建cookie管理器
    cookie_Headle1 = request.HTTPCookieProcessor(cookie1)
    # 创建http，https请求管理器
    http_Headle1 = request.HTTPHandler()
    https_Headle1 = request.HTTPSHandler()
    # 创建请求管理器
    opener1 = request.build_opener(http_Headle1, https_Headle1, cookie_Headle1)
    rsq = opener1.open(reqUrl)
    html = rsq.read().decode('utf-8')
    print(html)

if __name__ == '__main__':
    logUrl = "http://www.renren.com/PLogin.do"
    myProfile = "http://www.renren.com/288810313/profile"
    fileName = 'testCookie.txt'
    # 保存完成后，读取测试 ，这里的读取，好像不行。不知道问题在哪里，从文件中读取cookie好像不生效
    # doSaveCookie(logUrl,fileName)
    doReadCookie(myProfile,fileName)