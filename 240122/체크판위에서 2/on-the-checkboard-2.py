R, C = tuple(map(int,input().split()))
board = [
    list(input().split())
    for _ in range(R)
]
ans = 0
for i in range(1,R-1):
    for j in range(1,C-2):
        for k in range(i+1,R-1):
            for l in range(j+1,C-1):
                if board[i][j] != board[0][0] and board[k][l] == board[0][0]:
                    ans += 1
print(ans)