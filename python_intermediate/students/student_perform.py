import random
from datetime import datetime, timedelta
import json

num_stu=int(input("Enter number of students: "))
exam_yr=int(input("Enter examination year: "))

names=["Arun","Priya"]
departments=["Computer Science","Information Technology", "Electronics", "Mechanical"]

students = []

for i in range(1, num_stu+1):
    name = random.choice(names)
    department = random.choice(departments)
    age = random.randint(18, 25)
    python_marks = random.randint(0, 100)
    database_marks = random.randint(0, 100)
    networks_marks = random.randint(0, 100)
    total=python_marks+database_marks+networks_marks
    average=total/3
    if python_marks>=40 and database_marks>=40 and networks_marks>=40:
        result="Pass"
    else:
        result="Fail"
    start_date = datetime(exam_yr, 1, 1)
    if exam_yr % 4 == 0 and (exam_yr % 100 != 0 or exam_yr % 400 == 0):
        days_in_year = 366
    else:
        days_in_year = 365
    random_days = random.randint(0, days_in_year - 1)
    random_date = start_date + timedelta(days=random_days)
    exam_date = random_date.strftime("%Y-%m-%d")

    student = {
        "student_id": i,
        "name": name,
        "age": age,
        "department": department,
        "marks": {
            "python": python_marks,
            "database": database_marks,
            "networks": networks_marks
        },
        "total": total,
        "average": average,
        "result": result,
        "exam_date": exam_date
    }
    students.append(student)

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)

with open("students.json", "r") as file:
    added_students = json.load(file)

total_students = len(added_students)

passed = 0
failed = 0
averages = []

for student in added_students:

    if student["result"] == "Pass":
        passed += 1
    else:
        failed += 1

    averages.append(student["average"])


highest_average = max(averages)
lowest_average = min(averages)

print("\nStudent Performance Summary")
print("---------------------------")
print(f"Total Students : {total_students}")
print(f"Passed         : {passed}")
print(f"Failed         : {failed}")
print(f"Highest Average: {highest_average:.2f}")
print(f"Lowest Average : {lowest_average:.2f}")

print("\nStudent Data successfully written to students.json")

