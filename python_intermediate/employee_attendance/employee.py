import random
from datetime import date
import calendar
import xml.etree.ElementTree as ET
import json

names = [
    "Arun Kumar",
    "Priya Sharma",
    "Rahul Patil",
    "Sneha Naik",
    "Amit Shah",
    "Neha Joshi"
]

departments = [
    "IT",
    "HR",
    "Finance",
    "Sales",
    "Operations"
]

def generate_attendance(year, month):

    attendance = []

    number_of_days = calendar.monthrange(year, month)[1]

    for day in range(1, number_of_days + 1):

        current_date = date(year, month, day)

        if current_date.weekday() < 5:

            status = random.choices(
                ["Present", "Absent", "Leave"],
                weights=[80, 10, 10]
            )[0]

            attendance.append({
                "date": current_date.strftime("%Y-%m-%d"),
                "status": status
            })

    return attendance


def generate_data(num_employees, year, month):

    employees = []

    for i in range(num_employees):

        employee_id = 1001 + i

        name = random.choice(names)

        department = random.choice(departments)

        joining_year = random.randint(2020, 2025)
        joining_month = random.randint(1, 12)

        days_in_joining_month = calendar.monthrange(
            joining_year,
            joining_month
        )[1]

        joining_day = random.randint(1, days_in_joining_month)

        joining_date = date(
            joining_year,
            joining_month,
            joining_day
        ).strftime("%Y-%m-%d")

        attendance = generate_attendance(year, month)

        employee = {
            "id": employee_id,
            "name": name,
            "department": department,
            "joining_date": joining_date,
            "attendance": attendance
        }

        employees.append(employee)

    return employees

def save_data(employees):

    root = ET.Element("employees")

    for employee in employees:

        employee_element = ET.SubElement(root, "employee")

        id_element = ET.SubElement(employee_element, "id")
        id_element.text = str(employee["id"])

        name_element = ET.SubElement(employee_element, "name")
        name_element.text = employee["name"]

        department_element = ET.SubElement(
            employee_element,
            "department"
        )
        department_element.text = employee["department"]

        joining_element = ET.SubElement(
            employee_element,
            "joining_date"
        )
        joining_element.text = employee["joining_date"]

        attendance_element = ET.SubElement(
            employee_element,
            "attendance"
        )

        for record in employee["attendance"]:

            day_element = ET.SubElement(
                attendance_element,
                "day"
            )

            day_element.set(
                "date",
                record["date"]
            )

            day_element.text = record["status"]

    tree = ET.ElementTree(root)

    tree.write(
        "employees.xml",
        encoding="utf-8",
        xml_declaration=True
    )

def load_data():

    tree = ET.parse("employees.xml")

    root = tree.getroot()

    return root

def generate_report(root):

    reports = []

    for employee in root.findall("employee"):

        employee_id = int(employee.find("id").text)

        name = employee.find("name").text

        department = employee.find("department").text

        present_days = 0
        absent_days = 0
        leave_days = 0

        attendance = employee.find("attendance")

        for day in attendance.findall("day"):

            status = day.text

            if status == "Present":
                present_days += 1

            elif status == "Absent":
                absent_days += 1

            elif status == "Leave":
                leave_days += 1

        total_working_days = (
            present_days +
            absent_days +
            leave_days
        )

        if total_working_days > 0:
            attendance_percentage = (
                present_days /
                total_working_days
            ) * 100
        else:
            attendance_percentage = 0

        attendance_percentage = round(
            attendance_percentage,
            2
        )

        report = {
            "employee_id": employee_id,
            "name": name,
            "department": department,
            "total_working_days": total_working_days,
            "present_days": present_days,
            "absent_days": absent_days,
            "leave_days": leave_days,
            "attendance_percentage": attendance_percentage
        }

        reports.append(report)

    return reports

def save_report(reports):

    with open("attendance_report.json", "w") as file:

        json.dump(
            reports,
            file,
            indent=4
        )

def display_report(reports):

    print("================Employee Attendance Report================")

    for report in reports:

        print(f"Employee ID : {report['employee_id']}")
        print(f"Name        : {report['name']}")
        print(f"Department  : {report['department']}")
        print(f"Working Days : {report['total_working_days']}")
        print(f"Present      : {report['present_days']}")
        print(f"Absent       : {report['absent_days']}")
        print(f"Leave        : {report['leave_days']}")
        print(
            f"Attendance   : "
            f"{report['attendance_percentage']:.2f}%"
        )

        print("---------------------------------------")


def main():

    try:

        num_employees = int(
            input("Enter number of employees: ")
        )

        year = int(
            input("Enter year: ")
        )

        month = int(
            input("Enter month: ")
        )

        if num_employees <= 0:
            print("Number of employees must be greater than 0.")
            return

        if month < 1 or month > 12:
            print("Month must be between 1 and 12.")
            return

        if year < 1:
            print("Please enter a valid year.")
            return

    except ValueError:

        print("Please enter valid numbers.")
        return

    employees = generate_data(
        num_employees,
        year,
        month
    )

    save_data(employees)
    root = load_data()
    reports = generate_report(root)
    save_report(reports)
    display_report(reports)


    print("Attendance report generated successfully.")
    print("XML File : employees.xml")
    print("JSON File: attendance_report.json")


if __name__ == "__main__":
    main()