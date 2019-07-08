# Service
import socket

# 两个参数
# socket.AF_INET：使用的是IPV4协议族
# socket.SOCK_DGRAM：通讯方式UDP通信
# 建立socket
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 绑定IP和port，地址是一个tuple，(ip,port)
addr = ('127.0.0.1', 23306)
skt.bind(addr)
def serverFunc():
    # 接收消息，recvfrom接收的返回值是一个元祖，前一项表示数据，后一项表示地址
    # 参数的含义是缓冲区大小
    # rst = skt.recvfrom(500) 两种写法都行
    # 如果不写结束，会一直死等
    # 这里需要特别注意：data 是bytes数据流
    data,retAddr = skt.recvfrom(500)
    print(str(retAddr))
    print(data)
    # 数据流解码，指定UTF-8编码集
    print(data.decode('UTF-8'))
    # 给对方返回内容
    # 返回的内容也必须是bytes数据流
    rep = '这里是给回去的内容'
    repData = rep.encode('UTF-8')
    # sendto用的是UDP协议
    skt.sendto(repData,retAddr)
    # 结束socket服务
    # skt.close()
if __name__ == '__main__':
    print('sartServer--------')
    # 死都不关闭，简称常连接
    while True:
        serverFunc()
    print('endServer---------')