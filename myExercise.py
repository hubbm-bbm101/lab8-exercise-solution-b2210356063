import sys
file = sys.argv[1]
people = sys.argv[2].split(",")
dict = {}
output = ""
class MyException(Exception):
    pass
with open("student.txt", mode="r", encoding="utf-8") as f:
    data = str(f.read()).splitlines()
    for line in data:
        entries = line.split(":")
        dict[entries[0]] = entries[1]
for person in people:
    try:
        if(not person in dict):
            raise MyException
        output += " Name: " + person + ", University: " + dict[person]
    except MyException:
        output += " No record of ‘" + person +"’ was found!"
print(output)