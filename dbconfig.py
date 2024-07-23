import pymysql


class dbconfig:
    @staticmethod
    def open_connection():
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="1234",
            db='stu',
        )
        return conn

    @staticmethod
    def close_connection(conn):
        return conn.close()
