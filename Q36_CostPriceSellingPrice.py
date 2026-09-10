Item=input("Enter An Item : ")
CostPrice=int(input("Enter The Cost Price :"))
SellingPrice=int(input("Enter The Selling Price :"))
if (SellingPrice-CostPrice)>0:
    print("Profit")
elif (SellingPrice-CostPrice)==0:
    print("No Profit")
else:
    print("Loss")