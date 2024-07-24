from flask import Flask, request,jsonify

from Student_service import student_service
from Student import Student

app = Flask(__name__)

service = student_service()

@app.route('/student', methods = ['POST'])
def create_student():
    data = request.get_json()
    student = Student(data['reg_no'], data['name'], data['age'])
    service.create_student(student)
    doc_json = student.to_json()
    print("doc json ", doc_json)
    return doc_json


@app.route('/students', methods = ['GET'])
def get_all_students():
    student_list = service.get_students()
    return student_list

@app.route('/user/<int:reg_no>', methods=['GET'])
def get_student(user_id):
    pass

@app.route('/delete_user/<int:reg_no>', methods=['DELETE'])
def delete_user(reg_no):
    service.delete_user(reg_no)
    return jsonify({'message': 'User deleted successfully', 'id': reg_no})

@app.route('/update_user/<int:reg_no>', methods=['PUT'])
def update_user(reg_no):
    data = request.get_json()
    user = Student(reg_no, data['name'], data['age'])
    service.update_user(user)
    return jsonify({'message': 'User updated successfully', 'id': reg_no})


@app.route('/')
def hello():
    return 'Your Flask Server Running'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port = '5002')