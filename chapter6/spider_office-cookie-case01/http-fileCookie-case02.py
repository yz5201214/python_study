from urllib import request,parse
from http import cookiejar

# 创建一个fileCookie实例，同时命名cookie文件保存的名称
'''
这里需要特别注意：
FileCookieJar 实际上并没有实现save方法
但是MozillaCookieJar，LWPCookieJar 都实现了
所以如果需要将cookie文件进行保存，不能使用FileCookieJar.save
'''
fileName = 'cookieTest.txt'
fileCookie = cookiejar.MozillaCookieJar(fileName)
# fileCookie管理器
cookie_Hanlder = request.HTTPCookieProcessor(fileCookie)
# http，https请求管理器
http_Hanlder = request.HTTPHandler()
https_Hanlder = request.HTTPSHandler()
# 请求管理器
opener = request.build_opener(http_Hanlder,https_Hanlder,cookie_Hanlder)
def fileCookieTest(url):
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
        rsq = opener.open(req)
        # 开启保存cookie到文件
        # ignore_discard 表示即时cookie将要被丢弃，也要保存下来
        # ignore_expires 表示如果该文件中cookie即时已经过期，也要覆盖保存下来
        fileCookie.save(ignore_discard=True,ignore_expires=True)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    logUrl = "http://www.renren.com/PLogin.do"
    fileCookieTest(logUrl)

