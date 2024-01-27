n = int(input())
arr = list(map(int,input().split()))


def list_of_seq(n):
    if n == 1:
        return [[1]]
    return sorted([ ex_seq[:i] + [n] + ex_seq[i:] \
                    for i in range(n) \
                    for ex_seq in list_of_seq(n-1) ])


def adj_sum(seq):
    return [ seq[i]+seq[i+1] for i in range(len(seq)-1) ]


for perm in list_of_seq(n):
    if adj_sum(perm) == arr:
        for elem in perm:
            print(elem, end=" ")
        break