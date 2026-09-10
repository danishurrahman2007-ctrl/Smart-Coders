A=int(input("Enter First Side of Triangle : "))
B=int(input("Enter Second Side of Triangle : "))
C=int(input("Enter Third Side of Triangle : "))

if A==B and B==C:
    print("It Is An Equilateral Triangle")
elif (A==B and B!=C) or (A==C and C!=B):
    print("It Is An Isoceles Triangle")
else:
    print("It Is A Scalene Triangle")