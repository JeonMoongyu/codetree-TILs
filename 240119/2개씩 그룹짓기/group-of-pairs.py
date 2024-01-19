n = int(input())
arr = list(map(int,input().split()))
arr.sort()
groups = [
    arr[i]+arr[2*n-1-i]
    for i in range(n)
]
print(max(groups))