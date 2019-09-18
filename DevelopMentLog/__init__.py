import json,re,operator
import pymysql,time
import pandas as pd
from redis import Redis

class discuz_manage():
    def newPosts(self,cursors,connect,newItem):
        b_Fid = newItem['b_Fid']  # 这里是板块ID，通过统一配置来进行插入
        # 防止因为标题过程，入库失败
        if len(newItem['b_Title']) > 50:
            b_Title = newItem['b_Title'][0:35] + "..."
        else:
            b_Title = newItem['b_Title']
        # 如果时间戳没有，取当前时间戳
        b_Dataline = newItem['b_Dataline']
        if b_Dataline is None or b_Dataline == '':
            b_Dataline = str(int(time.time()))
        # 默认附件0个
        b_FilesSize = '0'
        if newItem['b_FilesSize'] is not None:
            b_FilesSize = newItem['b_FilesSize']
        try:
            # pid表
            cursors.execute(
                """insert into pre_forum_post_tableid(pid)
                           value (%s)""",
                ('0',))
            connect.commit()
            p_id = cursors.lastrowid
            cursors.execute(
                """insert into pre_forum_thread(tid,fid,posttableid,typeid,sortid,readperm,price,author,authorid,subject,dateline,lastpost,lastposter,views,replies,displayorder,highlight,digest,rate,special,attachment,moderated,closed,stickreply,recommends,recommend_add,recommend_sub,heats,status,isgroup,favtimes,sharetimes,stamp,icon,pushedaid,cover,replycredit,relatebytag,maxposition,bgcolor,comments,hidden)
                           value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (p_id, b_Fid, '0', '0', '0', '0', '0', 'admin', '1', b_Title, b_Dataline,
                 b_Dataline,
                 'admin', '1', '0', '0', '0', '0', '0', '0',
                 b_FilesSize,
                 '0', '0', '0', '0', '0', '0', '0', '32', '0', '0', '0', '-1', '-1', '0', '0', '0', '0', '1', '', '0',
                 '0',))
            connect.commit()

            cursors.execute(
                """insert into pre_forum_post(pid,fid,tid,first,author,authorid,subject,dateline,message,useip,port,invisible,anonymous,usesig,htmlon,bbcodeoff,smileyoff,parseurloff,attachment,rate,ratetimes,status,tags,comment,replycredit,position)
                           value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (p_id, b_Fid, p_id, '1', 'admin', '1',
                 b_Title, b_Dataline, newItem['b_Content'],  # + ''.join(attachList)
                 '127.0.0.1', '8081', '0', '0', '1', '1', '0', '-1', '0',
                 b_FilesSize,
                 '0', '0', '0', '', '0', '0', '1',))
            # 更新板块主题数目，今日发帖数等
            lastpost = ['亏坨屎', b_Title, b_Dataline, 'admin']
            lastpostStr = '	'.join(lastpost)
            updateForumSql = "update pre_forum_forum set threads = threads +1 , posts = posts +1 , todayposts = todayposts +1 , lastpost = '" + lastpostStr + "' where fid = %s "
            cursors.execute(updateForumSql, (b_Fid,))
            # 事物处理，一次性提交
            connect.commit()
        except Exception as e:
            print('新贴表插入异常，标题 %s ,异常内容 %s' % (newItem['b_Title'], e,))
            connect.rollback()
            connect.commit()

if __name__ == '__main__':
    redis_db = Redis(host='dev.kuituoshi.com', port=6379, password='88888888', db=4)
    redis_data_btbbt = 'btbbt_cache'

    my = pymysql.connect(
        host='www.findbt.com',  # 数据库地址
        port=3306,  # 端口 注意是int类型
        db='ultrax',  # 数据库名称
        user='root',  # 用户名
        passwd='cyfU2ypeM9AVeVzh',  # 用户密码
        charset='utf8',  # 字符编码集 ,注意这里，直接写utf8即可
        use_unicode=True)
    cur = my.cursor()
    newItem = {}
    newItem['b_Fid'] = '37'
    newItem['b_Title'] = 'teztsetsetststst'
    newItem['b_Content'] = '测试内容'
    newItem['b_Dataline'] = str(int(time.time()))
    newItem['b_FilesSize'] = '0'

    discuz = discuz_manage()
    discuz.newPosts(cur,my,newItem)


