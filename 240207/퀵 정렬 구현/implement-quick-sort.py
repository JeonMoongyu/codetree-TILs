n = int(input())
arr = list(map(int,input().split()))


def quick_sort(arr, low, high):
    if low < high:
        pos = quick_partition(arr, low, high)
        quick_sort(arr, low, pos-1)
        quick_sort(arr, pos+1, high)
    

def quick_partition(arr, low, high):
    k, pivot = select_pivot(arr, low, high)
    arr[high], arr[k] = arr[k], arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def select_pivot(arr, low, high):
    a, b, c = low, (low+high)//2, high
    cand = [ (a,arr[a]), (b,arr[b]), (c,arr[c]) ]
    cand.sort(key= lambda x: x[1])
    return cand[1]


quick_sort(arr, 0, n-1)
for elem in arr:
    print(elem, end=" ")