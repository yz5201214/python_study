from urllib import request ,error,parse
from http import cookiejar


def test01(url):
    file = cookiejar.FileCookieJar
    mozilla = cookiejar.MozillaCookieJar
    lwp = cookiejar.LWPCookieJar
    return None

if __name__ == '__main__':
    txt = input("请输入你需要的内容:")
    print(txt)