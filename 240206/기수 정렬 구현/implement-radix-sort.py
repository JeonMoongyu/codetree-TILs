n = int(input())
arr = list(map(int,input().split()))


def digit(num, k):
    return (num // 10**(k-1)) % 10


def radix_sort():
    global arr
    for k in range(1,7):
        new_arr = [ [] for _ in range(10) ]
        for elem in arr:
            new_arr[digit(elem,k)].append(elem)
        store_arr = []
        for i in range(10):
            for elem in new_arr[i]:
                store_arr.append(elem)
        arr = store_arr


radix_sort()

for elem in arr:
    print(elem, end=" ")