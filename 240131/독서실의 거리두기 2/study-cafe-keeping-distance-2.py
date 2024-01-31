n = int(input())
arr = list(map(int,list(input())))

max_dist = 0
for i in range(n):
    if arr[i] == 1:
        for j in range(i+1,n):
            if arr[j] == 1:
                if j-i > max_dist:
                    max_dist = j-i
                    max_i = i
                    max_j = j
                break

max_dist_2 = 0
if arr[0] == 0:
    max_dist_2 = arr.index(1)
    idx = 0
if arr[-1] == 0:
    if arr[::-1].index(1) > max_dist_2:
        max_dist_2 = arr[::-1].index(1)
        idx = n-1

if max_dist_2 > 0 and max_dist_2 >= max_dist // 2:
    arr[idx] = 1
else:
    arr[(max_i+max_j)//2] = 1

ans = 1000
for i in range(n):
    if arr[i] == 1:
        for j in range(i+1,n):
            if arr[j] ==1:
                ans = min(ans,j-i)

print(ans)