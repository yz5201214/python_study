# 注意邮件模块
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
# 发送的email地址
from_addr = '120821884@qq.com'
# 这里是授权码，并不是登陆密码
from_pwd = 'cqowfcbnqcpybhdd'
# smtp服务器地址，这里不同的邮件服务商，地址不一样
smtp_srv = 'smtp.qq.com'
# 这里注意smtp_srv 实际上传入的bytes格式
# 465是默认访问安全的smtp端口
srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)# smtp协议默认的端口是25


# 下面是纯文本邮件
def mailSend(to_addr):
    msg = MIMEText('测试python邮件','plain','utf-8')
    # 接收人的email地址
    # 用指定的邮箱，向需要接受邮件的邮箱发送指定的内容
    try:
        # 如果确定完全没问题，实际不需要放入try
        # 登陆邮箱
        srv.login(from_addr, from_pwd)
        srv.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as e:
        print(e)
    srv.quit()
# 这里是带HTML格式的邮件
def mailHtmlSend(to_addr):
    mail_content = """
                <!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="utf-8">
                    <title>Title</title>
                </head>
                <body>
                    <h1>这里是一封HTML格式邮件</h1>
                </body>
                </html>
        """
    # 注意这里的参数，表示邮件内容是HTML格式
    msg = MIMEText(mail_content,"html","utf-8")
    try:
        # 如果确定完全没问题，实际不需要放入try
        # 登陆邮箱
        srv.login(from_addr, from_pwd)
        srv.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as e:
        print(e)
    srv.quit()
# 附件邮件发送
def sendFileMail(to_addr):
    # 附件邮件模块
    maile_mul = MIMEMultipart()
    # 附件邮件的文字描述
    maile_text = MIMEText('这是一个附件邮件','plain','utf-8')
    # 将文字附加进去
    maile_mul.attach(maile_text)
    # 打开一个附件文件
    with open('附件1.txt','rb') as f:
        s = f.read()
        #设置附件的MIME和文件名，必须要base64编码
        m = MIMEText(s,'base64','utf-8')
        #
        m["Content-Type"] = "application/octet-stream"
        # 附件名称为中文时的写法
        m.add_header("Content-Disposition", "attachment", filename=("utf-8", "", "测试中文名称.txt"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        maile_mul.attach(m)
        try:
            # 如果确定完全没问题，实际不需要放入try
            # 登陆邮箱
            srv.login(from_addr, from_pwd)
            srv.sendmail(from_addr, [to_addr], maile_mul.as_string())
        except Exception as e:
            print(e)
        srv.quit()
# 设置邮件头，邮件其他内容
def sendMailOhterInfo(to_addr):
    msg = MIMEText('测试python邮件', 'plain', 'utf-8')
    # 接收人的email地址
    # 用指定的邮箱，向需要接受邮件的邮箱发送指定的内容
    # 这里设置邮件发送者的信息
    heard_from = Header('从我的QQ邮箱发出去<120821884@qq.com>','utf-8')
    msg['From'] =heard_from
    # 设置邮件接受者的信息 这里会出现乱码问题
    heard_to = Header('发送到我的163的邮箱里面<yz120821884@163.com>','utf-8')
    msg['To'] = heard_to
    # 这里是设置邮件的主题
    heard_sub = Header('啊我的python邮件主题', 'utf-8')
    msg['Subject'] = heard_sub
    try:
        # 如果确定完全没问题，实际不需要放入try
        # 登陆邮箱
        srv.login(from_addr, from_pwd)
        srv.sendmail(from_addr, [to_addr], msg.as_string())
    except Exception as e:
        print(e)
    srv.quit()

# HMTL和TXT结合文件，但是好像内容不对
def sendHtmlTextMail(to_addr):
    maile_mul = MIMEMultipart("alternative")
    msg = MIMEText('测试python邮件', 'plain', 'utf-8')
    mail_content = """
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                        <meta charset="utf-8">
                        <title>Title</title>
                    </head>
                    <body>
                        <h1>这里是一封HTML格式邮件</h1>
                    </body>
                    </html>
            """
    msgHtml = MIMEText(mail_content, "html", "utf-8")
    maile_mul.attach(msg)
    maile_mul.attach(msgHtml)
    try:
        # 如果确定完全没问题，实际不需要放入try
        # 登陆邮箱
        srv.login(from_addr, from_pwd)
        srv.sendmail(from_addr, [to_addr], maile_mul.as_string())
    except Exception as e:
        print(e)
    srv.quit()

if __name__ == '__main__':
    sendAddr = 'yz120821884@163.com'
    # mailSend(sendAddr);
    # mailHtmlSend(sendAddr)
    #sendFileMail(sendAddr)
    # sendMailOhterInfo(sendAddr)
    sendHtmlTextMail(sendAddr)