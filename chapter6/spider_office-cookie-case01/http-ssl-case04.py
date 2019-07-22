from urllib import request,parse
import ssl

def go12306(url):
    # 这里是创建一个忽略掉SSL警告
    # 利用非认证上下文环境替换认证的上下文环境
    ssl._create_default_https_context = ssl._create_unverified_context()
    rsp = request.urlopen(url)
    html = rsp.read().decode('utf-8')
    print(html)

if __name__ == '__main__':
    # 但是我写代码的时候，12306好像是可以访问了。。按照课程上面的会出现SSL异常
    url = "https://www.12306.cn/mormhweb/"
    go12306(url)