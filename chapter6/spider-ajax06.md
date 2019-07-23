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