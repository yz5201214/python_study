#HTTP协议
* 超文本
    * 包含超链接(Link)和各种多媒体元素标记(MarkUp)的文本。最常见的超文本格式是HTML        
* URL
    * URL即统一的资源定位符(Uniform Resource Locator),用来唯一的表示万维网中的某一个文档
* HTTP
    * 是一种按照URL指示，将超文本文档从一台主机(服务器)传输到另外一个主机的应用层协议
* HTTP工作原理
    * 请求/响应模型
    * 连接方式
        * 持久连接
            * 即在一个连接中，可以进行多次文档的亲切感求和响应。第一次请求完成后，服务与客户并不释放连接
        * 非持久连接
            * 每请求一个连接，请求传输完成后，立即释放连接
    * 无状态性
        * 是指同一个客户端第二次访问统一个web服务器上的页面，服务器无法知道这个客户曾经访问过。HTTP的无状态性简化了服务器的设计。能够支持更大的并发
* HTTP报文结构
    * 请求报文
        * 请求地址
        * 请求报文头
        * 请求报文主体
    * 返回报文
        * 状态行
        * 返回报文头
        * 返回报文主体
    * 请求报文中的方法
        * GET 请求读取
        * POST 附加一个命名资源(如WEB页面)
        * DELETE 删除WEB页面 
        * CONNECT 用于代理服务器
         
        * HEAD 请求读取一个web页面的首部
        * PUT 请求存储一个web页面
        * TRACE 用于测试，要求服务器返回收到的请求
        * OPTION 查询特定选项
    * 响应报文中的状态码
        * 1xx 通知成功
        * 2xx 成功
        * 3xx 重定向
        * 4xx 客户错误
        * 5xx 服务端错误
    * 首部字段或消息头
        * User-Agent 关于浏览器和他平台的信息
        * Accept 客户能处理的页面类型
        * Accept-Charset 客户能够接受的字符集
        * Accept-Encoding 客户能处理的页面编码方法
        * Accept-Language 客户能处理的自然语言
        * Host 服务器的DNS名称，从URL中提取出来，必须
        * Authorization 客户的信息凭据列表
        * Cookie 将以前设置的Cookie送回服务器
        * Date 请求的时间
        * Server 关于服务器的信息
        * Content-Encoding 内容是如何被编码的
        * Content-Language 页面所使用的自然语言
        * Content-length 以字节计算的页面长度
        * Content-Type 页面的MIME类型
        * Last-Modifind 页面最后被修改的时间日期
        * Location 只是客户讲消息发送给别处，重定向到另外一个URL
        * Set-Cookie 服务器希望客户保存另外一个Cookie
    * 报文结构实例
        * 自定义内容    
* HTTP代理
    * HTTP代理是WEB缓存或者代理服务器(Proxy Server)，是一种网络实体，能代表浏览器发送HTTP请求，并将最新的一些请求和响应暂存到本地
    磁盘中，当请求的web页面先前暂存过，则直接将暂存的页面发给客户端，无需再次访问Internet