t,a,b = tuple(map(int,input().split()))
arr = [0] * 1001
for _ in range(t):
    c,x = input().split()
    x = int(x)
    arr[x] = c


def in_range(i):
    return 1<=i and i<=1000


def is_special(k):
    for i in range(1000):
        if in_range(k-i) and arr[k-i] == 'S' or \
           in_range(k+i) and arr[k+i] == 'S':
           return True
        if in_range(k-i) and arr[k-i] == 'N' or \
           in_range(k+i) and arr[k+i] == 'N':
           return False


ans = 0
for k in range(a,b+1):
    if is_special(k):
        ans += 1

print(ans)