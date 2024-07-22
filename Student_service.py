from dbconfig import dbconfig
from Student import user
import json

class user_service:
    def get_users(self):
        conn=dbconfig.openconnection()
        cur=conn.cursor()
        cur.execute("select * from student")
        out=cur.fetchall()
        for i in out:
            print(i)
