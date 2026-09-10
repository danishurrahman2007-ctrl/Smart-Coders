N=int(input("Enter A Number : "))
for i in range(1,N+1):
    Count=0
    for j in range(1,N+1):
        if i%j==0:
            Count+=1
    if Count==2:
        print(i)