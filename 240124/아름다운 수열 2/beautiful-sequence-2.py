n,m = tuple(map(int,input().split()))
a_seq = list(map(int,input().split()))
b_seq = list(map(int,input().split()))


def is_beatiful(seq): # given len(seq)==len(b_seq)
    b_copy = list(tuple(b_seq))
    for i in range(m):
        satisfied = False
        for j in range(m):
            if seq[i] == b_copy[j]:
                satisfied = True
                b_copy[j] = 0
                break
        if not satisfied:
            return False
    return True


ans = 0
for i in range(n-m+1):
    if is_beatiful(a_seq[i:i+m]):
        ans += 1

print(ans)