X=int(input("Enter X Co-Ordinate : "))
Y=int(input("Enter Y Co-Ordinate : "))
if X>0 and Y>0:
    print("The Point Lies in First Quadrant")
elif X<0 and Y>0:
    print("The Point Lies in Second Quadrant")
elif X<0 and Y<0:
    print("The Point Lies in Third Quadrant")
elif X>0 and Y<0:
    print("The Point Lies in Fourth Quadrant")
else:
    print("The Point Is At Origin")