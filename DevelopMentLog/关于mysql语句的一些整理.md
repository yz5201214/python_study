# 关于MYSQL的一些语句说明
* mysql在python里面的like写法。好像不支持concat的写法。直接将模糊匹配的内容拼接成
    query_param = '%' + item['movie_name'] +'%' 然后作为参数传入即可