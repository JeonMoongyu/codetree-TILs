n = int(input())
arr = [0] + list(map(int,input().split()))


def heapify(arr, n ,i):
    largest = i
    left = i*2
    right = i*2 + 1

    if left <= n and arr[largest] < arr[left]:
        largest = left
    if right <= n and arr[largest] < arr[right]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr, n):
    for i in range(n//2, 0, -1):
        heapify(arr, n, i)
    arr[1], arr[n] = arr[n], arr[1]

    for j in range(n-1, 0, -1):
        heapify(arr, j, 1)
        arr[1], arr[j] = arr[j], arr[1]


heap_sort(arr, n)
for elem in arr[1:]:
    print(elem, end=" ")