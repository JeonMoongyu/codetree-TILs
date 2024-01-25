a,b,c = tuple(map(int,input().split()))

max_i = c//a
max_j = c//b

ans = 0
for i in range(max_i+1):
    for j in range(max_j+1):
        if a*i + b*j <= c:
            ans = max(ans,a*i + b*j)
print(ans)