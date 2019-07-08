#mail编程
* 参考资料
    https://docs.python.org/3/library/email.mime.html
* 邮件工作流程
    * MUA(MailUserAgent)邮件用户代理
    * MTA(MailTransferAgent)邮件传输代理
    * MDA(MailDeliveryAgent)邮件投递代理
    * 具体：
        * MUA->MTA
        * QQ的MTA--------->sina MTA，邮件通过传输代理
        * sina MTA--------> sina MDA，这个时候邮件已经在你邮箱里面
        * sina MDA-------->MUA(FoxMail/OutLook等工具)，邮件下载到本地
* 编写程序
    * 发送：MUA->MTA 使用SMTP协议，包含MTA->MTA
    * 接收：MDA->MUA 使用POP3 和 IMAP协议
* 准备工作
    * 注册邮箱（以QQ邮箱为例）
    * 第三方邮箱需要特殊设置
        * 需要获取授权码
* python for mail 案例case01.py
    * SMTP协议负责发送邮件
        * 使用email模块构建邮件
            * 纯文本邮件，不包含格式的邮件
            * HTML格式邮件发送
                * 准备HTML代码作为内容
                * 邮件的subtype设置为html
            * 发送带附件的邮件
                * 可以把邮件看做是一个文本邮件和一个附件的合体
                * 一封邮件如果涉及多个部门，需要使用MIMEMultipart格式构建
            * 添加邮件头，抄送等信息
                * mail['From'] 表示发送者信息，包括姓名和邮件
                * mail['To'] 表示接受者信息，包括姓名和邮件
                * mail['Subject'] 表示摘要或者主题信息
            * 同时支持HTML和text格式
                * 构建一个MIMEMUltipart格式邮件
                * MIMEMultipart的subtype设置成alternative格式
                * 添加HTML和text邮件
        * 使用smtplib模块发送邮件
    * POP3协议负责接收邮件 案例case02.py  但是太长了。。没写完
        * 本质上市MDA到MUA的一个过程
        * 从MDA下载下来的是一个王铮的邮件结构体，需要解析才能得到每个具体的邮件内容
        * 步骤：
            * 用poplib下载邮件结构体原始内容
            * 准备相应的内容（邮件地址，密码，POP3实例）
            * 身份认证
            * 一般会先得到邮箱内邮件的整体列表
            * 根据相应的序号，得到某一封信的数据流
            * 利用解析函数进行解析处相应的邮件结构体
            * 用email解析邮件的具体内容
    