import threading
# 导入异步IO的包
import asyncio
# 使用协程
@asyncio.coroutine
def hello():
    print('hello word! %s' % threading.currentThread())
    print('start.......... %s' % threading.currentThread())
    yield from asyncio.sleep(5)
    print('end.......... %s' % threading.currentThread())
    print('hello agein !.......... %s' % threading.currentThread())
# 以上简洁，替换写法
'''
注意，里面替换的内容，以及async的使用，和头的去除
'''
async def hello01():
    print('hello word! %s' % threading.currentThread())
    print('start.......... %s' % threading.currentThread())
    await asyncio.sleep(5)
    print('end.......... %s' % threading.currentThread())
    print('hello agein !.......... %s' % threading.currentThread())


@asyncio.coroutine
def test01(host):
    print('host is %s' % host)
    # 异步请求网络地址
    connect = asyncio.open_connection(host,80)
    # 注意这里的yidle from 写法
    reader ,writer = yield  from connect
    header = 'GET / HTTP/1.0\r/\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        # http协议下换换个使用
        if line == b'\r\n':
            break
        print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
    writer.close()

if __name__ == '__main__':
    # 启动消息循环
    loop = asyncio.get_event_loop()
    # 定义任务
    # tasks = [hello(),hello()]
    tasks = [test01(host) for host in ['www.baidu.com','www.sina.com.cn']]
    # asyncio 使用wait等待task
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

