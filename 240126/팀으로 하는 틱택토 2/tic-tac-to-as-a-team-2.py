arr = [
    list(map(int,list(str(input()))))
    for _ in range(3)
]


def did_won(_list):
    exist = [0] * 10
    for elem in _list:
        exist[elem] = 1
    return sum(exist)==2


def who_won(_list):
    a = _list[0]
    for elem in _list[1:]:
        if elem != a:
            return min(a,elem),max(a,elem)


won = [
    [0 for _ in range(10)]
    for _ in range(10)
]

for i in range(3):
    if did_won(arr[i]):
        a,b = who_won(arr[i])
        won[a][b] = 1
for j in range(3):
    col_j = [ arr[i][j] for i in range(3) ]
    if did_won(col_j):
        a,b = who_won(col_j)
        won[a][b] = 1

diag1 = [ arr[i][i] for i in range(3) ]
if did_won(diag1):
    a,b = who_won(diag1)
    won[a][b] = 1

diag2 = [ arr[i][2-i] for i in range(3) ]
if did_won(diag2):
    a,b = who_won(diag2)
    won[a][b] = 1

ans = 0
for row in won:
    ans += sum(row)
print(ans)