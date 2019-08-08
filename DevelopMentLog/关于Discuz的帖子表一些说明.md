# 部分自己摸索出来的表
* 如果想要通过插入数据实现发帖功能
    * pre_forum_post_tableid 帖子表的PID主表，可以根据倒叙排列+1插入数据，作为后续的唯一ID
    * pre_forum_thread 帖子主表， pre_forum_post 帖子内容表
    * pre_forum_attachment 附件主表， pre_forum_attachment_1/2/3/4/5/6/7/8附件内容表
* 帖子允许使用html代码 参考
    * http://www.discuz.net/thread-1577419-1-1.html
    * http://www.discuz.net/forum.php?mod=viewthread&tid=3661511