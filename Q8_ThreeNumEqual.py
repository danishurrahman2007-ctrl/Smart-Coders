A=int(input("Enter A Number : "))
B=int(input("Enter A Number : "))
C=int(input("Enter A Number : "))
if(A==B and B==C):
    print(f"{A},{B} and {C} are Equal")
elif(A==B and B!=C):
    print(f"{A} and {B} are Equal")
elif(A!=B and B==C):
    print(f"{B} and {C} are Equal")
elif(A==C and B!=C):
    print(f"{A} and {C} are Equal")
else:
    print("All Numbers Are Different")