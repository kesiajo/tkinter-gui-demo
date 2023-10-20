import json

import mongoengine

from models import EmployeeModel
from settings import MONGODB_DB_NAME, MONGODB_HOST

mongoengine.connect(host=MONGODB_HOST, db=MONGODB_DB_NAME)
with open('employees.json', "r") as file:
    data = json.load(file)

[EmployeeModel(**each).save() for each in data]
