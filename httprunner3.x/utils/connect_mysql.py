import pymysql
'''
pip install PyMySQL==0.9.3
'''

# 配置数据库相关信息
dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309}


class DbConnect(object):
    def __init__(self, db_cof, database=""):
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
           self.cursor.execute(sql)  # 执行SQL语句
           self.db.commit()  # 提交修改
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()

if __name__ == '__main__':
    db = DbConnect(dbinfo, database="apps")
    # 查询
    sql1 = 'SELECT * from apiapp_goods WHERE id = 1;'
    res1 = db.select(sql1)
    print(res1)

    # 执行
    sql2 = 'UPDATE apiapp_goods SET goodsname="xx悠悠课程" WHERE id=1;'
    db.execute(sql2)
    db.close()


