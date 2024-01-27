n = int(input())
arr = list(map(int,input().split()))


def list_of_perm(n):
    if n == 1:
        return [[1]]
    return sorted([ ex_perm[:i] + [n] + ex_perm[i:] \
                    for i in range(n) \
                    for ex_perm in list_of_perm(n-1) ])


def adj_sum(perm):
    return [ perm[i]+perm[i+1] for i in range(n-2) ]


for perm in list_of_seq(n):
    if adj_sum(perm) == arr:
        for elem in perm:
            print(elem, end=" ")
        break