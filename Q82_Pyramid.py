N = int(input("Enter Number of Rows For The Pattern : "))
for i in range(1, N + 1):
    for j in range(N - i):
        print(" ", end="")
    for k in range(1, 2 * i):
        print("*", end="")
        
    print()