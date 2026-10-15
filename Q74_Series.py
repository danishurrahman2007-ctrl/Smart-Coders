N=int(input("Enter Number Of Terms Required :  "))
Z=int(input("Enter A Number Of Which You Want To Find The Series Of : "))
Sum=0
X=0
Y=1
def Factorial(A):
    if A==0 or A==1:
        return 1
    return A*Factorial(A-1)
for i in range(0,N):
    Sum+=(((-1)**X)*(Z**Y))/(Factorial(Y))
    X+=1
    Y+=2
print(Sum)