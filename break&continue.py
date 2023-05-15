# break used to terminate loop
students = ["fardin","rahul","jain","furi","raju"]

for student in students:
    if student == "furi":
        break;
    print(student)


print("\n")
# continue used to skip that part
for student in students:
    if student == "rahhul":
        continue;
    print(student)