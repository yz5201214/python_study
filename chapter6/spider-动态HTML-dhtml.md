# 动态HTML
* 爬虫跟反爬虫
    * 实际上大部分的手机端的网站，一般反爬虫的机制比较少。PC端的会比较多
* 动态HTML介绍
    * JavaScript生成内容
    * jQuery
    * Ajax 异步动态加载
    * DHTML
* Python采集动态数据
    * 从JavaScript代码入手采集
        * 查看数据是否是通过js脚本请求而来
        * Python第三方库运行JavaScript，直接采集你再浏览器看到的页面
* Selenium + Chrome/FireFox
    * 安装Chrome，下载与机器上安装的chrom浏览器对应版本的chromeDrver，将下载的文件拷贝到相应编译器的目录内即刻
        或者配置相应的环境变量，安装对应的环境包也可以
    * Selenium：web自动化测试工具，可以操作浏览器
        * 官方中文文档：https://selenium-python-zh.readthedocs.io/en/latest/
        * 自动加载页面
        * 获取数据
        * 截屏
    * Selenium 库有一个WebDriver的API
        * WebDriver可以跟浏览器页面上的元素进行各种交互，用他可以进行内容爬取
        * 案例：spider-dhtml-case11.py
    * Selenium 的主要操作
        * 得到指定UI元素
            * find_element_by_id：根据元素的ID，有点像原始的document.getElementByid
            * find_elements_by_name 名称
            * find_elements_by_xpath 
            * find_elements_by_link_text
            * find_elements_by_partial_link_text
            * find_elements_by_tag_name
            * find_elements_by_class_name
            * find_elements_by_css_selector
        * 基于得到的UI元素进行模拟操作
            * 单击
            * 右键
            * 拖拽
            * 输入
            * 可以通过导入ActionsChains类来实现
        * 参考案例：spider-dhtml-case11.py
        * 因为如果多开浏览器会对机器性能造成很大影响，所以如果需要针对多网站的数据爬取，最好不要使用浏览器，如果是单网站操作，可以采用模拟浏览器模式
        