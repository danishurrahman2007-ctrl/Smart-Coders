N=int(input("Enter A Number : "))
Count=0
for i in range(1,N+1):
    if N%i==0:
        Count+=1
if Count==2:
    print("It Is A Prime Number")
else:
    print("It Is A Composite Number")
