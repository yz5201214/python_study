# spider02 使用urlopen
* 包含模块
    * urllib.request：打开和读取urls
    * urllib.error：包含urllib.request产生的常见错误，使用try捕获
    * urllib.parse：包含解析url的方法
    * urllib.robotparse：解析robots.txt文件，类似于爬虫的规则配置文件
* 网页编码问题解决
    * chardet 可以自动检测网页页面文件的编码格式，但是可能有误
    * 需要安装，默认已经安装
* urlopen 的返回对象
    * 返回的对象是：HTTPResponse
    * 基本函数：
        * geturl：返回请求对象的url
        * info：请求反馈对象的meta信息
        * getcode：返回的http code请求状态
* request.data 的使用
    * 访问网络的两种方法
        * get
            * 实际上是利用参数给服务器传递信息
            * 参数为dict，然后用parse编码传输即可
        * post
            * 一般向服务器传递使用
            * post是将信息自动加密处理
            * python使用post传递参数，需要使用到urlopen中的data参数
            * 使用post，意味着http的请求头可能需要更改：
                * Content-Type:application/x-www.form-urlencode
                * Content-Length:数据长度
                * 一旦更改请求方式，请注意其他头部信息相适应
            * urllib.parse.urlencode可以将字符串自动转换成上面的格式
            * 以上请求过程发现，为了更多的设置请求信息，单纯通过urlopen函数已经不够了
                * 需要利用request.Request 类，用于模拟请求实体
                