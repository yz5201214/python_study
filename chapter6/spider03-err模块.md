#urllib.error 
* URLError产生的原因
    * 没网
    * 服务器链接失败
    * 是OSError子类
    * 案例case02.py
* HTTPError，是URLError的一个子类

* 两者的区别
    * HTTPErroe是对应的http请求返回码错误，如果返回错误码是400以上的。则引发HTTPError
    * URLError对应的一半是网络出现情况，包括url问题
    * 关系区别：OSError-》URLError—》HTTPError
    