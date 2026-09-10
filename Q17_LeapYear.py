Year=int(input("Enter A Year : "))
if Year%400==0 and (Year%4==0 or Year%100!=0):
    print("It Is A Leap Year")
else: 
    print("It Is Not A Leap Year")