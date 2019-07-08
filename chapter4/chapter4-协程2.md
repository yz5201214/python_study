#协程
#<这一节课不是很明白>
* asyncio
    * python3.4开始引入标准库当中，内置对异步io的支持
    * asyncio本身是一个消息循环 案例case05.py
        * 步骤：
            * 创建消息循环
            * 将协程导入
            * 关闭
* asyncio and await
    * 为了更好的表示异步io 
    * python3.5引入
    * 让协程代码更简洁
    * 使用上，可以简单的对协程进行替换
        * 用async替换@asyncio.coroutine
        * await 替换 yield from

* aiohttp 
    * 案例case06.py
    * asyncio 实现了单线程的并发io，在客户端用处不大
    * 主要用途在服务器端可以asyncio+coroutine配合，因为http是io操作
    * asyncio实现了tcp，udp，ssl等协议
    * aiohttp是给予asyncio实现的http框架
    * pip install aiohttp安装
* concurrent.futures
    * 案例case07.py
    * python3新增的库
    * 类似其他语言的线程池的概念
    * 利用multiprocessiong 实现真正的并行计算
    * 核心原理：以子进程的形式，并行运行多个python解释器，从而令python程序可以利用多核CPU来提升执行速度。由于子进程与主解释器分离，所以他们的全局解释器锁也是相互独立的。每个子进程都能够完整的使用一个cpu内核
    * concurrent.futures.Executor
        * ThreadPollExecutor
        * ProcessPollExecutor
        * 执行的时候需要自行选择
    * submit(fn.args,kwargs)
        * fn:异步执行的函数
        * args,kwargs参数
* current中map函数
    * 案例 case07.py
    * map(fn,\*iterables,timeout=None)
    * 跟map函数类似
    * 函数需要异步执行
    * timeout：超时时间
    * map跟submit使用一个就行
* future
    * 一个比方：A的同学B三分钟后来家里做客，A想送一条烟给B作为礼物，但是A手上并没有一条烟。于是A让C去帮忙买一条烟
        购买的时间大概是30分钟，没办法，A在等待B来的时候，拿了一个空盒子给B看，并且告诉B，这是送给你的一条烟，并且
        告诉B，这个时候不能拆，不能抽。回家才能拆，抽。所以A和B继续吹逼一个小时。在吹逼的过程中，C将一条烟买了回来
        并且将这一条烟替换了空盒子。1个小时后，C离开，并且带走了真正购买回来的香烟
    * 重点是：A知道B要过来的同时，通知C去购买香烟，并且A与B愉快的度过一个小时，同时香烟也购买回来了。并没有耽误吹逼
    * 其中用来展示gneoup