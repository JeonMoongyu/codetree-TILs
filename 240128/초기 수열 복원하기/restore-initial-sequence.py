n = int(input())
arr = list(map(int,input().split()))


def list_of_perm(m):
    if m == 1:
        return [[1]]
    return sorted([ ex_perm[:i] + [m] + ex_perm[i:] \
                    for i in range(m) \
                    for ex_perm in list_of_perm(m-1) ])


def adj_sum(seq):
    return [ seq[i]+seq[i+1] for i in range(n-2) ]


for perm in list_of_seq(n):
    if adj_sum(perm) == arr:
        for elem in perm:
            print(elem, end=" ")
        break