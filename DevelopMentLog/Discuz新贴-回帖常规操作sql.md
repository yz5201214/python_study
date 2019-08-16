

select * from gt_m_main_info where f_type ='1'

select * from gt_m_replines_info where f_m_id = '703a5a2ee0ac4109a2aa4102a1506701'



select * from pre_forum_forum

select max(pid)pid from pre_forum_post_tableid

select * from pre_forum_thread order by tid desc



select * from pre_forum_post where subject !='--' order by pid desc

-- 527  根据主贴ID查找所有回复
select * from pre_forum_post where tid = '1162' order by pid desc

select * from pre_forum_attachment where pid = '1181' ORDER by pid desc;

select * from pre_forum_attachment where pid = '1488' ORDER by pid desc;



select * from pre_forum_attachment_7 where aid in ('4592','4593','4594')

select * from pre_forum_attachment_9 where aid = '3575'

select * from pre_forum_attachment_1 where tid = '3421'



select * from pre_forum_attachment_4 where pid = '694'


select * from pre_forum_attachment_5





delete from gt_m_main_info where f_type ='1'

delete from gt_m_replines_info where f_m_id not in (
	select f_spider_url from gt_m_main_info 
)
