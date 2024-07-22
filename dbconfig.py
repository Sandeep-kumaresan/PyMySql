import pymysql
class dbconfig:
    @staticmethod
    def openconnection():
        conn=pymysql.connect(
            host="localhost",
            username="root",
            password="1234",
            db="stu"
        )
        return conn
    @staticmethod
    def closeconnection(conn):
        return conn.close()