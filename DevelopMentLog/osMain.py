import os,json,time


if __name__ == '__main__':
    a = time.strftime("%H:%M:%S", time.localtime())
    a = '2019-09-13 '+ a
    pubTimeStr = time.strptime(a, "%Y-%m-%d %H:%M:%S")

    print(str(int(time.mktime(pubTimeStr))))