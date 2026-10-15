A=int(input("Enter A Number : "))
Temp2=A
Count=0
if A==0:
    Count=1
    SmallestNum=0
    LargestNum=0
while Temp2>0:
    Temp2=Temp2//10
    Count+=1
print("The Digits In The Number Is : ",Count)
Temp=A
Temp1=0
LargestNum=0
SmallestNum=9
for i in range(0,Count):
    Temp1=Temp%10
    if Temp1>LargestNum:
        LargestNum=Temp1
    if Temp1<SmallestNum:
        SmallestNum=Temp1
    Temp=Temp//10
print(f"The Largest Digit in {A} Is : ",LargestNum)
print(f"The Smallest Digit in {A} Is : ",SmallestNum)
