n = int(input())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]


def dup(i1,j1,i2,j2):
    for k in range(3):
        for l in range(3):
            if i1 == i2 and j1+k == j2+l:
                return True
    return False 


def in_range(i1,j1,i2,j2):
    return 0<=i1 and i1<n and 0<=j1 and j1<n-2 and \
           0<=i2 and i2<n and 0<=j2 and j2<n-2


ans = 0
for i1 in range(n):
    for j1 in range(n):
        for i2 in range(n):
            for j2 in range(j1,n):
                if dup(i1,j1,i2,j2) or not in_range(i1,j1,i2,j2):
                    continue
                sum_val = 0
                for k in range(3):
                    sum_val += arr[i1][j1+k]
                for k in range(3):
                    sum_val += arr[i2][j2+k]
                ans = max(ans,sum_val)
                
print(ans)