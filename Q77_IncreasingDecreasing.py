L = []
A = int(input("Enter Range Of Numbers : "))
for i in range(A):
    N = int(input("Enter A Number : "))
    L.append(N)

def IncDec(num_list):
    num_list.sort()
    print("Increasing Order:", num_list)
    dec_list = num_list[::-1]
    print("Decreasing Order:", dec_list)

IncDec(L)