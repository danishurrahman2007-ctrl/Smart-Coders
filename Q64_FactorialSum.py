N=int(input("Enter A Number : "))
SumOfFact=0
for i in range(0,N+1):
    Fact=1
    for j in range(1,i+1):
        Fact*=j
    SumOfFact+=Fact
print(f"The Sum Of Factorials Till {N} Is : ",SumOfFact)