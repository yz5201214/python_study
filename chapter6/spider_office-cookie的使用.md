# 请求中的使用cookie
* 在办公室的第一节
* 使用cookie登陆
    * 自动登陆
    * http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        * CookieJar
            * 管理存储cookie，向传出的http自动请求添加cookie
            * cookie存储在内存中，cookieJar实例回收后cookie则销毁
        * FileCookieJar(filename,delayload=None,policy=None)
            * 使用文件管理cookie
            * filename是保存cookie的文件
        * MozillaCookieJar(filename,delayload=None,policy=None)
            * 创建与mocilla浏览器cookie.txt兼容的fileCookieJar实例
        * LwpCookieJar(filename,delayload=None,policy=None)
            * 创建与libwww-per标准兼容的Set-Cookie3格式的FileCookieJar实例
        * 衍生关系是：CookieJar --> FileCookieJar --> MozillaCookieJar --> LwpCookieJar
    * 利用cookiejar访问 案例case01.py
        * 自动使用cookie登录，大概流程是：
            * 打开登录页面后，自动通过用户名/密码登录
            * 自动获取反馈回来的cookie
            * 利用提取的cookie直接打开隐私网页
    * handle是Handle的实例，常用的有：
        * cookie管理器 # cookie 实例 cookie = cookiejar.CookieJar()  # cookie管理器 cookie_Headle = request.HTTPCookieProcessor(cookie)
        * http请求管理器 request.HTTPHandler()
        * https请求管理器 request.HTTPSHandler()
    * 创建handle后，使用open而打开，打开后相应的业务由相应的hanlder处理    
        * * 实际请求管理器 oper = request.build_opener(http_Headle,https_Headle,cookie_Headle)
    * cookie可以在代码中获取到，并且重复使用，如果不获取，则会在管理器的生命周期结束后自动销毁  案例case01.py
        * cookie属性 ，cookie信息是不能修改的，只能够用来解读或者查看分析
            * name：名称
            * value：值
            * domain：可以访问此cookie的域名
            * path：可以访问此cookie的页面路径
            * expires：cookie的过期时间
            * size：cookie的大小
            * http字段
    * 使用fileCookie来进行cookie管理 案例case02.py
    