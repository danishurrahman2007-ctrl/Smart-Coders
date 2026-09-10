number  = int(input("Enter A Number : "))
count = 0
while number:
    if (number & 1) != 0:
        count += 1
    number = number >> 1

print(count)