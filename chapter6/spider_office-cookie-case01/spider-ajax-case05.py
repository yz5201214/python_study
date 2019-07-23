'''
利用ajax请求，爬取豆瓣电影
了解python调用ajax
'''
from urllib import request,parse
import time,json


def moveDoubanAjax():
    # 注意下面的连接，start是开始下表，limit是当前加载的数据条数，interval_id是打分区间
    # 实际这里就是一个ajax请求，注意豆瓣电影，排行，分类里面选择一个之后，都是一直加载而不是重新刷新页面
    url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20"
    rsq = request.urlopen(url)
    data = rsq.read().decode()
    jsonData = json.loads(data)
    print(jsonData)

if __name__ == '__main__':
    moveDoubanAjax()