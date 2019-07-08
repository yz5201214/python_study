# tpc server
import socket
def tcp_ser():
    # 建立sockt，注意第二个参数与UDP链接的不一样
    skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 服务端IP，端口
    addr = ('127.1.0.1',23306)
    # 建立绑定关系b
    skt.bind(addr)
    # 监听接入的访问sockt
    skt.listen()
    while True:
        # 接收访问的socket，可以理解接收访问即建立了一个通讯的链接通路
        # accept返回的元祖
        clientP,resAdd = skt.accept()
        # 接收对方的发送消息，利用接收到的socket接收内容
        # recvfrom 是UDP的用法，TCP注意要用recv
        msg = clientP.recv(500)
        # 接收到的内容也是bytes数据流格式
        print('接收到的内容是:{0}，来自：{1}'.format(msg.decode(),resAdd))
        # 返回内容
        clientP.send('接收成功'.encode())
        # 因为这里是监听事件，所以每次客户端连接进来后，执行完所有的过程，都需要关闭客户端连接
        clientP.close()
if __name__ == '__main__':
    tcp_ser()
