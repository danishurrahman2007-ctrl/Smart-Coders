A=input("Enter A Character : ")
if len(A)!=1:
    print("Enter A Single Character Only")
elif A.isupper():
    print("The Character is Uppercase")
elif A.islower():
    print("The Character is Lowercase")
elif A.isdigit():
    print("The Character is Digit")
else:
    print("Special Character")