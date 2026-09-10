def ProductOfDigits(N):
    if N<=9:
        return N
    return (N%10)*ProductOfDigits(N//10)
    print(Count)
A=int(input("Enter A Number : "))
print(ProductOfDigits(A))
