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
    def get_student(self, reg_no):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("select * from student where reg_no = " + str(reg_no))
        output = cur.fetchall()
        user = ''
        for i in output:
            print("select query output ", i)
            user = Student(i[0], i[1], i[2]);

        dbconfig.close_connection(conn)
        return Student.to_json(user)
    def create_student(self, student):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("""
                   insert into student(reg_no,name,age) values ( %s, %s, %s)
                   """,
                    (student.reg_no, student.name, student.age))
        print(conn.insert_id())
        conn.commit()

    def update_student(self,student):
        conn=dbconfig.open_connection()
        cur=conn.cursor()
        cur.execute("""UPDATE student
        set name = %s,age = %s where reg_no = %s""",
                    (student.name,student.age,student.reg_no))
        conn.commit()
        conn.close()

    def delete_student(self,reg_no):
        conn = dbconfig.open_connection()
        cur = conn.cursor()
        cur.execute("DELETE from student where reg_no = " + str(reg_no))
        conn.commit()