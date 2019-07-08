#正则表达式(RegularExpression,re)
    * 不同平台，不同开发语言，共享一套正则表达式
    * 学习更多的是为了爬虫
    * 是一个计算机科学的概念
    * 用于使用单个字符串来描述，匹配符合某个规则的字符串
    * 常常用来检索，替换某些模式的文本
* 正则的写法
    * 实际上是用一段特殊的字符，用来描述长字符串的规律 
    * https://www.runoob.com/regexp/regexp-syntax.html
* 正则表达式的python写法 基本与java一致
    * python大致步骤
        * 使用compile将表示正则的字符串编译成一个pattern对象
        * 通过pattern对象提供一系列方法对文本进行查找匹配，或者皮结果，一个Match对象
        * 最后使用Match对象提供的属性和方法获得信息，根据需要进行操作
    * RE使用大致步骤 case01.py
        * group()：获得一个或者多个风阻匹配的字符串，当要获得整个匹配的子串时，直接使用group或者group(0)
        * start：获取分组匹配的字符串在整个字符串中的真实位置，参数默认0
        * end：获取分组匹配的字符串在整个字符串中结束的位置，默认0
        * span：返回的结构技术(start(group),end(group))
        * search(str,[, pos[, endpos]])：在字符串中查找匹配，pos和endpos表示起止位置
            * findall：查找所有
            * finditer：查找，返回一个iter结果
        * sub 替换
            * sub(rep1,str[, count])
        * 匹配中文
            * 大部分中文内容表示范围是[u4e00-u9fa5]，不包括全角标点
        * 贪婪和非贪婪
            * 贪婪：尽可能多的匹配，(*)表示贪婪匹配
            * 非贪婪：找到符合条件的最小内容即可，(?)表示非贪婪
            * 正则默认贪婪模式
        
     