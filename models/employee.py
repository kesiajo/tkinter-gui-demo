from mongoengine import Document, StringField, IntField


class EmployeeModel(Document):
    meta = {"collection": "employees"}

    emp_id = IntField(required=True)
    emp_name = StringField(required=True)
    department = StringField(required=True)
    email = StringField(required=True)
