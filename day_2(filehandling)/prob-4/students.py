import csv

passed = 0
failed = 0
max_avg = 0
topper = ""
processed_students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        maths = int(row["maths"])
        physics = int(row["physics"])
        chemistry = int(row["chemistry"])
        name = row["name"]
        
        total = maths + physics + chemistry
        average = round(total / 3, 2)
        
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        elif average >= 40:
            grade = "D"
        else:
            grade = "F"
            
        row["total"] = total
        row["average"] = average
        row["grade"] = grade
        processed_students.append(row)
        
        if average > max_avg:
            max_avg = average
            topper = name
            
        if average >= 40:
            passed += 1
        else:
            failed += 1

headers = ["roll_no", "name", "maths", "physics", "chemistry", "total", "average", "grade"]

with open("students_result.csv", "w", newline="") as out_file:
    writer = csv.DictWriter(out_file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(processed_students)

print(f"Processed {len(processed_students)} students -> students_result.csv")
print(f"Class Topper : {topper} (avg {max_avg})")
print(f"Passed : {passed} | Failed : {failed}")