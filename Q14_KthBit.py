# If Bit 1 then Is Set or else Not Set 
N=int(input("Enter A Number : "))
K=1
Mask=1<<K
if (N and Mask)!=0:
    print(f"The Bit At {K} Is 1")
else:
    print(f"The Bit At {K} Is 0")
