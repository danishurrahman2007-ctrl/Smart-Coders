Balance=int(input("Enter Your Balance : "))
MinBalance=2000
WithdrawlAmt=int(input("Enter The Amount You Wish To Withdraw : "))
if Balance<=MinBalance:
    print("Balance is Less than the Minimum Required Balance Withdrawl Rejected")
elif WithdrawlAmt<=50000 and Balance>MinBalance:
    if WithdrawlAmt>50000:
        print("The Withdrawl Amount Cannot Exceed 50K")
    else:
        print(WithdrawlAmt,"Has Been Debited")

