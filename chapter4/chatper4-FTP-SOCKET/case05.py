# tcp client
import socket,time

def clientFunc(i):
    # 建立sockt，注意第二个参数与UDP链接的不一样
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 服务端IP，端口
    addr = ('127.1.0.1', 23306)
    # 建立连接关系
    # 特别注意，这里是连接关系
    skt.connect(addr)
    skt.send(("我的第"+i+"条TCP消息").encode())
    # 注意接收的关键字写法
    msg = skt.recv(500)
    print(msg.decode())
    skt.close()

if __name__ == '__main__':
    for i in range(10,20):
        clientFunc(str(i))
