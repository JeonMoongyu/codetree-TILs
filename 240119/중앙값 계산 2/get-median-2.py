n = int(input())
arr = list(map(int,input().split()))
for i in range(0,n,2):
    sorted_arr = sorted(arr[:i+1])
    print(sorted_arr[i//2], end=" ")