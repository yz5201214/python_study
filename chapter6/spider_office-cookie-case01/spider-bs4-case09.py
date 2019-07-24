from bs4 import BeautifulSoup
import requests,re
'''
利用beautifusoup《CSS选择器》进行页面数据爬取
'''
def bs4Test01():
    url = 'https://www.baidu.com'
    rsp = requests.request('get',url=url)
    # 下面开始使用
    bs = BeautifulSoup(rsp.text,'lxml')
    html = bs.prettify()
    print(html)

# 使用四大对象
def bs4Test02():
    url = 'https://www.50s.wang/whole/1.html'
    rsp = requests.request('get', url=url)
    # 下面开始使用
    bs = BeautifulSoup(rsp.text, 'lxml')
    html = bs.prettify()
    # print(html)
    # 这里只能读取第一个
    print(bs.link)
    # 读取他的全部属性
    print(bs.link.attrs)
    # 读取他的指定属性的指定内容
    print(bs.link.attrs['rel'])
    # 注意
    print("="*20)
    print(bs.title)
    print(bs.title.name)
    print(bs.title.attrs)
    # 注意这里输出的是标签里面的内容
    print(bs.title.string)
    print("=" * 20)
    # 下面beautifulsoup的本质
    print(bs.name)
    print(bs.attrs)

# 遍历整个页面
def forHtmlTest03():
    url = 'https://www.50s.wang/whole/1.html'
    rsp = requests.request('get', url=url)
    # 下面开始使用
    bs = BeautifulSoup(rsp.text, 'lxml')
    print("=" * 20)
    '''
    for item in bs.body.contents:
        if item.name == 'div':
            for divContent in item.contents:
                # print(divContent)
                if divContent.name =='a':
                    # and divContent.attrs['style'] == 'position:relative;display:block;'
                    print(divContent.attrs['style'])
    '''
# 不使用上面的挨个标签遍历。采用find_all
def forHtmlTest04():
    url = 'https://www.50s.wang/whole/1.html'
    rsp = requests.request('get', url=url)
    # 下面开始使用
    bs = BeautifulSoup(rsp.text, 'lxml')
    print("=" * 20)
    # 查找所有tag是a标签的列表
    '''
    aTags = bs.find_all(name='a')
    print(aTags)
     for aItem in aTags:
         print(aItem.attrs)
    '''

    # 使用正则表达式进行find_all，其实是找到对应标签，并且属性style=指定值的内容
    html = bs.find_all(re.compile('^a.*'),style='position:relative;display:block;')
    for aItem in html:
        if aItem.name =='a':
            print("name:" + aItem.attrs['title'])
            print("url:"+aItem.attrs['href'])

if __name__ == '__main__':
    # bs4Test01()
    bs4Test02()
    # forHtmlTest03()
    # forHtmlTest04()