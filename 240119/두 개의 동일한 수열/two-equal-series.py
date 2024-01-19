n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
arr1.sort()
arr2.sort()

satisfied = True
for i in range(n):
    if arr1[i] != arr2[i]:
        satisfied = False
        break

if satisfied:
    print("Yes")
else:
    print("No")