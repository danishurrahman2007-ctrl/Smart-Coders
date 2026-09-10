AdultTickets=200
ChildTickets=100
BabyTickets=0

N=int(input("Enter Number Of Adults : "))
N1=int(input("Enter Number Of Children : "))
N2=int(input("Enter Number Of Babies : "))

TotalPrice=N*200 + N1*100 + N2*0

print(f"The Total Price Of {N+N1} Tickets Is : ",TotalPrice)
print("Enjoy Your Trip !!!")
