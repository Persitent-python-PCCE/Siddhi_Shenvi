import random
from datetime import datetime, timedelta
import json
#student names, departments, student records-list
names = ["Arun", "Priya", "Rahul", "Sneha"]
random.randint(0, 100)
random.choice(names)
student={
    "name":"Arjun",
    "age": 21,
    "dept": "IT"
}
print(student["age"])

#venv, 1. 2. 3. min 5-6 tables, add more records, modular(sep pages not everything in main.py)
# main.py cursor
#sep of concern(soc): controller -- service -- dao --dto(model class)(modules and packages class)
#student_id=none
#menu in controller with loop and 0 exited...like 1.view prod 2.add prod
