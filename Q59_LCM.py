def HCFLCM(A,B):
    Temp=0
    for i in range(1,A+1):
        if A%i==0 and B%i==0:
            if Temp<i:
                 Temp=i
    print(f"The HCF Of {A} and {B} Is : ",Temp)
    LCM=(X*Y)/Temp
    print(f"The LCM Of {A} and {B} Is : ",LCM)
X=int(input("Enter First Number : "))
Y=int(input("Enter Second Number : "))

HCFLCM(X,Y)
                