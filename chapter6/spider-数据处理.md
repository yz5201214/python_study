# 爬虫网站数据处理
* 结构数据
    * 先构建结构，再填充数据
        * JSON格式
            * JSON Path
            * 转换成Python类型进行操作（json类）
        * XML格式
            * 可以转换成Python类型（xmltodict）
            * XPath
            * CSS选择器
            * 正则表达式
* 非结构化数据
    * 先有数据，再衍生出结构
        * 文本，电话号码，邮箱地址等，没有规则
            * 通常处理这种数据，使用正则表达式来进行局部规则匹配
        * Html文件
            * 正则
            * XPath
            * CSS选择器
* 正则表达式
    * 一套规则，对字符串按照指定的规则查找内容
    * Python正则模块，re
        * match: 从开始的位置查找，一次匹配
        * search：从任何位置查找，一次匹配
        * findall：全部匹配，返回列表
        * finditer：全部匹配，返回迭代器，需要循环处理，基本findall一致
        * split：分割字符串，返回列表
        * sub：替换
    * 匹配中文
        * 中文unicode范围主要在[u4e00-u9fa5]，注意是主要，不是全部
    * 贪婪
        * 在整个表达his匹配成功的前提下，尽可能多的匹配
    * 非贪婪
        * 尽可能少的匹配
    * Python默认的是贪婪模式
    * 正则一些案例参考：spider-regularExpression-case06.py
* XML
    * 参考前面基础知识
    * XPath（XML Path Language）是一门在XML稳定中查找信息的语言
        * 重点参考官方文档：http://www.w3school.com.cn/xpath/index.asp
        * XPath表达式工具：XMLQuire
        * chrom插件：XPath Helper

* lxml库
    * python的HTML/XML的解析器
        * 官方文档: https://lxml.de/index.html
        * 案例：spider-lxml-case08.py
    * etree
        * 解析HTML
        * 文件读取只能读取XML文件，不能读取HTML文件
    