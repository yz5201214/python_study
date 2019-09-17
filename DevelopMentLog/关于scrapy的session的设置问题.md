# scrapy 中请求的session设置问题
* 参考内容：https://blog.csdn.net/fuck487/article/details/84617194
    * spider中设置的cookies在piplines管道中的文件下载请求中，并不生效
    * 意味着如果在piplines管道中进行文件下载的时候，重写了get_media_requests方法，需要在scrapy.Request请求中，重新设置cookies
    

