#XPath
* 在XML文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
* http://www.w3school.com.cn/xpath/index.asp
* XPath 开发工具
    * 开源的XPath表达式编辑工具：XMLQuire
    * Chrom插件：XPath Helper
    * Firefox插件：XPath Checker
* 选取节点
    * nodename：选取子节点的所有子节点
    * /{根节点名称}：从根节点开始选取
    * //{节点名称}：选取节点，不考虑位置，如果有多个，选择返回内容列表list
    * .：选取当前节点
    * ..：选取当前节点的父节点
    * @：选取属性
    * xpath中查找一般按照节点路径进行查找，以下是路径表示方法
        School/Teacher：返回Teacher节点
        School/Student：返回两个Student节点
        //Student：返回所有的Student的节点，不考虑位置
        School//Age：选取所有School子节点中，所有Age节点
        //@Other：选取Other属性，所有的Other
        //Age[@Detail]：选取带有属性的Detail的Age节点
    * 谓语：Predicates
        * /School/Student[1]：选取School下面多个Student中的第一个节点
        * /School/Student[last()]：选取School下面多个Student中的最后一个Student节点
        * /School/Student[last()-1]：选取School下面多个Student中的倒数第二个
        * /School/Student[last()<3]：选取School下面多个Student中的去前两个
        * //Student[@score]：选取带有属性score的Student节点
        * //Student[@score='99']：选取带有属性score的Student节点，并且属性score=99
        * //Student[@score]/Age：选取带有属性score的Student节点，继续查找他的子节点Age
    * XPath的一些操作
        * |：或者
            //Student[@score] | //Teacher：选取带有属性score的Student节点 和 Teacher节点
        * 其余不常见XPath运算符号包括：+，-，*等等
    