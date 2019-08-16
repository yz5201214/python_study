# 部分自己摸索出来的表
* 如果想要通过插入数据实现发帖功能
    * pre_forum_post_tableid 帖子表的PID主表，可以根据倒叙排列+1插入数据，作为后续的唯一ID
    * pre_forum_thread 帖子主表， pre_forum_post 帖子内容表
    * pre_forum_attachment 附件主表， pre_forum_attachment_1/2/3/4/5/6/7/8附件内容表
    * 参考：https://www.cnblogs.com/rwxwsblog/p/4759775.html
        * 帖子表：pre_forum_post 
        * 帖子表pid最大值设置表：pre_forum_post_tableid
　　　　* 帖子列表表：pre_forum_thread
　　　　* 帖子所在板块表：pre_forum_forum
            * threads 总主题数，posts 首页帖子数，
* 帖子允许使用html代码 参考
    * http://www.discuz.net/thread-1577419-1-1.html
    * http://www.discuz.net/forum.php?mod=viewthread&tid=3661511
* 重新本地安装教程
    * https://jingyan.baidu.com/article/642c9d34e491d8644a46f708.html
* 局域网访问教程：
    * 总结一下在局域网内访问挂在Wampserver的www目录下的网站需要的几个步骤：
        * 将httpd.conf文件中的几处Deny from all改为Allow from all （网上一搜就有很多，不重复了）
        * 把本地的防火墙关闭（各系统关闭方式网上搜一下也有很多，由于我的系统是Win10 所以可能问题就出在这，也许一些Win7的同学不需要关闭防火墙就能访问了）
        * 将电脑和手机连到同一个wifi下（或者可以用手机给笔记本电脑开热点的方式，只要能让它们处于同一个局域网中）
        * Win+R呼出cmd，使用ipconfig命令，查看本地的IPv4地址，
        * 打开手机中的任意浏览器，输入电脑的IPv4地址+端口号+项目名的方式，即可成功访问站点，进行移动端的测试。


* 插件需要新增的数据表
    * 参数配置表:pre_common_pluginvar
    * 影视分享主记录表:pre_plugin_xlwsq_ysdp_item
    * 影视分享下载记录表:pre_plugin_xlwsq_ysdp_down
