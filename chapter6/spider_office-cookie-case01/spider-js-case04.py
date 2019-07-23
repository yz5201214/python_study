from urllib import request,parse
import time,random,hashlib


def youdaoTest(str1):
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    data = {
        'i': 'hello',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15638508783116',
        'sign': 'b28471ebdd6838013c7ca974d48593fe',
        'ts': '1563850878311',# int(time.time()),
        'bv': '316dd52438d41a1d675c1d848edf4877',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    data = parse.urlencode(data).encode('utf-8')
    headers = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        # 如果这设置的不是压缩包模式，那么返回的内容可以decode，否则会异常
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '238',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1631468808@10.108.160.17; JSESSIONID=aaaFu9Tlqvv01dDK0JCWw; OUTFOX_SEARCH_USER_ID_NCOO=1935665156.876143; ___rl__test__cookies=1563847499586',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        req = request.Request(url=url, data=data, headers=headers)
        rsq = request.urlopen(req)
        html = rsq.read().decode('utf-8')
        print(html)
    except Exception as e:
        e
'''
这里是有道笔记的加密算法内容
var r = function(e) {
    var t = n.md5(navigator.appVersion),
    r = "" + (new Date).getTime(),
    i = r + parseInt(10 * Math.random(), 10);
    return {
        ts: r,
        bv: t,
        salt: i,
        sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
    }
};
'''
def youdaoSign(str1):
    m5 = hashlib.md5()
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    ts = int(time.time()*1000)
    salt = ts + random.randint(0,10)
    signStr = 'fanyideskweb' + str1 + str(salt) + 'n%A-rKaT5fb[Gy?;N5@Tj'
    m5.update(signStr.encode('utf-8'))
    sign = m5.hexdigest()
    data = {
        'i': str1,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': salt,
        'sign': sign,
        'ts': str(ts),
        'bv': '316dd52438d41a1d675c1d848edf4877',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    data = parse.urlencode(data).encode('utf-8')
    headers = {
        'Accept': 'application/json,text/javascript,*/*;q=0.01',
        # 如果这设置的不是压缩包模式，那么返回的内容可以decode，否则会异常
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        # 长度必须是传入参数的长度，否则会请求异常
        'Content-Length': len(data),
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=-1631468808@10.108.160.17; JSESSIONID=aaaFu9Tlqvv01dDK0JCWw; OUTFOX_SEARCH_USER_ID_NCOO=1935665156.876143; ___rl__test__cookies=1563847499586',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        req = request.Request(url=url, data=data, headers=headers)
        rsq = request.urlopen(req)
        html = rsq.read().decode('utf-8')
        print(html)
    except Exception as e:
        e


if __name__ == '__main__':
    str1 = input("请输入你要翻译的内容:")
    # youdaoTest(str1)
    youdaoSign(str1)
