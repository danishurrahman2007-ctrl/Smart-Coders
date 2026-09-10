A=int(input("Enter First Side of Triangle : "))
B=int(input("Enter Second Side of Triangle : "))
C=int(input("Enter Third Side of Triangle : "))

if A<0 or B<0 or C<0:
    print("Invalid Side Length")
elif (A+B)<=C or (A+C)<=B or (B+C)<=A:
    print("Invalid Triangle Side Length")
else:
    print("Valid Triangle")
