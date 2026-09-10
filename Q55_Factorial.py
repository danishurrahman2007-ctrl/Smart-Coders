def Factorial(N):
    if N==0 or N==1:
        return 1
    return N*Factorial(N-1)
Num=int(input("Enter A Number : "))
print(f"The Factorial Of {Num} Is : ",Factorial(Num))