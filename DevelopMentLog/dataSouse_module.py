import pymysql.cursors,logging

class dataSouse_manage():

    def getCon(self,host,port,db,user,passwd):
        try:
            # 将整个连接池返回出去
            self.con = pymysql.connect(
                host=host,  # 数据库地址
                port=port,  # 端口 注意是int类型
                db=db,  # 数据库名称
                user=user,  # 用户名
                passwd=passwd,  # 用户密码
                charset='utf8mb4',  # 字符编码集 ,注意这里，直接写utf8即可
                use_unicode=True)
            return self.con
        except Exception as e:
            self.con.commit()
            self.con.rollback()
            logging.error('数据库初始化异常，异常内容:%s',e)
        return None

    def getCur(self):
        self.cur = self.con.cursor()
        return self.cur

    def select_fetchall(self,sql,whereStr):
        try:
            if whereStr is not None:
                self.cur.execute(sql,whereStr)
            else:
                self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as e:
            self.con.commit()
            self.con.rollback()
            logging.error('集合数据查询异常，异常语句:%s，条件内容:%s，异常内容:%s',(sql,whereStr,e))
        return None

    def select_fetchone(self,sql,whereStr):
        try:
            if whereStr is not None:
                self.cur.execute(sql, whereStr)
            else:
                self.cur.execute(sql)
            return self.cur.fetchone()
        except Exception as e:
            self.con.commit()
            self.con.rollback()
            logging.error('单挑数据查询异常，异常语句:%s，条件内容:%s，异常内容:%s',(sql,whereStr,e))
        return None

    '''
    插入，返回主键 ID
    '''
    def insert(self,sql,valuesStr):
        try:
            self.cur.execute(sql, valuesStr)
            self.con.commit()
            return self.cur.lastrowid
        except Exception as e:
            self.con.commit()
            self.con.rollback()
            logging.error('数据插入异常，异常语句:%s，插入数据内容:%s，异常内容:%s',(sql,valuesStr,e))
        return None

    def update(self,sql,valuesStr):
        try:
            self.cur.execute(sql, valuesStr)
            self.con.commit()
            return self.cur.lastrowid
        except Exception as e:
            self.con.commit()
            self.con.rollback()
            logging.error('数据更新异常，异常语句:%s，更新数据内容:%s，异常内容:%s',(sql,valuesStr,e))
        return None