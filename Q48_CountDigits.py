N=int(input("Enter A Number : "))
Temp=N
Count=0
while Temp>0:
    Temp=Temp//10
    Count+=1
print("The Digits In The Number Is : ",Count)