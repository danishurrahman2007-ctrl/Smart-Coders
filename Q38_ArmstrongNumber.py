N=int(input("Enter A 3-Digit Number : "))
Temp1=N
X=0
for i in range(0,3):
    Temp=Temp1%10
    R=((Temp)**3)
    X+=R
    Temp1=Temp1//10
print(X)
if X==N:
    print(N,"Is An Armstrong Number")