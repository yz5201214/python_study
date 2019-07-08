import logging
# 问题在于，每次如果都是输出的情况下，如果大型程序没法处理，并且资源消耗太大
def test01():
    color = ['red','blue','gree','yellow','black']
    for i in color:
        if i == 'red':
            print(i)

# 这里使用loggingging模块记录日志
# 控制台默认只能打印warning级别以上的日志
def test02():
    logging.debug("this is debug level logging")
    logging.info("this is info level logging")
    logging.warning("this is warning level logging")
    logging.error("this is error level logging")
    logging.critical("this is critical level logging")
    # 注意这里的写法
    logging.logging(logging.CRITICAL,"另外一种的日志写法")
    logging.logging(logging.ERROR, "另外一种的日志写法")
# 这里进行设置处理
# 日志的设置，只有第一次生效。后面的设置就不生效了
def test03():
    # filename 日志文件，可以设置目录
    # level 日志初始级别
    # format 自定义内容格式：asctime 时间，levelname级别，message内容，%()表示内容替换，这里要根据python的logging关键字来写
    logging_format = "%(asctime)s......%(levelname)s......%(message)s"
    logging.basicConfig(filename="test.logging",level=logging.DEBUG,format=logging_format)
    logging.debug("this is debug level logging")
    logging.info("this is info level logging")
    logging.warning("this is warning level logging")
    logging.error("this is error level logging")
    logging.critical("this is critical level logging")
# 日志案例：
# 1）要求将所有级别的所有日志都写入磁盘1）要求将所有级别的所有日志都写入磁盘文件中
# 2）all.logging文件中记录所有的日志信息，日志格式为：日期和时间 - 日志级别 - 日志信息
# 3）error.logging文件中单独记录error及以上级别的日志信息，日志格式为：日期和时间 - 日志级别 - 文件名[:行号] - 日志信息
# 4）要求all.logging在每天凌晨进行日志切割
import datetime
# 需要导入才能用.扩展出来
import logging.handlers
def test04():

    loger = logging.getLogger("yzlogging")
    loger.setLevel(logging.DEBUG)
    # 两个不同的日志文件，设置了不同的Handler，注意两种写法，第一种写法主要是凌晨进行日志切割，第二种写法是没有切割
    rf_handler = logging.handlers.TimedRotatingFileHandler('all.logging', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
    rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    f_handler = logging.FileHandler('error.log')
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
    # 为日志添加handler
    loger.addHandler(rf_handler)
    loger.addHandler(f_handler)
    # 然后产生日志
    loger.debug('debug message')
    loger.info('info message')
    loger.warning('warning message')
    loger.error('error message')
    loger.critical('critical message')
if __name__ == '__main__':
    test04()