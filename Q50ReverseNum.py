N=int(input("Enter A Number : "))
Temp1=N
Count=0
while Temp1>0:
    Remainder=Temp1%10
    Count=((Count*10) + Remainder)
    Temp1=Temp1//10
print("The Reverse Of The Number Is : ",Count)