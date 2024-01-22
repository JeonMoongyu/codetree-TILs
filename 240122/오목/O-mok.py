board = [
    list(map(int,input().split()))
    for _ in range(19)
]


def black_win_at(i,j):
    if 2<=i and i<=16:
        win = True
        for k in range(-2,3):
            if board[i+k][j] != 1:
                win = False
        if win:
            return True
    if 2<=j and j<=16:
        win = True
        for k in range(-2,3):
            if board[i][j+k] != 1:
                win = False
        if win:
            return True
    if 2<=i and i<=16 and 2<=j and j<=16:
        win = True
        for k in range(-2,3):
            if board[i+k][j+k] != 1:
                win = False
        if win:
            return True
        win = True
        for k in range(-2,3):
            if board[i-k][j+k] != 1:
                win = False
        if win:
            return True
    return False


def white_win_at(i,j):
    if 2<=i and i<=16:
        win = True
        for k in range(-2,3):
            if board[i+k][j] != 2:
                win = False
        if win:
            return True
    if 2<=j and j<=16:
        win = True
        for k in range(-2,3):
            if board[i][j+k] != 2:
                win = False
        if win:
            return True
    if 2<=i and i<=16 and 2<=j and j<=16:
        win = True
        for k in range(-2,3):
            if board[i+k][j+k] != 2:
                win = False
        if win:
            return True
        win = True
        for k in range(-2,3):
            if board[i-k][j+k] != 2:
                win = False
        if win:
            return True
    return False


someone_win = False
for i in range(19):
    for j in range(19):
        if black_win_at(i,j):
            someone_win = True
            print(1)
            print(i+1,j+1)
            break
        if white_win_at(i,j):
            someone_win = True
            print(2)
            print(i+1,j+1)
            break
    if someone_win:
        break
if not someone_win:
    print(0)