from lxml import etree
'''
主要作用是解析HTML代码
这里可以用把HTML字符串，转换成HTML文档
etree主要可以补全HTML代码，解析HTML
'''
def test01():
    str1 = '''
        <div>
            <ul>
                <li class='item-0'><a href = '1.html'>0.html</a></li>
                <li class='item-1'><a href = '1.html'>1.html</a></li>
                <li class='item-2'><a href = '1.html'>2.html</a></li>
                <li class='item-3'><a href = '1.html'>3.html</a></li>
                <li class='item-4'><a href = '1.html'>4.html</a></li>
                <li class='item-5'><a href = '1.html'>5.html</a></li>
                <li class='item-6'><a href = '1.html'>6.html</a></li>
                <li class='item-7'><a href = '1.html'>7.html</a></li>
            <ul>
        </div>
    '''
    html = etree.HTML(str1)
    s = etree.tostring(html)
    print(s)

# etree与XPath的配合使用
def test02():
    None

if __name__ == '__main__':
    test01()