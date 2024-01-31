n = int(input())
arr = list(map(int,list(input())))

idx_of_1s = [ i for i in range(n) if arr[i]==1 ]

max_int = 0
max_idx = 0
for j in range(len(idx_of_1s)-1):
    if idx_of_1s[j+1] - idx_of_1s[j] > max_int:
        max_int = idx_of_1s[j+1] - idx_of_1s[j]
        max_idx = idx_of_1s[j]

arr[ (max_idx*2 + max_int) // 2 ] = 1
idx_of_1s = [ i for i in range(n) if arr[i]==1 ]
min_int = 1000
for j in range(len(idx_of_1s)-1):
    if idx_of_1s[j+1] - idx_of_1s[j] < min_int:
        min_int = idx_of_1s[j+1] - idx_of_1s[j]
print(min_int)