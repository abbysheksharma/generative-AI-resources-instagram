import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    rows = [
            ["Name", "Age", "City"],
            ["Rahul", 20, "Delhi"],
            ["Aman", 22, "Mumbai"]
        ]
    writer.writerows(rows)