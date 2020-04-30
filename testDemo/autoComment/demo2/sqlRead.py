import MySQLdb

class DBconnect():

    dbAddress = "116.62.22.93:3306"
    userName = "weixue"
    password = "wx_123456"
    db = "jihe_2019"

    def dbConn(self, dbAddress="116.62.22.93", userName="weixue", password="wx_123456", db="jihe_2019"):
        # 打开数据库连接
        db = MySQLdb.connect(dbAddress, userName, password, db, charset='utf8')
        return db

    def dbClose(self, db):
        # 关闭数据库连接
        db.close()

    def dbTest(self, db):
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # 使用execute方法执行SQL语句
        cursor.execute("SELECT VERSION()")

        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchone()

        print("Database version : %s " % data)

    def search(self, db, sqlStatement):
        lis = []

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        # SQL 查询语句
        sql = sqlStatement
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            # print(results)
            for row in results:
                customer_id = row[0]
                lis.append(customer_id)

        except:
            print("Error: unable to fecth data")
        # print(lis)
        return lis


if __name__ == "__main__":
    db = DBconnect()
    dbc = db.dbConn()
    # db.dbTest(dbc)
    sql = "SELECT mobile FROM jh_customer_login WHERE mobile LIKE '1521234%' ORDER BY mobile DESC"
    mobileList = db.search(dbc, sql)
    db.dbClose(dbc)
