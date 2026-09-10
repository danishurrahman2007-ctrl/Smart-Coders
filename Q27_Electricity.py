FixedCharge=100
Units=int(input("Enter Number Of Units Used : "))

if Units<=100:
    print("The Total Price Is : ",(Units*1.50))
elif Units<=300:
    print("The Total Price Is : ",(100*1.50) + ((Units-100)*3.00))
else:
    print("The Total Price Is : ",(100*1.50) + (200*3.00) + ((Units-300)*5.00))