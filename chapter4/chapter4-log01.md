# LOG
* [Python的LOG详解](https://www.cnblogs.com/yyds/p/6901864.html)
* 以下所有讲解，基本是基于上面这个帖子
* logging
    * logging 模块提供模块级别的函数记录日志
    * 包括四大组件
* 日志的相关概念
    * 日志实际就是程序运行过程中的记录
    * 日志不需要大量记录，只需要记录关键信息，程序异常关键点，运行过程关键数据等
    * 日志级别（level）
        * 不同用户关注的的信息类别不一样
            * DEBUG 调试日志
            * INFO  基本日志
            * NOTICE 通知日志
            * WARNING 警告日志
            * ERROR 错误日志
            * CRITICAL 严重错误日志
            * ALERT 日常后追加日志
            * EMERGENCY 
    * IO操作不需要太过频繁
* LOG的作用
    * 调试
    * 了解软件的运行情况
    * 分析定位问题
* 日志信息
    * 时间 time
    * 位置 address
    * 级别level
    * 内容描述，尽量简单明了
* python有成熟的第三方模块
    * log4j
    * log4php
    * loging
* loggin模块
    * 级别定义
        * 级别可以自定义 ，DEBUG,INFO,WARNING,ERROR,CRITICAL
    * 初始化/写入日志的时候，需要定义级别
    * python的日志使用的是单例模式
    * 使用方式
        * 直接使用loging(封装了其他的组件)
        * Loging四大组件直接定制
    * logging模块级别的日志
        * logging.debug(msg, *args, **kwargs)	创建一条严重级别为DEBUG的日志记录
        * logging.info(msg, *args, **kwargs)	创建一条严重级别为INFO的日志记录
        * logging.warning(msg, *args, **kwargs)	创建一条严重级别为WARNING的日志记录
        * logging.error(msg, *args, **kwargs)	创建一条严重级别为ERROR的日志记录
        * logging.critical(msg, *args, **kwargs)	创建一条严重级别为CRITICAL的日志记录
        * logging.log(level, *args, **kwargs)	创建一条严重级别为level的日志记录
        * logging.basicConfig(**kwargs)	对root logger进行一次性配置
            * 只有第一次调用的时候起作用。
            * 不针对logging进行配置，则使用默认配置
                * 输出：sys.stderr.标准错误输出
                * 级别：warning.默认只到警告级别
                * 格式：level:log_name:content
            * format格式说明：
                * asctime	%(asctime)s	日志事件发生的时间--人类可读时间，如：2003-07-08 16:49:45,896
                * created	%(created)f	日志事件发生的时间--时间戳，就是当时调用time.time()函数返回的值
                * relativeCreated	%(relativeCreated)d	日志事件发生的时间相对于logging模块加载时间的相对毫秒数（目前还不知道干嘛用的）
                * msecs	%(msecs)d	日志事件发生事件的毫秒部分
                * levelname	%(levelname)s	该日志记录的文字形式的日志级别（'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'）
                * levelno	%(levelno)s	该日志记录的数字形式的日志级别（10, 20, 30, 40, 50）
                * name	%(name)s	所使用的日志器名称，默认是'root'，因为默认使用的是 rootLogger
                * message	%(message)s	日志记录的文本内容，通过 msg % args计算得到的
                * pathname	%(pathname)s	调用日志记录函数的源码文件的全路径
                * filename	%(filename)s	pathname的文件名部分，包含文件后缀
                * module	%(module)s	filename的名称部分，不包含后缀
                * lineno	%(lineno)d	调用日志记录函数的源代码所在的行号
                * funcName	%(funcName)s	调用日志记录函数的函数名
                * process	%(process)d	进程ID
                * processName	%(processName)s	进程名称，Python 3.1新增
                * thread	%(thread)d	线程ID
                * threadName	%(thread)s	线程名称
* logging模块的处理流程
    * 四大组件，生产，发送，分类，格式
        * 日志器(Logger)：产生日志的一个接口
            * 生产一个日志
            * 配置日志：
                * Logger.setLevel()	设置日志器将会处理的日志消息的最低严重级别
                * Logger.addHandler() 和 Logger.removeHandler()	为该logger对象添加 和 移除一个handler对象
                * Logger.addFilter() 和 Logger.removeFilter()	为该logger对象添加 和 移除一个filter对象
                * 创建日志：
                    * Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), Logger.critical()	创建一个与它们的方法名对应等级的日志记录
                    * Logger.exception()	创建一个类似于Logger.error()的日志消息
                    * Logger.log()	需要获取一个明确的日志level参数来创建一个日志记录
                * 如何得到一个logger对象
                    * 实例化
                    * logging.getLogger()               
        * 处理器(Handler)：把生成的日志发送到相应的目的地，可以根据日志的情况，需要，给不同的人或者目的地发送日志
            * 处理方法：
                * Handler.setLevel()	设置handler将会处理的日志消息的最低严重级别
                * Handler.setFormatter()	为handler设置一个格式器对象
                * Handler.addFilter() 和 Handler.removeFilter()	为handler添加 和 删除一个过滤器对象
            * 不需要直接使用，Handler是一个基类
                * logging.StreamHandler	将日志消息发送到输出到Stream，如std.out, std.err或任何file-like对象。
                * logging.FileHandler	将日志消息发送到磁盘文件，默认情况下文件大小会无限增长
                * logging.handlers.RotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按大小切割
                * logging.hanlders.TimedRotatingFileHandler	将日志消息发送到磁盘文件，并支持日志文件按时间切割
                * logging.handlers.HTTPHandler	将日志消息以GET或POST的方式发送给一个HTTP服务器
                * logging.handlers.SMTPHandler	将日志消息发送给一个指定的email地址
                * logging.NullHandler	该Handler实例会忽略error messages，通常被想使用logging的library开发者使用来避免'No handlers could be found for logger XXX'信息的出现。
        * 过滤器(Filter)：更精细的控制日志内容，给不同的人或者不同的目的地发送的内容需要进行不同的日志处理/过滤
            * 可以被Handler和Logger使用
            * 控制传递过来的信息的具体内容
        * 格式器(Formatter)：对输出的信息进行自定义的格式化
            * 直接实例化
            * 可以继承Format添加特殊内容
            * 三个参数：
                * fmt：指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
                * datefmt：指定日期格式字符串，如果不指定该参数则默认使用"%Y-%m-%d %H:%M:%S"
                * style：Python 3.2新增的参数，可取值为 '%', '{'和 '$'，如果不指定该参数则默认使用'%'
    