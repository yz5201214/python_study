# scrapy框架
* 爬虫框架
    * scrapy
        * https://doc.scrapy.org/en/latest/
        * 安装教程：http://www.scrapyd.cn/doc/124.html
        * 建议使用pip install Scrapy 安装
        * 官网：https://scrapy.org
        * 主要部件
            * ScrapyEngine：神经中枢，大脑，核心
            * Scheduler：调度器，引擎发出来的request请求，调度器需要处理，然后交换引擎
            * Downloader：下载器，将引擎发送来的requests发出请求，得到response
            * Spider：爬虫，负责将下载器得到的内容/结果进行分解，分解成我们需要的数据+后续请求链接
            * ItemPipeline：管道，详细处理Item
            * DownloaderMiddleware：下载中间件，自定义下载的功能扩展组件，主要是对下载器进行扩展，类似于请求伪装
            * SpiderMiddleware：爬虫中间件 
        * 爬虫项目大概流程：
            * 新建项目：scrapy startproject xxxx
            * 明确爬取目标/产出：编写item.py
            * 制作爬虫：地址 spider/xxspider.py
            * 存储内容：piplines.py       
    * pyspider
    * crawley