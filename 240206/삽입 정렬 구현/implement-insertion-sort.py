n = int(input())
arr = list(map(int,input().split()))


def insertion_sort():
    for i in range(1,n):
        key = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > key:
                arr[j+1] = arr[j]
            else:
                break
        if j == 0 and arr[0] > key:
            arr[0] = key
        else:
            arr[j+1] = key
            


insertion_sort()

for elem in arr:
    print(elem, end=" ")