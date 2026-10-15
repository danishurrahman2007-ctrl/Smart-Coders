N=int(input("Enter A Binary Numer : "))
StrN=str(N)
Temp=N
BinaryToDecimal=0
for i in range(0,len(StrN)):
    Temp1=int(Temp%10)
    BinaryToDecimal+=(Temp1*(2**i))
    Temp=int(Temp//10)
print(BinaryToDecimal)
