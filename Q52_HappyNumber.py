N = int(input("Enter A Number: "))
Temp = N
while Temp > 9:
    total = 0
    while Temp > 0:
        digit = Temp % 10
        total += digit ** 2
        Temp //= 10
    Temp = total
if Temp == 1 or Temp == 7:
    print(f"{N} reaches 1! It Is A Happy Number")
else:
    print(f"{N} does not reach 1 It Is Not A Happy Number.")