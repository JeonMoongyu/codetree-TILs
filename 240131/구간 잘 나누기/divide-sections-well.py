import sys

n,m = tuple(map(int,input().split()))
arr = list(map(int,input().split()))

def num_of_int(arr, max_val): # max_val > arr[i] for all i
    curr_sum = 0
    result = 1
    for elem in arr:
        if curr_sum + elem > max_val:
            curr_sum = elem
            result += 1
        else:
            curr_sum += elem
    return result

max_val = sum(arr) + 1
while max_val > max(arr):
    if num_of_int(arr, max_val - 1) <= m:
        max_val -= 1
    else:
        break

print(max_val)