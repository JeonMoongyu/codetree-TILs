arr = [
    list(map(int,list(str(input()))))
    for _ in range(3)
]


def cnt(_list):
    exist = [0] * 10
    for elem in _list:
        exist[elem] = 1
    return sum(exist)


ans = 0
for i in range(3):
    if cnt(arr[i]) == 2:
        ans += 1
for j in range(3):
    col_j = [ arr[i][j] for i in range(3) ]
    if cnt(col_j) == 2:
        ans += 1

diag1 = [ arr[i][i] for i in range(3) ]
if cnt(diag1) == 2:
    ans += 1

diag2 = [ arr[i][2-i] for i in range(3) ]
if cnt(diag2) == 2:
    ans += 1

print(ans)