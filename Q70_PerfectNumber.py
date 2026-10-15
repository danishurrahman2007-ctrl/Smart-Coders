N=int(input("Enter A Number : "))
SumOfDivisors=0
for i in range(1,N):
    if N%i==0:
        SumOfDivisors+=i
print(SumOfDivisors)
if SumOfDivisors==N:
    print(N,"Is A Perfect Number")
else:
    print(N,"Is Not A Perfect Number")