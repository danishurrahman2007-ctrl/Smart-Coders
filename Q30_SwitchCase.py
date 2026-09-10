X=int(input("Enter First Number : "))
Y=int(input("Enter Second Number : "))
A=input("Enter '+' , '-' , '*' , or '//' : ")
match(A):
    case '+':
        print(X+Y) 
    case '-':
            print(X-Y)
    case '*':
            print(X*Y)
    case '//':
            print(X//Y)