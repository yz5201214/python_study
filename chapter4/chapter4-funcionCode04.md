# 高级函数补充及调试
* zip 函数 案例：case01.py
    * 把两个可迭代内容生成一个可迭代的tuple元素类型组成的内容
* enumerate 模块
    * 跟zip功能比较像
    * 对可迭代对象的每一个元素，配上一个索引，然后索引和内容构成tuple类型
* collections 模块 
    * namedtuple 具体参考案例
        * tuple 类型，可扩展的tuple 
    * deque
        * 比较方便的解决了频繁删除，插入带来的效率问题
    * defauldict
        * 当世界读取dict不存在的属性时，直接返回默认值
    * Counter
        * 统计字符串个数
 
# python调试
* 调试技术
    * 调试流程：单元测试-》继承测试-》交付测试(测试部门)
    * 分类：
        * 静态调试
            * 自我检测代码
        * 动态调试
    * pdb调试
        * 了解，课程不讲
        * pdb：python调试库
    * pycharm调试 基本操作与java一致
        * run模式
            * 直接运行
        * debug模式
            * 断点逐步调试
        
    * 单元测试
        * 自己写测试用例，类似idear 中java直接写测试用例一样 
    