A=int(input("Enter First Number : "))
B=int(input("Enter Second Number : "))
C=int(input("Enter Third Number : "))

if A>B and A>C:
    print(A,"Is The Largest Number")
elif B>C and B>A:
    print(B,"Is The Largest Number")
else:
    print(C,"Is The Largest Number")

