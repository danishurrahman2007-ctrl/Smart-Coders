L=[]
Count=0
N=0
while N!=-1:
    N=int(input("Enter A Number : "))
    L.append(N)
    Count+=1
Sum=0
for j in range(0,Count):
    Sum=sum(L)
Avg=(Sum//Count)
print(Count)
print(Avg)