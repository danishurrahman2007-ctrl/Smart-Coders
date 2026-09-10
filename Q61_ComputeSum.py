N=int(input("Enter A Number : "))
Sum=0
for i in range(1,N+1):
    Sum+=(1/i)
print(f"The Sum Of Series Till {N} Is : ",Sum)