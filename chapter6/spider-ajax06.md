# ajax
* 特点
    * 一定会有url
    * 一般使用json格式参数
    * 案例，爬取豆瓣电影，案例：spider-ajax-case05.py
* Request-献给人类
    * HTTP for Humans，更简洁友好
    * 集成了urllib的所有特征
    * 底层使用的是urllib3
    * 第三方开源模块
    * 开源地址：https://github.com/kennethreitz/requests
    * 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
    * 参考：https://blog.csdn.net/qq_37616069/article/details/80376776
    * GET请求
        * requests.get(url)
        * requests.request("get",url)
        * 可以带有headers和parmas参数
        * 参考案例spider-requests-case06.py
    * POST请求
        * rsp = requests.post(url,data=data)
        * 参考案例spider-requests-case06.py
        * 特别注意的地方是：data，和headles是dict类型，并不需要转码处理
    * proxy
        * 代理
            proxies = {
                "http":"address of proxy for http" http的代理
                "https":"address of proxy for https" https的代理
            }
            rsp = requests.request("get",url,proxies = proxies) 使用代理
        * 代理有可能报错，如果使用的人多，考虑安全问题，有可能会被强行关闭，如果关闭了。需要切换代理
    * 用户验证问题
        * 代理验证
            * 可能需要使用HTTP basic Auth,可以如下
                格式为 用户名：密码@ 代理地址
                    proxy = {
                        "http":"china:1234546@192.168.1.123:8377"   
                    }
                    rsp = requests.request("get",url,proxies = proxies)
        * web客户端验证
            * 如果遇到web客户端验证，需要添加auth=(用户名，密码)
                    auth=("test1","123456") 授权信息
                    rsp = requests.request("get",url,auth = auth)
             
    * cookie
        * requests 可以自动处理cookie信息
            rsp = requests.get("www.baidu.com")
            如果这个时候服务器给传送过来的cookie信息，则可以通过反馈的cookie属性得到，cookiejar = rsp.cookies   
            返回的cookies信息是一个cookiejar实例
            如果希望查看cookie信息如下
                cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    * session
        * 跟服务器端的session不是一个东西，这个是客户端使用
        * 模拟一次会话，从客户端浏览器连接服务器开始，到客户端浏览器断开为止
        * 可以让客户端跨请求的时候保持一些参数，比如在同一个session实例发出的所有请求之间保持cookie
            创建session对象，可以保持cookie
            ss = requests.session()
            headers = {'User-Agent':'xxxxxxxx'}
            data = {'name':'xxxxxxxxx'}
            这个时候的请求不需要requests，直接使用session管理器，由session负责发出请求
            下面两个请求，使用的是同一个cookie
            ss.post(url,data = data,headers=headers)
            rsp = ss.get(url)
    * https 请求验证ssl证书
        * 由参数verify负责表示是否需要验证ssl安全证书，默认是True
            rsp = request.get('https://www.baidu.com',verify=False)
        * 如果启用类sll安全证书验证去访问没有ssl安全证书的url，会出现异常
* 实际requests最终使用还是urllib，只是做了比较好的封装，如果写爬虫程序，建议使用requests，使用方便，简洁
            
            