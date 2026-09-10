a=1
b=0
if (bool(a) ^ bool(b)):
    a,b=b,a
else:
    print("Equal Numbers")
print(a)
print(b)
