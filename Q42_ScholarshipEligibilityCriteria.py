print("Scholarship Eligibility Criteria : ")
Marks=int(input("Enter Your Intermediate Marks : "))
Attendance=int(input("Enter Your Attendance : "))
FamilyIncome=int(input("Enter Your Family Income : "))

if Marks>300 and Attendance>75 and FamilyIncome<180000:
    print("Student Eligible For Scholarship")
else:
    print("Student Not Eligible For Scholarship")