import sys

board = [
    list(map(int,input().split()))
    for _ in range(19)
]


def in_range(i,j):
    return 0<=i and i<19 and 0<=j and j<19


dis, djs = [0,1,1], [1,1,0]
for i in range(19):
    for j in range(19):
        if board[i][j] == 0:
            continue
        for di, dj in zip(dis,djs):
            cur_i = i
            cur_j = j
            win = True
            for _ in range(4):
                ni, nj = cur_i+di, cur_j+dj
                if not in_range(ni,nj) or board[ni][nj]!=board[i][j]:
                    win = False
                    break
                cur_i = ni
                cur_j = nj
            if win:
                print(board[i][j])
                print(i+di*2+1,j+dj*2+1)
                sys.exit()
print(0)