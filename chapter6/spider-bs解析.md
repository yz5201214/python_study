# bs4
* bs4 全名：BeautifulSoup4
    * 官方文档：https://beautifulsoup.readthedocs.io/zh_CN/v4.4.0/
    * 使用案例：spider-bs4-case09.py
    * CSS选择器
    * 四大对象
        * Tag
            * 对应html标签
            * 可以通过soup.tag_name获取标签名
            * 两个重要属性
                * name 标签名称
                * attrs 读取指定标签的属性内容
        * NavigableString
            * 对应的内容值
        * BeautifulSoup
            * 表示的是一个文档的内容，可以把它当作一个tag对象
            * 一般我们可以用soup来表示
        * Comment 注释
            * 特殊类型的NavagableString对象
            * 对其输出，则内容不包括注释符号
        * 遍历文档对象
            * contents：tag的子节点以列表的方式给出
            * children：子节点以迭代器形式放回
            * descendants：所有的子孙节点
            * string：输出节点内容
        * 搜索文档对象
            * find_all(name,attrs,recursive,text,** kwargs)
                * name :按照指定的字符串进行搜索，可以传入内容为
                    * 字符串
                    * 正则表达式
                    * 列表
                * kwargs：可以用来表示属性
                * text：对应tag的文本值
        * CSS选择器 对于网页的内容爬取，更友好
            * 使用的是soup.select，返回一个列表
            * 可以通过标签名：soup.select("class")
            * 也可以通过类名：soup.select(".content")
            * 通过标签ID进行查找：soup.select("#name_id") name_id 表示标签ID
            * 通过属性查找：soup.select("img[class='xxxx']") 查找img标签，class=xxx的
            * 组合查找：soup.select("div #input_content") 表示查找DIV，并且ID=input_content
            * 获取tag内容：tag.get_text 获取指定标签的值
            * 重点案例：spider-bs4-css-case10.py
            