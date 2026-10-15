A=[]
print("Enter List Elements : ")
while True:
    N=input()
    if N.lower()=="done":
        break
    A.append(int(N))
Target=int(input("Enter Your Target Number : "))
def binary_search(list, target):
  low, high = 0, len(list) - 1
  while low <= high:
    mid = (low + high) // 2
    if list[mid] == target:
      return mid
    elif list[mid] < target:
      low = mid + 1
    else:
      high = mid - 1
  return -1

result = binary_search(A, Target)

if result != -1:
  print(f"Found at index {result}")
else:
  print("Not found")