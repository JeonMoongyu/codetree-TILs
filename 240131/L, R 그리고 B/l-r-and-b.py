l_i, l_j, b_i, b_j, r_i, r_j = 0, 0, 0, 0, 0, 0

for i in range(1,11):
    row = input()
    for j in range(1,11):
        if row[j-1] == 'L':
            l_i, l_j = i, j
        if row[j-1] == 'B':
            b_i, b_j = i, j
        if row[j-1] == 'R':
            r_i, r_j = i, j

if l_i == r_i and r_i == b_i and \
   (l_j < r_j and r_j < b_j or l_j > r_j and r_j > b_j):
    ans = abs(l_j-b_j+1)
elif l_j == r_j and r_j == b_j and \
    (l_i < r_i and r_i < b_i or l_i > r_i and r_i > b_i):
    ans = abs(l_i-b_i+1)
else:
    ans = abs(l_i-b_i) + abs(l_j-b_j) - 1

print(ans)