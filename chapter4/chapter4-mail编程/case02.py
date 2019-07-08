# 接收邮件
import poplib
# 接收邮件的包
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

#获取最新邮件，获取最新邮件的整体结构
def getMsg():
    email = '120821884@qq.com'
    email_pwd = 'cqowfcbnqcpybhdd'
    pop3_srv = 'pop.qq.com'
    # ssl代表安全通道
    srv = poplib.POP3_SSL(pop3_srv)
    # 获取邮件的账号，密码
    srv.user(email)
    srv.pass_(email_pwd)
    # 返回一个tuple格式
    # 返回邮件的数量和占用空间
    msgs,counts = srv.stat()
    print('msg------>{0},count-------->{1}'.format(msgs,counts))
    # list返回所有邮件编号列表
    # mails是所有邮件编号列表
    rsp,mails,octets = srv.list()
    # 获取最新一封邮件，注意，邮件的索引号是从1开始，最新代表索引号最高
    index = len(mails)
    # retr 负责返回一个具体索引号的一封信的内容，内容不具有可读性
    # lines 存储与偶见的最原始文本的每一行
    rsps,lines,octetss = srv.retr(index)
    # 获取整个邮件的原始文本
    msg_count = b'\r\n'.join(lines).decode('utf-8')
    # 解析处邮件整体结构体
    # 参数是解码后的邮件整体
    msg = Parser().parsestr(msg_count)
    srv.quit()
    return msg;

if __name__ == '__main__':
    getMsg()
