n = int(input("Enter n (arrow size): "))
for i in range(1, n + 1):
    print("*" * i)
print("*" * (2 * n))
for i in range(n - 1, 0, -1):
    print("*" * i)
