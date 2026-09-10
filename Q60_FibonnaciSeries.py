N=int(input("Enter A Number : "))
A=0
B=1
C=0
print(A)
print(B)
for i in range(0,N-2):
    C=A+B
    A=B
    B=C
    print(C)