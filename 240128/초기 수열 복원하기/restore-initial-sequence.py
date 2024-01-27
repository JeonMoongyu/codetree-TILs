n = int(input())
arr = list(map(int,input().split()))


def list_of_perm(m):
    if m == 1:
        return [[1]]
    return sorted([ ex_perm[:i] + [m] + ex_perm[i:] \
                    for i in range(m) \
                    for ex_perm in list_of_perm(m-1) ])


for perm in list_of_perm(n):
    satisfied = True
    for i in range(n-1):
        if perm[i]+perm[i+1] != arr[i]:
            satisfied = False
            break
    if satisfied:
        for elem in perm:
            print(elem, end=" ")
        break