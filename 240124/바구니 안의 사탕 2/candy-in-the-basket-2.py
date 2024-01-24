n,k = tuple(map(int,input().split()))
arr = [ 0 for _ in range(101) ]
for _ in range(n):
    candies, box = tuple(map(int,input().split()))
    arr[box] += candies

ans = 0
for c in range(k,101-k):
    num_of_candies = 0
    for i in range(c-k,c+k+1):
        num_of_candies += arr[i]
    ans = max(ans,num_of_candies)

print(ans)