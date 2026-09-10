import math 

a=int(input("Enter a Value : "))
b=int(input("Enter b Value : "))
c=int(input("Enter c Value : "))
discriminant=b**2-4*a*c
if discriminant>0:
    x1=(-b+math.sqrt(abs(discriminant)))/(2*a)
    x2=(-b-math.sqrt(abs(discriminant)))/(2*a)
    print(x1,x2)
elif discriminant==0:
    x1=((-b)/(2*a))
    x2=((-b)/(2*a))
    print(x1,x2)
else:
    realpart=-b/2*a
    imagpart=(math.sqrt(abs(discriminant)))/(2*a)
    print(complex(realpart,imagpart))
    print(complex(realpart,-imagpart))

