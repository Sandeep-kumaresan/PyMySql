from flask import json


class Student:
    reg_no = 0
    name = ""
    age = 0

    def __init__(self, reg_no, name, age):
        self.reg_no = reg_no
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"({self.reg_no}-{self.name}-{self.age})"

    def to_json(obj):
        return json.dumps(obj, default=lambda obj: obj.__dict__)
