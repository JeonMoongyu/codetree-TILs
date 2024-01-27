import sys

n = int(input())
heights = [ int(input()) for _ in range(n) ]


def cost(lb):
    result = 0
    for h in heights:
        if h < lb:
            result += (h - lb)**2
        if h > lb+17:
            result += (h - lb - 17)**2
    return result


ans = sys.maxsize
for lb in range(0,84):
    ans = min(ans,cost(lb))
print(ans)