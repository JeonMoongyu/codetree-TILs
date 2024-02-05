n = int(input())
arr = list(map(int,input().split()))

for i in range(n-1):
    for j in range(i+1,n):
        min_idx = i
        if arr[j] < arr[i]:
            min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

for elem in arr:
    print(elem, end=" ")