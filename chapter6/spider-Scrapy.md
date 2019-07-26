# scrapy框架
* 爬虫框架
    * scrapy
        * https://doc.scrapy.org/en/latest/
        * 中文文档：https://scrapy-chs.readthedocs.io/zh_CN/0.24/
        * 安装教程+中文教程：http://www.scrapyd.cn/doc/124.html
        * 建议使用pip install Scrapy 安 装
        * 官网：https://scrapy.org
        * 主要部件
            * ScrapyEngine：神经中枢，大脑，核心
            * Scheduler：调度器，引擎发出来的request请求，调度器需要处理，然后交换引擎
            * Downloader：下载器，将引擎发送来的requests发出请求，得到response
            * Spider：爬虫，负责将下载器得到的内容/结果进行分解，分解成我们需要的数据+后续请求链接
                * 对应的是spiders下的文件
                * __init__：初始化爬虫名称，start_urls列表
                * start_requests：生产Requests对象提交给Scrapy下载器返回response
                * pares：根据返回的response解析出相应的item，item自动进入pipline，同时需要，可以解析出url，自动进入requests模块
                    ，一直循环到后续的url为空为止
                * start_request：此方法仅能被调用一次，读取start_url内容并且启动循环过程
                * name：设置spider名称
                * start_url：设置开启位置的url
                * allow_domains：spider允许爬取的域名，不设置则不论域名是否符合都爬取
                * pares：解析spider返回的response
                * log：记录日志
                
            * ItemPipeline：管道，详细处理Item
                * 对应的piplines文件
                * 爬虫提取出数据存入item后，item中保存的数据需要进一步处理，比如清晰，去重，存储等
                * 所有注册的pipeline必须全部执行并且处理
                * pipeline可以注册多个，有执行顺序
                * pipeline需要处理process_item函数
                    * 常见函数
                    * process_item：spider提出出来的item作为参数传入，同事传入的还有spider
                    * 此方法必须实现
                        * 必须返回一个Item对象，被丢弃的item不会被之后的pipeline处理
                * init：构造函数
                    * 不是必须初始化，根据项目实际情况处理
                    * 进行一些必要的参数初始化
                * open_spider(spider)：
                    * spider对象被开启的时候调用
                * close_spider(spider)：
                    * 当spider关闭的时候调用
                    
            * DownloaderMiddleware：下载中间件，自定义下载的功能扩展组件，主要是对下载器进行扩展，类似于请求伪装
                * 请求，反馈都可以经过中间件处理，处于引擎和下载器中间的一个组建
                * 可以有多个，按照指定顺序进行加载执行
                * 请求身份的伪装，反馈内容的初步内容过滤，预处理
                * 在middlewares.py文件中
                * 需要在setting.xml中进行设置生效
                * 一般一个中间件完成一项功能，提升代码的可读性
                    * 必须实现以下一个或者多个方法
                        * process_request(self, request, spider)
                            * 在request通过的时候被调用
                            * 必须返回None或Response或Request或raise IgnoreRequest
                            * None：scrapy将继续处理该request
                            * Request：scrapy会停止调用process_request并重新调度返回的request
                            * Response：scrapy将不会调用其他的process_request或者process_excepition，直接将该response作为结果，同时
                                会调用process_response函数，将返回的response作为参数传入
                        * process_response(self, request,response, spider)
                            * 跟process_request大同小异
                            * 每次有返回结果的时候会自动调用
                            * 可以有多个，按照指定顺序调用
                
            * SpiderMiddleware：爬虫中间件
        * 爬虫项目大概流程：
            * 新建项目：scrapy startproject xxxx
            * 明确爬取目标/产出：编写item.py
            * 制作爬虫：地址 spider/xxspider.py
            * 存储内容：piplines.py       
    * pyspider
    * crawley
    * 案例创建新项目
* 去重
    * 为了防止spider陷入死循环，需要去重
    * 即在spider中的parse函数中，返回Request的时候加上dongt_filter=False参数
        * myspeder(scrapy.Spider):
            def parse(...........):
                .........
                yield scrapy.Request(url=url, callback=self.parse, dont_filter=False) //去掉重复的URL
    * 如何在scrapy使用selenium
        * 使用浏览器太过于消耗服务器性能，如果不需要使用，尽可能不适用
        * 可以将selenium放入中间件中的process_request函数中
        * 流程是：请求在通过DownloaderMiddleware中间件的时候，不使用Downloader，直接使用selenium模拟浏览器爬去，然后返回response
        * 案例代码如下:
            class MyMiddleWare(object):
                def process_request(...):
                    # 使用selenium 模拟浏览器登录爬取内容
                    driver = webdriver.Chrom()
                    html = driver.page_source
                    driver.quit()
                    return HtmlResponse(url=request.url, encoding='utf-8', body = html, request=request)
* shell
    * 参考文档：https://segmentfault.com/a/1190000013199636?utm_source=tag-newest
    * windows下的PowerShell：命令模式下输入：PowerShell 进入PowerShell，即命令行终端模式
    * 目前我基本用不到

* 分布式爬虫
    * 单机爬虫的问题
        * 单机效率问题
        * IO吞吐量
    * 多爬虫的问题
        * 数据共享问题，主要是cookie等共享问题
        * 在空间上不同的多台机器，可以称为分布式 
    * 分部署爬虫说明
        * 共享队列
        * 队列去重
            * Redis-内存数据库，也可以保存到硬盘，可以去重，集成了dict，set，list的集合体
        * scrapy使用的请求队列可以在setting.xml进行配置
        * 保存到数据库
            * MongoDB
            * MySql
    * 安装scrapy_redisreadthedocs
        * pip install scrapy_redis
        * github.com/rolando/scrapy-redis
        * 参考文档：https://www.cnblogs.com/pythoner6833/p/9148937.html
    * 爬虫推荐书籍：
        * Python爬虫开发于项目实战，范传辉，机械工业出版社
        * 精通Python爬虫框架Scrpay，李斌翻译，人民邮电出版社         