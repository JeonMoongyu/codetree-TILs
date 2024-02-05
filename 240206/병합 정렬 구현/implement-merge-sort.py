n = int(input())
arr = list(map(int,input().split()))

def merge(low,mid,high):
    global arr

    merged_arr = []
    i, j = low, mid+1

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            merged_arr.append(arr[i])
            i += 1
        else:
            merged_arr.append(arr[j])
            j += 1
        
    while i <= mid:
        merged_arr.append(arr[i])
        i += 1

    while j <= high:
        merged_arr.append(arr[j])
        j += 1
        
    for i in range(low,high+1):
        arr[i] = merged_arr[i-low]


def merge_sort(low, high):
    global arr

    if low < high:
        mid = (low+high)//2
        merge_sort(low,mid)
        merge_sort(mid+1,high)
        merge(low,mid,high)
    


merge_sort(0,n-1)

for elem in arr:
    print(elem, end=" ")