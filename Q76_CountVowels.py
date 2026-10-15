N=input("Enter A String : ")
Count=0
for i in N:
    if i.lower() in "aeiou":
        Count+=1
    else:
        continue
print(Count)