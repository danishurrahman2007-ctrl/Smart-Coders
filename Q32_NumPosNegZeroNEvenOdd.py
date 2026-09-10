N=int(input("Enter A Number : "))
if N>0:
    print(N,"Is A Positive Number")
    if N%2==0:
        print(N,"Is An Even Number")
    else:
        print(N,"Is An Odd Number")
elif N<0:
    print(N,"Is A Negative Number")
else:
    print(N,"Is Zero")