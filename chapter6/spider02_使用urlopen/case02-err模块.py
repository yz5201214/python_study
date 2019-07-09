from urllib import error,request

def test01(url):
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        returnMsg = rsp.read().decode('utf-8')
        print(returnMsg)
    except error.URLError as e:
        print(e)

def test02(url):
    try:
        req = request.Request(url)
        rsp = request.urlopen(req)
        returnMsg = rsp.read().decode('utf-8')
        print(returnMsg)
    except error.HTTPError as e:
        print('httperror:{0}'.format(e.reason))
        print('httperror:{0}'.format(e))
    except error.URLError as a:
        print('urlerror:{0}'.format(a.reason))
        print('urlerror:{0}'.format(a))

if __name__ == '__main__':
    url = 'http://www.sipo.gov.cn/www'
    test02(url)