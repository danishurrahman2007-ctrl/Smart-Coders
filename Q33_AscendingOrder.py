A=int(input("Enter First Number : "))
B=int(input("Enter Second Number : "))
C = int(input("Enter Third Number : "))

if A<B and A<C:
    print(A)
    if B<C:
        print(B)
        print(C)
    else:
        print(C)
        print(B)
elif B<A and B<C:
    print(B)
    if A<C:
        print(A)
        print(C)
    else:
        print(C)
        print(A)
else:
    print(C)
    if A<B:
        print(A)
        print(B)
    else:
        print(B)
        print(A)