N1=input("Enter A Character : ")
N=ord(N1)
if (N>=65 and N<=90) or (N>=97 and N<=122):
    print("The Character Is An Alphabet")
elif N>=48 and N<=57:
    print("The Character Is A Digit")
else:
    print("The Character Is A Special Character")