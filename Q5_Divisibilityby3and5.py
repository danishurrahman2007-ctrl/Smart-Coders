Num=int(input("Enter A Number : "))
if(Num%3==0 and Num%5==0):
    print(Num,"Is Divisible by 3 and 5")
elif(Num%3==0):
    print(Num,"Is Divisible by 3")
elif(Num%5==0):
    print(Num,"Is Divisible by 5")
else:
    print(Num,"Is Not Divisible by both 3 and 5")