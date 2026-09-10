Hour=int(input("Enter The Time in Hours from 0 to 24 : "))
if Hour in range(5,11):
    print("Good Morning")
elif Hour in range(12,17):
    print("Good Afternoon")
elif Hour in range(18,20):
    print("Good Evening")
else:
    print("Good Night")