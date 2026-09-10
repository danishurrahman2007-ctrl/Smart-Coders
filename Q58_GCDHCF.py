def HCF(A,B):
    Temp=0
    for i in range(1,A+1):
        if A%i==0 and B%i==0:
            if Temp<i:
                 Temp=i
    print(Temp)

X=int(input("Enter First Number : "))
Y=int(input("Enter Second Number : "))

HCF(X,Y)
                
            

