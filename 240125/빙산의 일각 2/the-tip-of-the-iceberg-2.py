n = int(input())
heights = [
    int(input())
    for _ in range(n)
]


def count_chunk(arr):
    if len(arr) == 1:
        return 1 if arr[0] > 0 else 0
    if arr[-2] <= 0 and arr[-1] > 0:
        return count_chunk(arr[:-1]) + 1
    else:
        return count_chunk(arr[:-1])


ans = 0
for h in range(1,1000):
    visible = [ heights[i]-h for i in range(n) ]
    ans = max(ans,count_chunk(visible))
print(ans)