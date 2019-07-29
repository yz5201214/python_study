# 创建一个Scrrapy项目
* 环境
    * windows + anaconda + pycharm
    * 首先安装scrapy，conda Scrapy
    * 然后命令行进入workspace目录，运行：scrapy startproject 项目名称，在workspace中就会自动创建一个scrapy框架的项目
        * 错误日志记录：
            * 如果新环境，导入scrapy框架的spider项目，如果出现scrapy包无法导入，且在anaconda已经安装scrapy的情况下，需要
                重新设置项目的解释器，但是选择anaconda后，发现还是无法找到scrapy包的情况下，参考帖子：https://blog.csdn.net/neverstopforcode/article/details/79868234
    * 然后运行pycharm 打开项目，在spiders中创建你需要的spider.py文件
        * 在spider.py中进行数据爬取，分析，以及传入下一个爬取页面。主要方法有：
            * start_request：可以不写，有两种连接初始化方法
            * parse：网页内容解析，必须有
    * 如果在不知道解析格式的情况下，可以进行调试：调试语句：scrapy shell 调试网页，然后在命令行输入相应的解析语句即可看到返回结果集
    * 运行spider程序命令：scrapy crawl 爬虫名称
    
    * spider入库教程：
        * 参考：http://www.scrapyd.cn/jiaocheng/169.html
    