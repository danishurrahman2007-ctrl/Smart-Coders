ID=2604
Password="AlberTKamchor"

A=int(input("Enter Your ID : "))
B=input("Enter Your Password : ")

if ID==A and Password==B:
    print("User Successfully Recognized")
elif ID==A:
    print("Wrong Password")
elif Password==B:
    print("Wrong ID")
else:
    print("Wrong ID and Password")