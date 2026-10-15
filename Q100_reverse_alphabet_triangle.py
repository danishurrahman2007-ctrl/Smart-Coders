n = int(input("Enter number of rows (max 26): "))
for i in range(n, 0, -1):
    print(" ".join(chr(ord("A") + k) for k in range(i)))
