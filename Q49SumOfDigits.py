N=int(input("Enter A Number : "))
Temp1=N
Count=0
while Temp1>0:
    Temp=Temp1%10
    Count+=Temp
    Temp1=Temp1//10
print("The Sum Of The Digits In The Number Is : ",Count)