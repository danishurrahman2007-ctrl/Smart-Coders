N=int(input("Enter A Number : "))
print(f"The Factors Of {N} Are : ")
for i in range(1,N+1):
    if N%i==0:
        print(i)
