import json,re,threading,requests,base64,execjs,sys
from bs4 import BeautifulSoup
from urllib import parse



def hello(name):
    print("hello %s\n" % name)

    global timer
    timer = threading.Timer(2.0, hello, ["Hawk"])
    timer.start()

def  chenluo():
    rsq = requests.request("get", url='https://www.50s.wang/play/137306/1/1.html')
    bs4 = BeautifulSoup(rsq.text, 'lxml')
    print(bs4.select("#player iframe"))
    if len(bs4.select("#player iframe")) > 0:
        iframeSrc = bs4.select("#player iframe")[0].attrs['src']
        iframeList = bs4.select("iframe")
        iframeStr = str(iframeList[0])
        print(iframeStr)
        if iframeSrc.find('m3u8') < 0:
            parseTuple = parse.urlparse(iframeSrc)
            print(parseTuple)
            urlDict = parse.parse_qs(parseTuple.query)
            if urlDict.__contains__('url'):
                lastUrl = urlDict['url'][0]
                print(lastUrl)
                if lastUrl.find('http://') >= 0 or lastUrl.find('https://') >= 0 or lastUrl.find('miguvideo') > 0:
                    abc = 'https://www.heimijx.com/jx/api/?url=' + lastUrl
                    print(abc)
                else:
                    postData = {
                        'url': lastUrl
                    }
                    prsq = requests.request('post', url='https://chenluo3.chenluo.org/chenluonuox/api.php',
                                            data=postData)
                    if prsq.status_code != 404:
                        bs4 = BeautifulSoup(prsq.text, 'lxml')
                        jsonItem = json.loads(bs4.p.string)
                        print(jsonItem)
                        abc = base64.b64decode(jsonItem['url'])
                        abc = abc.decode('gbk')
                        p = re.compile(r'https://.*')
                        m = p.findall(abc)
                        if len(m) > 0:
                            realSrc = m[0]
                            abc = iframeStr.replace(iframeSrc, realSrc)
                            print(abc)
    else:
        for scriptItem in bs4.select('script'):
            if str(scriptItem).find('videoObject') >= 0:
                videoStr = scriptItem.text
                p = re.compile(r'([a-zA-z]+://[^\s]*[$\'|\"])')
                m = p.findall(videoStr)
                for mx in m:
                    if mx.find('.m3u8') >= 0:
                        print(mx[0:-1])
                '''
                ctx = execjs.compile(scriptItem.text)
                videoObject = ctx.eval('videoObject')
                print(videoObject)
                '''
    print('*' * 100)

    '''
    postData = {
        'url':'1098_91e25dcd592a609988761dcbe69d3f65'
    }
    prsq = requests.request('post',url='https://chenluo3.chenluo.org/chenluonuox/api.php',data=postData)
    bs4 = BeautifulSoup(prsq.text, 'lxml')
    jsonItem = json.loads(bs4.p.string)
    print(jsonItem)
    abc = base64.b64decode(jsonItem['url'])
    print(type(abc))
    print(abc.decode('gbk'))
    '''


if __name__ == "__main__":
    '''
    rsq = requests.get('https://www.cmdy5.com/play/27439.html?27439-2-1')
    soup = BeautifulSoup(rsq.text, 'lxml')
    for scrpit_item in soup.select('script'):
        try:
            src_str = scrpit_item.attrs['src']
            if src_str.find('27439')>=0:
                js_url = 'https://www.cmdy5.com/'+src_str
                break
        except Exception as e:
            continue
    if js_url is not None:
        print(js_url)
        rsq = requests.get(js_url)
        soup = BeautifulSoup(rsq.text, 'lxml')
        soup.prettify('utf-8')
        print(rsq.text)
        print(parse.unquote(soup.text,encoding='utf-8', errors='replace'))
    '''
    abc = '%u7b2c01%u96c6'
    abc = abc
    print(parse.quote("第01集"))
    print(parse.unquote(abc))

