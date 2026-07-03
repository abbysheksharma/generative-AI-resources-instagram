#1
# file = open("students.txt", "r")
# print(file.read())
# file.close()

#2
with open("students.txt", "r") as file:
  print(file.read())