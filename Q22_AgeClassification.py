Age=int(input("Enter Age Of The Person : "))
if Age<18:
    print("The Person is A Child")
elif Age>=18 and Age<25:
    print("The Person is A Teenager")
elif Age>=25 and Age<=50:
    print("The Person is An Adult")
elif Age>50 and Age<=99:
    print("The Person is A Senior Citizen")
elif Age>=100:
    print("Century Man")
else:
    print("Enter Valid Age")