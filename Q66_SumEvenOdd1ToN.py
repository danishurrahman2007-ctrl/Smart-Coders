N=int(input("Enter A Number : "))
EvenSum=0
OddSum=0
for i in range(0,N):
    if i%2==0:
        EvenSum+=i
    else:
        OddSum+=i
print(f"Sum Of Even Numbers Till {N} Is : ",EvenSum)
print(f"Sum Of Odd Numbers Till {N} Is : ",OddSum)