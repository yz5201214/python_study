#Client
import socket,time

# 注意两个参数的意义
skt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def clientFunc():
    # 消息一旦推送，自动绑定
    msg = '这是第三条消息'
    skt.sendto(msg.encode('UTF-8'),('127.0.0.1',23306))
    data ,resAddr = skt.recvfrom(500)
    print(resAddr)
    print(data.decode('UTF-8'))

if __name__ == '__main__':
    print('clientStart-------------')
    clientFunc()
    print('clientEnd-------------')