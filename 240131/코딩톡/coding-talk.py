import sys

n, m, p = tuple(map(int,input().split()))
data = [0]
for _ in range(m):
    c, u = input().split()
    data.append((c,int(u)))

if data[p][1] == 0:
    sys.exit()

check = [1] * n


def alp_to_num(x):
    return ord(x)-ord('A')


def num_to_alp(k):
    return chr(k+ord('A'))


for c, u in data[p:]:
    check[alp_to_num(c)] = 0

for c, u in data[1:p]:
    if u == data[p][1]:
        check[alp_to_num(c)] = 0

for i in range(n):
    if check[i]:
        print(num_to_alp(i), end=" ")