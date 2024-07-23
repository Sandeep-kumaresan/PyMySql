from dbconfig import dbconfig
from Student import Student
import json


class student_service:
    def get_students(self):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from student")
        out = cur.fetchall()
        users_list = []
        for i in out:
            print("select query output", i)
            student = Student(i[0], i[1], i[2]);
            users_list.append(json.loads(Student.to_json(student)))
        dbconfig.close_connection(conn)
        return users_list

    def create_student(self, student):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                   insert into student(reg_no,name,age) values ( %s, %s, %s)
                   """,
                    (student.reg_no, student.name, student.age))
        print(conn.insert_id())
        conn.commit()
