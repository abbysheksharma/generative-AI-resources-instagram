import json

student = {
    "name": "Rahul",
    "age": 20,
    "city": "Delhi",
    "gender": "mail"
}

with open("data.json", "w+") as file:
    json.dump(student, file, indent=2)
    file.seek(0)
    data = json.load(file)

print(data)