#Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5× rate)
HoursWorked=int(input("Enter Number Of Hours Worked : "))
Salary=50000
if HoursWorked>40:
    Salary+=(HoursWorked-40)*1875
    print("The Total Salary Is : ",Salary)
elif HoursWorked<40:
    Salary-=(40-HoursWorked)*1250
    print("The Total Salary Is : ",Salary)
