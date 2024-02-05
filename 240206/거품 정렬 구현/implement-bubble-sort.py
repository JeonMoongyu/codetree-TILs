n = int(input())
arr = list(map(int,input().split()))
does_sorted = True

while True:
    does_sorted = True
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            does_sorted = False
    if does_sorted:
        break

for elem in arr:
    print(elem, end=" ")