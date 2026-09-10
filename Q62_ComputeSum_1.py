N=int(input("Enter A Number : "))
Sum=0
X=1
for i in range(0,N):
    Sum+=((-1)**i)*X
    X=X+1
print(f"The Sum Of Series Till {N} Is : ",Sum)