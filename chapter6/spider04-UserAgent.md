#用户代理
* UserAgent
    * 用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者身份
    * 常见的UA值，使用的时候可以直接赋值粘贴，也可以用浏览器访问的时候抓包
    * 设置UA可以通过两种方式
        * heads
        * add_header
* ProxyHandler处理(代理服务器)
    * 使用代理IP，是爬虫的常用手段
    * 常用的公用代理服务器
        * www.xicidaili.com
        * www.goubanjia.com
    * 代理的主要作用就是为了伪装机器地址，防止访问的网站进行IP限制，所以代理一定要多~一定的周期更换代理
        * 设置代理地址
        * 创建PrxoyHandler
        * 创建opener
        * 安装opener
* cookie 和 session
    * 由于http协议的无记忆性，人们弥补这个问题，所采用的异步补充协议
    * cookie是发给用户的一段信息，存储在浏览器中。session是保存在服务器上的对应的另外一部分信息，用来记录用户信息
    * 区别
        * cookie存储用户本地，session是存储在请求对象的服务器上
            * session是有有效期的，cookie同样也有有效期
        * 单个cookie保存的数据不超过4K，很多浏览器限制一个站点最多保存20个
        * session的存储一般在服务器上有专门的存放位置，比如数据库，比如redis等
    