n,k = tuple(map(int,input().split()))
arr = [ 0 for _ in range(101) ]
for _ in range(n):
    candies, box = tuple(map(int,input().split()))
    arr[box] += candies


def in_range(i):
    return 0<=i and i<101

    
ans = 0
for c in range(101):
    num_of_candies = 0
    for i in range(c-k,c+k+1):
        if in_range(i):
            num_of_candies += arr[i]
    ans = max(ans,num_of_candies)

print(ans)