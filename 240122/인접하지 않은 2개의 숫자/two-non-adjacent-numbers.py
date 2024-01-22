n = int(input())
arr = list(map(int,input().split()))
max_sum = 0
for i in range(n-2):
    for j in range(i+2,n):
        max_sum = max(max_sum,arr[i]+arr[j])
print(max_sum)