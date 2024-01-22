n, t = tuple(map(int,input().split()))
r, c, d = input().split()
r, c = int(r), int(c)

mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}
d = mapper[d]

dis, djs = [-1,0,0,1], [0,1,-1,0]


def in_range(i,j):
    return 1<=i and i<=n and 1<=j and j<=n


for _ in range(t):
    if in_range(r+dis[d],c+djs[d]):
        r += dis[d]
        c += djs[d]
    else:
        d = 3-d

print(r,c)