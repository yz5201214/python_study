from DevelopMentLog.dataSouse_module import dataSouse_manage


if __name__ == '__main__':
    dataSouse_manage = dataSouse_manage()
    con = dataSouse_manage.getCon('www.findbt.com',3306,'ultrax','root','cyfU2ypeM9AVeVzh')
    cur = dataSouse_manage.getCur()
    selectSql = 'select * from pre_common_pluginvar'
    dataList = dataSouse_manage.select_fetchall(selectSql,None)
    print(dataList)

    selectSql = "select * from pre_common_pluginvar where pluginvarid = %s and title like %s"
    dataItem = dataSouse_manage.select_fetchall(selectSql, ('1','%影视%',))
    print(dataItem)