import ftplib
import os,socket

HOST = 'ftp.mozilla.org'
DIR = '/pub/zz/'
FILE = 'marker.txt'

def test01():
    try:
        # 建立FTP连接
        f = ftplib.FTP()
        f.set_debuglevel(2)
        f.connect(HOST)
        # 登陆,如果有用户名，请传入用户名
        f.login()
        # 进入目录
        f.cwd(DIR)
        # 运行ENTR命令 下载文件到本地，然后运行回调函数
        f.retrbinary('ENTR {0}'.format(FILE),open(FILE,'web').write())
    except Exception as e:
        print(e)
        exit()

if __name__ == '__main__':
    test01()