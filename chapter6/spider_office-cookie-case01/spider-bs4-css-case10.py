from bs4 import BeautifulSoup
import requests,re

# 通过select等查询条件获取指定的内容
def test01():
    url = 'https://www.50s.wang/whole/1.html'
    rsq = requests.request("get",url=url)
    # 特别注意最后面的参数'lxml'，如果确实会出现异常 'str' object has no attribute 'decode'
    # 将整个页面代码进行初始化
    bs4 = BeautifulSoup(rsq.text,'lxml')
    # 页面元素美化 但是乱码。要解决的问题
    # html = bs4.prettify()
    tagDiv = bs4.select("div[class='movie-item-in']")
    movieInfo = {}

    for movieDiv in tagDiv:
        aList = movieDiv.select("a[style='position:relative;display:block;']")
        for aUrl in aList:
            print("url:{0},name:{1}".format(aUrl.attrs['href'], aUrl.attrs['title']))
        typeList = movieDiv.select("div[class='otherinfo']")
        for typeItem in typeList:
            print(typeItem.text)

if __name__ == '__main__':
    test01()