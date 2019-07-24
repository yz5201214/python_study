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
    * Selenium：web自动化测试工具，可以操作浏览器
        * 官方中文文档：https://selenium-python-zh.readthedocs.io/en/latest/
        * 自动加载页面
        * 获取数据
        * 截屏
    * Selenium 库有一个WebDriver的API
        * WebDriver可以跟浏览器页面上的元素进行各种交互，用他可以进行内容爬取
        * 案例：spider-dhtml-case11.py
        