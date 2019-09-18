import oss2,time
from itertools import islice

def upload():
    auth = oss2.Auth('LTAI4Fm1MACEyXSzXMW6PT1m', 'rCIsBsNYc9nxL2cxhx4PJp2V6FBAsP')
    bucket = oss2.Bucket(auth, 'http://oss-cn-hongkong.aliyuncs.com', 'bbs-movie', connect_timeout=30)

    # 1) 直接上传文件put_object_from_file
    result = bucket.put_object_from_file('j2f8mtancr9te8j.jpg',
                                         r'G:\data\i.gtimg.cn\qqlive\img\jpgcache\files\qqvideo\j\j2f8mtancr9te8j.jpg')
    if result.status == 200:
        print('success')


def downLoad():
    auth = oss2.Auth('LTAI4Fm1MACEyXSzXMW6PT1m', 'rCIsBsNYc9nxL2cxhx4PJp2V6FBAsP')
    bucket = oss2.Bucket(auth, 'http://oss-cn-hongkong.aliyuncs.com', 'bbs-movie', connect_timeout=30)
    result = bucket.get_object_to_file('j2f8mtancr9te8j.jpg', 'j2f8mtancr9te8j.jpg')
    print(result.status)


def getFileList():
    auth = oss2.Auth('LTAI4Fm1MACEyXSzXMW6PT1m', 'rCIsBsNYc9nxL2cxhx4PJp2V6FBAsP')
    bucket = oss2.Bucket(auth, 'http://oss-cn-hongkong.aliyuncs.com', 'bbs-movie', connect_timeout=30)
    for b in islice(oss2.ObjectIterator(bucket), 10):
        print(b.key)

def getAllBucket():
    service = oss2.Service(oss2.Auth('LTAI4Fm1MACEyXSzXMW6PT1m', 'rCIsBsNYc9nxL2cxhx4PJp2V6FBAsP'), 'http://oss-cn-hongkong.aliyuncs.com')
    print('\n'.join(info.name for info in oss2.BucketIterator(service)))

def delFile():
    auth = oss2.Auth('LTAI4Fm1MACEyXSzXMW6PT1m', 'rCIsBsNYc9nxL2cxhx4PJp2V6FBAsP')
    bucket = oss2.Bucket(auth, 'http://oss-cn-hongkong.aliyuncs.com', 'bbs-movie', connect_timeout=30)
    bucket.delete_object()

def delFile():
    import shutil, os
    if os.path.exists(os.path.join(r'G:\data\eximg.hitv.com\u\o\archievideo\iqiyi\collects', '2c6d193eae951807bb821faef8406e9e.jpg')):
        os.remove(os.path.join(r'G:\data\eximg.hitv.com\u\o\archievideo\iqiyi\collects', '2c6d193eae951807bb821faef8406e9e.jpg'))
if __name__ == '__main__':
    # upload()
    # downLoad()
    # getFileList()
    # getAllBucket()
    # delFile()
    abc = '2019-09-11 13:59:53'
    timeArray = time.strptime(abc, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    print(timestamp)
