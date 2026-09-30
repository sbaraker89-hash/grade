print("BCA STUDENT RESULT")

name = input("Enter student name: ")

c = int(input("Enter C Programming marks: "))
python = int(input("Enter Python marks: "))
dbms = int(input("Enter DBMS marks: "))
os = int(input("Enter Operating System marks: "))
maths = int(input("Enter Mathematics marks: "))

if c >= 35 and python >= 35 and dbms >= 35 and os >= 35 and maths >= 35:
    print("\nStudent Name:", name)
    print("Result: PASS")
else:
    print("\nStudent Name:", name)
    print("Result: FAIL")