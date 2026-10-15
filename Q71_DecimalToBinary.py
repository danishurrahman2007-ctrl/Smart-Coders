N=int(input("Enter A Number : "))
Temp=N
Temp1=N
Remainder=0
DecimalToBinary=""
while Temp1>0:
    Remainder=Temp1%2
    DecimalToBinary=str(Remainder)+DecimalToBinary
    Temp1=Temp1//2
print(DecimalToBinary)