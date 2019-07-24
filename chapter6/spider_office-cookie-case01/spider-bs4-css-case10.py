from bs4 import BeautifulSoup
import requests,re

# 通过select等查询条件获取指定的内容
def test01(url):
    rsq = requests.request("get",url=url)
    # 特别注意最后面的参数'lxml'，如果确实会出现异常 'str' object has no attribute 'decode'
    # 将整个页面代码进行初始化
    bs4 = BeautifulSoup(rsq.text,'lxml')
    # 页面元素美化 但是乱码。要解决的问题
    # html = bs4.prettify()
    tagDiv = bs4.select("div[class='movie-item-in']")
    for movieDiv in tagDiv:
        aList = movieDiv.select("a[style='position:relative;display:block;']")
        for aUrl in aList:
            print("url:{0},name:{1}".format(aUrl.attrs['href'], aUrl.attrs['title']))
        typeList = movieDiv.select("div[class='otherinfo']")
        for typeItem in typeList:
            textStr = typeItem.text
            textStr = textStr[3:len(textStr)-1]
            print("类型数组：{0}".format(str(textStr.split(" "))))


def getNext(url):
    rsq = requests.request("get", url=url)
    # 特别注意最后面的参数'lxml'，如果确实会出现异常 'str' object has no attribute 'decode'
    # 将整个页面代码进行初始化
    bs4 = BeautifulSoup(rsq.text, 'lxml')
    # 页面元素美化 但是乱码。要解决的问题
    # html = bs4.prettify()
    # 获取所有分页信息
    nextUrl = ""
    pagerDiv = bs4.select("div[class='pager-bg']")
    for itemPage in pagerDiv:
        pagerList = itemPage.select("a[rel='next']")
        nextUrl = pagerList[0].attrs['href']
    return nextUrl

if __name__ == '__main__':
    host = 'https://www.50s.wang'
    url = 'https://www.50s.wang/whole/1.html'
    # test01(url)
    nextUrl = host+getNext(url)
    print(nextUrl)
    test01(nextUrl)