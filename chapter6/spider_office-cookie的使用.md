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